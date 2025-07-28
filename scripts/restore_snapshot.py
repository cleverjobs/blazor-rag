#!/usr/bin/env python3
"""
Restore a Qdrant collection from a snapshot file.
"""

import os
import sys
import time
from qdrant_client import QdrantClient
from pathlib import Path

def wait_for_qdrant(client, max_retries=30):
    """Wait for Qdrant to be ready."""
    for i in range(max_retries):
        try:
            client.get_collections()
            print("✅ Qdrant is ready!")
            return True
        except Exception as e:
            print(f"⏳ Waiting for Qdrant... ({i+1}/{max_retries})")
            time.sleep(2)
    return False

def restore_snapshot(snapshot_name=None):
    """Restore a snapshot of the Qdrant collection."""
    
    # Detect if running in Docker container
    is_docker = os.path.exists('/.dockerenv') or os.getenv('QDRANT_URL')
    
    if is_docker:
        # Docker environment - use environment variables
        qdrant_url = os.getenv("QDRANT_URL", "qdrant:6333")
        collection_name = os.getenv("COLLECTION_NAME", "telerik_blazor_docs")
        snapshot_name = snapshot_name or os.getenv("SNAPSHOT_NAME")
        client = QdrantClient(url=f"http://{qdrant_url}")
        snapshot_path = f"/data/snapshots/{snapshot_name}"
    else:
        # Local environment
        client = QdrantClient(host="localhost", port=6333)
        collection_name = "telerik_blazor_docs"
        snapshot_path = f"data/snapshots/{snapshot_name}"
    
    if not snapshot_name:
        print("❌ Snapshot name is required")
        return False
    
    # Wait for Qdrant if in Docker
    if is_docker and not wait_for_qdrant(client):
        print("❌ Qdrant failed to start within timeout")
        return False
    
    try:
        # Check if snapshot file exists
        if not os.path.exists(snapshot_path):
            print(f"❌ Snapshot file not found: {snapshot_path}")
            return False
        
        print(f"📁 Found snapshot: {snapshot_path}")
        print(f"📊 Restoring collection: {collection_name}")
        
        if is_docker:
            # In Docker, we need to copy the snapshot to where Qdrant can access it
            # Qdrant expects snapshots to be accessible via HTTP API
            # We'll use the REST API to upload and restore
            import requests
            import shutil
            
            print("📸 Uploading snapshot to Qdrant...")
            
            # Upload snapshot via API
            upload_url = f"http://{qdrant_url}/collections/{collection_name}/snapshots/upload"
            
            with open(snapshot_path, 'rb') as f:
                files = {'snapshot': f}
                response = requests.post(upload_url, files=files)
                
                if response.status_code == 200:
                    print("✅ Snapshot uploaded successfully!")
                else:
                    print(f"❌ Failed to upload snapshot: {response.status_code} - {response.text}")
                    return False
        else:
            # Local environment - copy to Qdrant container
            import subprocess
            copy_result = subprocess.run([
                "docker", "compose", "cp", 
                snapshot_path,
                f"qdrant:/qdrant/snapshots/telerik_blazor_docs/{snapshot_name}"
            ], capture_output=True, text=True)
            
            if copy_result.returncode != 0:
                print(f"❌ Failed to copy snapshot to container: {copy_result.stderr}")
                return False
            
            print("📸 Copying snapshot to Qdrant container...")
            
            # Restore the collection
            print("🔄 Restoring collection from snapshot...")
            client.recover_snapshot(collection_name=collection_name, location=snapshot_path)
        
        # Wait a moment for restoration to complete
        time.sleep(5)
        
        # Verify restoration
        info = client.get_collection(collection_name)
        print(f"✅ Collection restored successfully!")
        print(f"   - Name: {collection_name}")
        print(f"   - Points: {info.points_count:,}")
        print(f"   - Vector size: {info.config.params.vectors.size}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error restoring snapshot: {e}")
        return False

def main():
    # Check if running in Docker environment
    is_docker = os.path.exists('/.dockerenv') or os.getenv('QDRANT_URL')
    
    if is_docker:
        # In Docker, get snapshot name from environment
        snapshot_name = os.getenv("SNAPSHOT_NAME")
        if not snapshot_name:
            print("❌ SNAPSHOT_NAME environment variable is required in Docker")
            sys.exit(1)
    else:
        # Local usage requires command line argument
        if len(sys.argv) != 2:
            print("Usage: python restore_qdrant_snapshot.py <snapshot_name>")
            print("\nExample:")
            print("  python scripts/restore_qdrant_snapshot.py telerik_blazor_docs-1883480512116257-2025-07-28-10-14-25.snapshot")
            sys.exit(1)
        snapshot_name = sys.argv[1]
    
    success = restore_snapshot(snapshot_name)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

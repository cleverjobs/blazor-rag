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
            # In Docker, copy snapshot to tmp directory for Qdrant
            import shutil
            qdrant_snapshot_dir = f"/tmp/qdrant_snapshots"
            os.makedirs(qdrant_snapshot_dir, exist_ok=True)
            qdrant_snapshot_path = f"{qdrant_snapshot_dir}/{snapshot_name}"
            
            print("📸 Copying snapshot for Qdrant...")
            shutil.copy2(snapshot_path, qdrant_snapshot_path)
            
            # Restore using local path
            client.recover_snapshot(
                collection_name=collection_name, 
                snapshot_name=snapshot_name,
                snapshot_path=qdrant_snapshot_dir
            )
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
            client.recover_snapshot(collection_name=collection_name, snapshot_name=snapshot_name)
        
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

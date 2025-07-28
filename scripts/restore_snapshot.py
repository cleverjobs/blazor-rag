#!/usr/bin/env python3
"""
Restore a Qdrant collection from a snapshot file.
"""

import os
import sys
from qdrant_client import QdrantClient
from pathlib import Path

def restore_snapshot(snapshot_name):
    """Restore a snapshot of the Qdrant collection."""
    
    # Connect to Qdrant
    client = QdrantClient(host="localhost", port=6333)
    
    collection_name = "telerik_blazor_docs"
    snapshot_path = f"data/snapshots/{snapshot_name}"
    
    try:
        # Check if snapshot file exists
        if not os.path.exists(snapshot_path):
            print(f"❌ Snapshot file not found: {snapshot_path}")
            return False
        
        print(f"📁 Found snapshot: {snapshot_path}")
        print(f"📊 Restoring collection: {collection_name}")
        
        # Copy snapshot to Qdrant container
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

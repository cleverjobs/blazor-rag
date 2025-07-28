#!/usr/bin/env python3
"""
Create a snapshot of the Qdrant collection for backup/restore purposes.
"""

import os
import sys
from qdrant_client import QdrantClient
from datetime import datetime

def create_snapshot():
    """Create a snapshot of the Qdrant collection."""
    
    # Connect to Qdrant
    client = QdrantClient(host="localhost", port=6333)
    
    collection_name = "telerik_blazor_docs"
    
    try:
        # Check if collection exists
        collections = client.get_collections()
        collection_exists = any(col.name == collection_name for col in collections.collections)
        
        if not collection_exists:
            print(f"❌ Collection '{collection_name}' does not exist!")
            return False
            
        # Get collection info
        info = client.get_collection(collection_name)
        print(f"📊 Collection info:")
        print(f"   - Name: {collection_name}")
        print(f"   - Points: {info.points_count}")
        print(f"   - Vector size: {info.config.params.vectors.size}")
        print()
        
        # Create snapshot
        print("📸 Creating snapshot...")
        snapshot_info = client.create_snapshot(collection_name=collection_name)
        
        print(f"✅ Snapshot created successfully!")
        print(f"   - Snapshot name: {snapshot_info.name}")
        print(f"   - Creation time: {snapshot_info.creation_time}")
        print(f"   - Size: {snapshot_info.size} bytes")
        
        # Copy snapshot to data/snapshots directory
        print("📁 Copying snapshot to data/snapshots...")
        import subprocess
        copy_result = subprocess.run([
            "docker", "compose", "cp", 
            f"qdrant:/qdrant/snapshots/telerik_blazor_docs/{snapshot_info.name}", 
            f"./data/snapshots/"
        ], capture_output=True, text=True)
        
        if copy_result.returncode == 0:
            print(f"✅ Snapshot copied to: data/snapshots/{snapshot_info.name}")
            
            # Also copy checksum file
            checksum_result = subprocess.run([
                "docker", "compose", "cp", 
                f"qdrant:/qdrant/snapshots/telerik_blazor_docs/{snapshot_info.name}.checksum", 
                f"./data/snapshots/"
            ], capture_output=True, text=True)
            
            if checksum_result.returncode == 0:
                print(f"✅ Checksum copied to: data/snapshots/{snapshot_info.name}.checksum")
        else:
            print(f"⚠️  Failed to copy snapshot: {copy_result.stderr}")
        
        print("\n📋 Snapshot Details:")
        print(f"   - File: data/snapshots/{snapshot_info.name}")
        print(f"   - Collection: {collection_name}")
        print(f"   - Points: {info.points_count:,}")
        print(f"   - Vector Dimensions: {info.config.params.vectors.size}")
        print(f"   - Size: {snapshot_info.size:,} bytes (~{snapshot_info.size / (1024*1024):.1f} MB)")
        print(f"\n🔄 To restore this snapshot:")
        print(f"   python scripts/restore_qdrant_snapshot.py {snapshot_info.name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating snapshot: {e}")
        return False

if __name__ == "__main__":
    success = create_snapshot()
    sys.exit(0 if success else 1)

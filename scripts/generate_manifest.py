#!/usr/bin/env python3
"""
Generate File Manifest - Create inventory of all files in repository
Creates SHA256 hashes, metadata, and outputs to CSV/JSON
"""

import os
import json
import hashlib
import csv
from pathlib import Path
from datetime import datetime

def get_file_hash(filepath):
    """Calculate SHA256 hash of file"""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def get_file_metadata(filepath):
    """Extract file metadata"""
    try:
        stat = os.stat(filepath)
        return {
            "size": stat.st_size,
            "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        }
    except Exception as e:
        return {"error": str(e)}

def generate_manifest(root_dir="."):
    """Generate manifest of all files"""
    manifest = []
    
    print(f"Scanning directory: {root_dir}")
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories and common exclusions
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        
        for filename in filenames:
            if filename.startswith('.'):
                continue
                
            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, root_dir)
            
            print(f"  Processing: {rel_path}")
            
            file_hash = get_file_hash(filepath)
            metadata = get_file_metadata(filepath)
            
            manifest.append({
                "filename": filename,
                "path": rel_path,
                "extension": os.path.splitext(filename)[1],
                "hash": file_hash,
                "size": metadata.get("size", 0),
                "created": metadata.get("created", ""),
                "modified": metadata.get("modified", ""),
            })
    
    print(f"\nTotal files found: {len(manifest)}")
    return manifest

def save_manifest(manifest, output_dir="data"):
    """Save manifest to JSON and CSV"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Save as JSON
    json_path = os.path.join(output_dir, "file_manifest.json")
    with open(json_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"✓ Saved JSON manifest: {json_path}")
    
    # Save as CSV
    csv_path = os.path.join(output_dir, "file_manifest.csv")
    if manifest:
        keys = manifest[0].keys()
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(manifest)
        print(f"✓ Saved CSV manifest: {csv_path}")
    
    # Save statistics
    stats = {
        "total_files": len(manifest),
        "total_size_bytes": sum(f.get("size", 0) for f in manifest),
        "total_size_mb": sum(f.get("size", 0) for f in manifest) / (1024 * 1024),
        "file_types": {},
        "largest_files": sorted(manifest, key=lambda x: x.get("size", 0), reverse=True)[:20],
        "timestamp": datetime.now().isoformat(),
    }
    
    # Count by extension
    for f in manifest:
        ext = f.get("extension", "no_extension")
        stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1
    
    stats_path = os.path.join(output_dir, "manifest_statistics.json")
    with open(stats_path, 'w') as f:
        json.dump(stats, f, indent=2)
    print(f"✓ Saved statistics: {stats_path}")
    
    print(f"\n📊 Statistics:")
    print(f"   Total files: {stats['total_files']}")
    print(f"   Total size: {stats['total_size_mb']:.2f} MB")
    print(f"   File types: {len(stats['file_types'])}")
    for ext, count in sorted(stats['file_types'].items(), key=lambda x: x[1], reverse=True):
        print(f"      {ext if ext else '(no ext)'}: {count}")

if __name__ == "__main__":
    manifest = generate_manifest(".")
    save_manifest(manifest)
    print("\n✅ Manifest generation complete!")

#!/usr/bin/env python3
"""
Check References - Verify all cross-references and links between files
Identifies broken references and creates dependency graph
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def load_json_files(root_dir="."):
    """Load all JSON files for reference checking"""
    files = {}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        for filename in filenames:
            if filename.endswith('.json'):
                filepath = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(filepath, root_dir)
                
                try:
                    with open(filepath, 'r') as f:
                        files[rel_path] = json.load(f)
                except:
                    pass
    
    return files

def find_references(content, parent_file=""):
    """Find file references in content"""
    references = []
    
    if isinstance(content, dict):
        # Look for common reference keys
        for key in ["references", "related_files", "dependencies", "see_also", "source", "sources"]:
            if key in content:
                value = content[key]
                if isinstance(value, str):
                    references.append({"type": key, "target": value, "from": parent_file})
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, str):
                            references.append({"type": key, "target": item, "from": parent_file})
                        elif isinstance(item, dict) and "path" in item:
                            references.append({"type": key, "target": item["path"], "from": parent_file})
        
        # Recursively search nested objects
        for value in content.values():
            if isinstance(value, (dict, list)):
                references.extend(find_references(value, parent_file))
    
    elif isinstance(content, list):
        for item in content:
            if isinstance(item, (dict, list)):
                references.extend(find_references(item, parent_file))
    
    return references

def check_references(files):
    """Check all references for validity"""
    all_references = []
    broken_references = []
    file_paths = set(files.keys())
    
    print("Checking references...")
    
    for file_path, content in files.items():
        references = find_references(content, file_path)
        all_references.extend(references)
        
        for ref in references:
            target = ref["target"]
            
            # Check if reference exists
            if target not in file_paths:
                # Try with common extensions
                found = False
                for ext in ['.json', '.md', '.txt']:
                    if (target + ext) in file_paths:
                        found = True
                        break
                
                if not found:
                    broken_references.append({
                        "from": file_path,
                        "target": target,
                        "type": ref["type"],
                    })
    
    return {
        "total_references": len(all_references),
        "valid_references": len(all_references) - len(broken_references),
        "broken_references": len(broken_references),
        "details": broken_references,
    }

def create_dependency_graph(files):
    """Create dependency graph of files"""
    graph = defaultdict(list)
    
    for file_path, content in files.items():
        references = find_references(content, file_path)
        for ref in references:
            target = ref["target"]
            graph[file_path].append(target)
    
    return dict(graph)

def find_orphaned_files(files, graph):
    """Find files that are never referenced"""
    referenced_files = set()
    
    for deps in graph.values():
        referenced_files.update(deps)
    
    orphaned = []
    for file_path in files.keys():
        if file_path not in referenced_files and file_path not in graph:
            orphaned.append(file_path)
    
    return orphaned

def save_reference_report(check_results, graph, orphaned, output_dir="data"):
    """Save reference checking report"""
    Path(output_dir).mkdir(exist_ok=True)
    
    report = {
        "timestamp": __import__('datetime').datetime.now().isoformat(),
        "reference_summary": check_results,
        "dependency_graph": graph,
        "orphaned_files": orphaned,
        "statistics": {
            "total_files": len(graph),
            "total_dependencies": sum(len(deps) for deps in graph.values()),
            "total_orphaned": len(orphaned),
        },
    }
    
    report_path = Path(output_dir) / "reference_check_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"✓ Saved reference report: {report_path}")
    
    # Print summary
    print("\n📊 Reference Check Summary:")
    print(f"   Total references: {check_results['total_references']}")
    print(f"   Valid references: {check_results['valid_references']}")
    print(f"   Broken references: {check_results['broken_references']}")
    print(f"   Orphaned files: {len(orphaned)}")
    
    if check_results["broken_references"] > 0:
        print(f"\n⚠️  Broken References ({check_results['broken_references']}):")
        for ref in check_results["details"][:10]:
            print(f"   - {ref['from']} -> {ref['target']}")
        if len(check_results["details"]) > 10:
            print(f"   ... and {len(check_results['details']) - 10} more")
    
    if orphaned:
        print(f"\n📦 Orphaned Files ({len(orphaned)}):")
        for f in orphaned[:10]:
            print(f"   - {f}")
        if len(orphaned) > 10:
            print(f"   ... and {len(orphaned) - 10} more")

if __name__ == "__main__":
    print("Loading JSON files...")
    files = load_json_files(".")
    print(f"Loaded {len(files)} JSON files")
    
    print("Checking references...")
    check_results = check_references(files)
    
    print("Creating dependency graph...")
    graph = create_dependency_graph(files)
    
    print("Finding orphaned files...")
    orphaned = find_orphaned_files(files, graph)
    
    print("Saving report...")
    save_reference_report(check_results, graph, orphaned)
    
    print("\n✅ Reference checking complete!")

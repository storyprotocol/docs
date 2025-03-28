#!/usr/bin/env python3
import json
import sys
import argparse

def find_additional_resources_section(navigation):
    """Find the Additional Resources section specifically in the Network tab"""
    for tab in navigation.get("tabs", []):
        for group in tab.get("groups", []):
            if any(page == "network/more/additional-resources" for page in group.get("pages", [])):
                return group
            if group.get("group") == "Additional Resources":
                return group
            for page in group.get("pages", []):
                if isinstance(page, dict) and page.get("group") == "Additional Resources":
                    return page
    
    return None

def add_file_to_navigation(config, file_path):
    """Add a new file to the navigation structure"""
    file_path = file_path.lstrip('/')
    if file_path.endswith('.md'):
        file_path = file_path[:-3]  
    elif file_path.endswith('.mdx'):
        file_path = file_path[:-4]  

    if file_path.startswith("network/more/"):
        resources_section = find_additional_resources_section(config["navigation"])
        
        if resources_section:
            pages = resources_section.get("pages", [])
            page_name = file_path
            
            if page_name not in pages:
                pages.append(page_name)
                print(f"Added '{page_name}' to the Additional Resources section")
                return True
            else:
                print(f"File '{page_name}' already exists in navigation")
                return False
        else:
            print("Could not find the Additional Resources section in the navigation")
            return False
    else:
        print(f"Could not find appropriate position for '{file_path}' in navigation structure")
        return False

def main():
    parser = argparse.ArgumentParser(description='Add a file to the navigation structure in the docs.json file')
    parser.add_argument('file_path', help='Path of the file to add (relative to content root)')
    parser.add_argument('--config', default='docs.json', help='Path to the docs.json configuration file')
    
    args = parser.parse_args()
    
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return 1
    
    success = add_file_to_navigation(config, args.file_path)
    
    if success:
        try:
            with open(args.config, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"Updated configuration file: {args.config}")
        except Exception as e:
            print(f"Error writing configuration file: {e}")
            return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
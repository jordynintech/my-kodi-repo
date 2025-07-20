#!/usr/bin/env python3
"""
Simple script to update your Kodi repository when you add new add-ons
"""

import os
import xml.etree.ElementTree as ET
import hashlib
import zipfile

def generate_addons_xml(zips_dir='zips', output_file='addons.xml'):
    """Generate addons.xml from all add-on directories"""
    addons_root = ET.Element('addons')
    
    # Add the repository add-on itself
    repo_addon = ET.SubElement(addons_root, 'addon')
    repo_addon.set('id', 'repository.jordynintech')
    repo_addon.set('name', "Jordyn's Kodi Repository")
    repo_addon.set('version', '1.0.1')
    repo_addon.set('provider-name', 'Jordyn in Tech')
    
    # Repository extension
    repo_ext = ET.SubElement(repo_addon, 'extension')
    repo_ext.set('point', 'xbmc.addon.repository')
    repo_ext.set('name', "Jordyn's Kodi Repository")
    
    repo_dir = ET.SubElement(repo_ext, 'dir')
    info = ET.SubElement(repo_dir, 'info')
    info.set('compressed', 'false')
    info.text = 'https://raw.githubusercontent.com/jordynintech/my-kodi-repo/main/addons.xml'
    
    checksum = ET.SubElement(repo_dir, 'checksum')
    checksum.text = 'https://raw.githubusercontent.com/jordynintech/my-kodi-repo/main/addons.xml.md5'
    
    datadir = ET.SubElement(repo_dir, 'datadir')
    datadir.set('zip', 'true')
    datadir.text = 'https://raw.githubusercontent.com/jordynintech/my-kodi-repo/main/zips/'
    
    # Repository metadata
    repo_meta = ET.SubElement(repo_addon, 'extension')
    repo_meta.set('point', 'xbmc.addon.metadata')
    
    summary = ET.SubElement(repo_meta, 'summary')
    summary.text = "A personal repository of my favorite Kodi addons."
    
    description = ET.SubElement(repo_meta, 'description')
    description.text = "This repository contains my favorite add-ons and is not official."
    
    platform = ET.SubElement(repo_meta, 'platform')
    platform.text = 'all'
    
    # Add actual add-ons
    addon_count = 0
    for item in os.listdir(zips_dir):
        item_path = os.path.join(zips_dir, item)
        
        if os.path.isdir(item_path) and not item.startswith('.'):
            addon_xml_path = os.path.join(item_path, 'addon.xml')
            if os.path.exists(addon_xml_path):
                try:
                    tree = ET.parse(addon_xml_path)
                    addon_elem = tree.getroot()
                    
                    if addon_elem.tag == 'addon':
                        # Skip repository add-ons
                        extensions = addon_elem.findall('.//extension[@point]')
                        is_repo = any(ext.get('point') == 'xbmc.addon.repository' for ext in extensions)
                        
                        if not is_repo:
                            addons_root.append(addon_elem)
                            addon_count += 1
                            print(f"Added add-on: {addon_elem.get('id')} v{addon_elem.get('version')}")
                            
                except ET.ParseError as e:
                    print(f"Error parsing {addon_xml_path}: {e}")
                    continue
    
    # Write the addons.xml file
    tree = ET.ElementTree(addons_root)
    ET.indent(tree, space="  ", level=0)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    
    # Generate MD5 checksum
    with open(output_file, 'rb') as f:
        content = f.read()
        md5_hash = hashlib.md5(content).hexdigest()
    
    with open(f"{output_file}.md5", 'w') as f:
        f.write(md5_hash)
    
    print(f"Generated {output_file} with {addon_count} add-ons and {output_file}.md5")

def main():
    print("Updating Kodi repository...")
    generate_addons_xml()
    print("\nRepository updated! Don't forget to commit and push changes to GitHub.")
    print("\nTo add a new add-on:")
    print("1. Create a directory in 'zips/' with the add-on ID as the name")
    print("2. Put the addon.xml file in that directory")
    print("3. Put the .zip file for the add-on in that directory")
    print("4. Run this script again")
    print("5. Commit and push to GitHub")

if __name__ == '__main__':
    main()
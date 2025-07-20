import os
import zipfile
import shutil

ZIPS_DIR = 'zips'

# Helper to extract addon id from addon.xml
import xml.etree.ElementTree as ET

def get_addon_id_from_xml(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        return root.attrib.get('id')
    except Exception as e:
        print(f"Error reading addon.xml: {e}")
        return None

def organize_addons():
    for entry in os.listdir(ZIPS_DIR):
        entry_path = os.path.join(ZIPS_DIR, entry)
        # Only process loose ZIPs (not in folders)
        if os.path.isfile(entry_path) and entry.lower().endswith('.zip'):
            print(f"Processing {entry}...")
            with zipfile.ZipFile(entry_path, 'r') as zip_ref:
                # Find addon.xml in the ZIP
                addon_xml_name = None
                for name in zip_ref.namelist():
                    if name.endswith('addon.xml'):
                        addon_xml_name = name
                        break
                if not addon_xml_name:
                    print(f"  No addon.xml found in {entry}, skipping.")
                    continue
                # Extract addon.xml to temp location
                temp_xml = os.path.join(ZIPS_DIR, 'temp_addon.xml')
                zip_ref.extract(addon_xml_name, ZIPS_DIR)
                extracted_xml_path = os.path.join(ZIPS_DIR, addon_xml_name)
                # Read addon id
                addon_id = get_addon_id_from_xml(extracted_xml_path)
                if not addon_id:
                    # Fallback: use filename up to first dash
                    addon_id = entry.split('-')[0]
                addon_folder = os.path.join(ZIPS_DIR, addon_id)
                os.makedirs(addon_folder, exist_ok=True)
                # Move ZIP into folder
                shutil.move(entry_path, os.path.join(addon_folder, entry))
                # Move addon.xml into folder (rename if needed)
                shutil.move(extracted_xml_path, os.path.join(addon_folder, 'addon.xml'))
                # Clean up any temp dirs created by extraction
                temp_dir = os.path.join(ZIPS_DIR, addon_xml_name.split('/')[0])
                if os.path.isdir(temp_dir):
                    shutil.rmtree(temp_dir)
                print(f"  Organized into {addon_folder}/")
    print("Done organizing add-ons.")

if __name__ == '__main__':
    organize_addons() 
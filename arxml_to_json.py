import xml.etree.ElementTree as ET
import json
import argparse

def arxml_to_dict(element):
    """Recursively convert an ElementTree element into a dictionary."""
    result_dict = {}
    
    # Include element attributes if any
    if element.attrib:
        # Use attribute keys as-is, you may want to process namespaces if needed
        result_dict.update({f"@{key}": value for key, value in element.attrib.items()})

    children = list(element)
    if children:

        child_dict = {}
        for child in children:
            child_tag = child.tag.split('}')[-1]  
            child_data = arxml_to_dict(child)
            # If tag already exists, convert to list
            if child_tag in child_dict:
                if not isinstance(child_dict[child_tag], list):
                    child_dict[child_tag] = [child_dict[child_tag]]
                child_dict[child_tag].append(child_data)
            else:
                child_dict[child_tag] = child_data
        result_dict.update(child_dict)
    else:
        # Leaf node, get text
        text = element.text.strip() if element.text else ''
        if text:
            result_dict = text if not result_dict else {**result_dict, "#text": text}
        else:
            if not result_dict:
                result_dict = None  # Empty element
    
    return result_dict

def save_json_output(data, output_file):
    """Save dictionary data to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def main():
    # Add argparse implementation
    parser = argparse.ArgumentParser(description='Convert ARXML file to JSON format')
    parser.add_argument('input_file', help='Input ARXML file path')
    parser.add_argument('output_file', help='Output JSON file path')
    
    arguments = parser.parse_args()

    tree = ET.parse(arguments.input_file)
    root = tree.getroot()

    root_tag = root.tag.split('}')[-1]
    arxml_dict = {root_tag: arxml_to_dict(root)}

    # Save JSON output
    save_json_output(arxml_dict, arguments.output_file)

    print(f"Converted {arguments.input_file} to {arguments.output_file}")

if __name__ == "__main__":
    main()
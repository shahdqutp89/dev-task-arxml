
import argparse
from arxml_manager import ARXMLManagerFactory

def main():
    parser = argparse.ArgumentParser(description='Process ARXML file with attribute addition')
    parser.add_argument('input_file', help='Input ARXML file path')
    parser.add_argument('output_file', help='Output ARXML file path')
    
    arguments = parser.parse_args()
    
    manager = ARXMLManagerFactory.create_standard_manager()
    manager.load_arxml_file(arguments.input_file)
    manager.add_attribute_by_tag("ECUC-MODULE-CONFIGURATION-VALUES", "version", "1.0")
    manager.save_arxml_file(arguments.output_file)

if __name__ == "__main__":
    main()
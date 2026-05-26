#!/usr/bin/env python3
"""Basic Python CSV to JSON converter"""

import xml.etree.ElementTree as ET  # XML manipulation lib
import xml.dom.minidom            # NOT required but used in <3.9 to indent xml
import os                         # Check file was created then delete.
from pathlib import Path          # Optional extra checks on created file.
import mimetypes                  # Same optional extra checks.

# ============= MINIMAL IMPLEMENTATION ===============


# ===== OFFICIAL EXERCISE METHODS ======
def serialize_to_xml(dictionary, filename):
    rootElement = ET.Element('data')

    # Parsing dict, creating "sub element" foor each element.
    for name, value in dictionary.items():
        metadata = ET.SubElement(rootElement, name)
        metadata.text = value

    # METHOD 1
    # tree = ET.ElementTree(rootElement)
    # tree.write(filename, xml_declaration=True, encoding="utf-8")
    # METHOD 2: formatting with dedicated module then basic write
    raw = ET.tostring(rootElement, encoding="unicode")
    pretty = xml.dom.minidom.parseString(raw).toprettyxml(indent="    ")
    # Remove xml declaration apparently checker doesn't expect it'
    pretty = "\n".join(pretty.split("\n")[1:])
    with open(filename, 'w') as f:
        f.write(pretty)


def deserialize_from_xml(filename):
    dict_from_xml = {}
    try:
        xmlTree = ET.parse(filename)
        treeRoot = xmlTree.getroot()
        for child in treeRoot:
            dict_from_xml[child.tag] = child.text
        return dict_from_xml
    except Exception as e:
        return None


# ===== OFFICIAL EXERCISE SELF-TEST PROCESS (single child level xml) ======
def single_level_data_tests():
    print("===== SELF-TEST: START =====")
    sample_singlelevel_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    print("\n@dev: Step 0: Creating our test dictionary")
    test_source = sample_singlelevel_dict

    print("\n@dev: Step 1: trying the conversion to XML")
    test_converted = "PythonDictConverted.xml"
    print("Dictionary used:", test_source, sep="\n")
    serialize_to_xml(sample_singlelevel_dict, test_converted)

    print("\n@dev: Step 2a: checking a file has been created")
    print(f"File {test_converted} created? {os.path.exists(test_converted)}")
    print("\n@dev: Step 2b: checking it's valid xml")
    try:
        # Just to learn how to use, but I know it's a .json file
        p = Path(test_converted)
        # Warning do not forget the . before actual file extension
        print(f"File has json extension? {p.suffix == '.xml'}")
        # Method to get file basename
        print(f"  and its basename is: {p.stem}")
        with open(test_converted, 'r') as f:
            print("File content: \n ----", f.read(), "-----", sep="\n")
        mime_type, encoding = mimetypes.guess_type(test_converted)
        print(f"Mimetype is xml? {mime_type == 'application/xml'}")
    except Exception as e:
        print(e)

    print("\n@dev: Step 3: converting FROM XML back to dict")
    try:
        # USELESS: ElementTree can take in a simple pathname
        # with open(test_converted) as xmlFile:
        #    recreated = deserialize_from_xml(xmlFile)
        recreated = deserialize_from_xml(test_converted)
    except Exception as e:
        print(e)
    print(f"Same as original? {recreated == sample_singlelevel_dict}")

    print(f"\n@dev: Step 4: cleaning up filesystem (rm {test_converted}")
    try:
        os.remove(test_converted)
    except Exception as e:
        print(e)
    print(f"@dev: file removed/absent? {not os.path.exists(test_converted)}")
    print("\n===== SELF-TEST: END =====")


# ===== SELF-TEST =====
if __name__ == "__main__":
    single_level_data_tests()

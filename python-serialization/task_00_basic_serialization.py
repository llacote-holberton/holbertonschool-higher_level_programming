#!/usr/bin/env python3
"""Basic Python dictionary to JSON string serialization module"""

import json     # Module providing native JSON (de)serialization
import pickle   # To try and see the difference
import os       # To clean up files created from self-tests


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary object into JSON string on filesystem"""

    # Your code here to serialize and save data to the specified file
    if not isinstance(data, dict):
        pass
    data_as_json = json.dumps(data)
    with open(filename, 'w') as f:
        try:
            f.write(data_as_json)
            return True
        except OSError as e:
            return False


def load_and_deserialize(filename):
    """Parses a JSON string stored on filesystem as a dictionary"""

    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r') as f:
        data_as_json = f.read()
        return json.loads(data_as_json)


if __name__ == "__main__":
    original_dict = {"key": "house"}
    print(dir(original_dict))
    print("\n@dev: Step 0: comparing pickle and json serialization")
    print(f"Pickle first: \n {pickle.dumps(original_dict)}")
    print(f"JSON first: \n {json.dumps(original_dict)}")

    print("@dev: now trying my functions")
    test_file = ".test_json_dump.tmp"
    print("@dev: Step 0: displaying dict with Python for reference")
    print(original_dict)

    print("\n@dev: Step 1: writing to JSON file")
    serialize_and_save_to_file(original_dict, test_file)
    print(f"@dev: file created/rewritten? {os.path.exists(test_file)}")
    print("\n@dev: Step 2: reconstituting dict")
    recreated_dict = load_and_deserialize(test_file)
    print("\n@dev: Step 3: checking everything went fine")
    print(recreated_dict)
    print(f"@dev: Same dictionary? {original_dict == recreated_dict}")
    print(f"\n@dev: Step 4: cleaning up filesystem (rm {test_file}")
    os.remove(test_file)
    print(f"@dev: file removed? {not os.path.exists(test_file)}")
    print(f"\n@dev: END")

#!/usr/bin/env python3
"""Basic Python CSV to JSON converter"""

import csv      # To convert to/from csv
import json     # To convert to/from json
import os       # To check file creation and clean up afterwards


def convert_csv_to_json(csv_filename):
    """Basic converter which always writes converted to data.json"""
    destination_file = "data.json"
    try:
        # Contrarily to draft I do prefer slitting steps and responsabilities.
        # First ensure we get exploitable data from given filename.
        temp_dict = []
        with open(csv_filename) as f:
            temp_dict = list(csv.DictReader(f))

        with open(destination_file, 'w') as j:
            json.dump(temp_dict, j)
            return True
    except Exception as e:
        # print(e)
        return False


if __name__ == "__main__":
    print("===== SELF-TEST: START =====")

    print("\n@dev: Step 0: Verifying we have a source csv")
    test_source = "myCsvSource.csv"
    test_converted = "data.json"

    print("\n@dev: Step 1: trying the conversion")
    convert_csv_to_json(test_source)

    print("\n@dev: Step 2: checking a file has been created")
    print(f"File {test_converted} created? {os.path.exists(test_converted)}")

    print("\n@dev: Step 3: comparing 'list of dicts' creation: csv vs json")
    try:
        with open(test_source) as csvFile:
            print("Recreating dict from csv")
            dictListsFromCsv = list(csv.DictReader(csvFile))
            print(dictListsFromCsv)
        with open(test_converted) as jsonFile:
            print("Recreating dict from json")
            dictListsFromJson = json.load(jsonFile)
            print(dictListsFromJson)
    except Exception as e:
        print(e)
    print(f"Same from json and csv? {dictListsFromCsv == dictListsFromJson}")

    print(f"\n@dev: Step 4: cleaning up filesystem (rm {test_converted}")
    try:
        os.remove(test_converted)
    except Exception as e:
        print(e)
    print(f"@dev: file removed/absent? {not os.path.exists(test_converted)}")
    print("\n===== SELF-TEST: END =====")

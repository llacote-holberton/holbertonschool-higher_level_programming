#!/usr/bin/env python3
"""Basic Python CSV to JSON converter"""

import csv      # To convert to/from csv
import json     # To convert to/from json
import os       # To check file creation and clean up afterwards
from pathlib import Path  # Unnecessary, just me experimenting
import mimetypes          # Same, just expanding potential. :)


def convert_csv_to_json(csv_filename):
    """Basic converter which always writes converted to data.json"""
    destination_file = "data.json"
    try:
        with open(csv_filename) as f:
            temp_dict = []
            # Creating an iterable object thanks to dedicated method
            #   provided by csv module.
            # "Iterable" being an object which can be automatically
            #   converted into a "loop stack" with a "for i in object"
            #   expression because it implements specific methods
            # Confer https://stackoverflow.com/a/32800536 and
            # https://docs.python.org/3/library/
            #       collections.abc.html#collections.abc.Iterable
            csvLineByLineIterable = csv.DictReader(f)
            # NOTE: above just creates an iterable, does NOT actually read data
            print(csvLineByLineIterable)
            # Method 1: classic loop - Explicit but no necessary here.
            # temp_dict = []
            # for item in csvLineByLineIterable:
            #     temp_dict.append(item)
            # Method 2: list "comprehension", confer https://medium.com
            #       /@anshubantra/comprehensions-in-python-95b73ec21d2a
            # temp_dict = [item for item in csvLineByLineIterable]
            # Method 3: since our target object is an Iterable we can
            #   also just use the list "instanciator"
            # temp_dict = list(csvLineByLineIterable)
            # And technically we can therefore avoid all that complexity...
            with open(destination_file, 'w') as j:
                # Nested "get Iterable from csv" -> convert to list
                #   -> serialize and write result to file.
                # Beware: dump WITHOUT s (otherwise just returns text)
                json.dump(list(csv.DictReader(f)), j)
            return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    print("===== SELF-TEST: START =====")
    print("\n@dev: Step 0: Verifying we have a source csv")
    test_source = "myCsvSource.csv"
    test_converted = "data.json"
    print("\n@dev: Step 1: trying the conversion")
    convert_csv_to_json(test_source)
    print("\n@dev: Step 2a: checking a file has been created")
    print(f"File {test_converted} created? {os.path.exists(test_converted)}")
    print("\n@dev: Step 2b: checking it's valid json")
    try:
        # Just to learn how to use, but I know it's a .json file
        p = Path(test_converted)
        # Warning do not forget the . before actual file extension
        print(f"File has json extension? {p.suffix == '.json'}")
        # Method to get file basename
        print(f"  and its basename is: {p.stem}")
        with open(test_converted, 'r') as f:
            print(f.read())
        mime_type, encoding = mimetypes.guess_type(test_converted)
        print(mime_type)
        print(f"Mimetype is json? {mime_type == "application/json"}")
        # Fun fact: it's not "text/json" because "text/" implies data
        #   directly readable by human without preprocess.
        # JSON usually requires a parser to be easy to read by human,
        #   first designed for data to be consumed by applications.
        # Hence the counter-intuitive official categorization.
    except Exception as e:
        print(e)

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

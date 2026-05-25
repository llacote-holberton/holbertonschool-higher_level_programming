#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json
import os  # To clean up filesystem.

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")


os.remove("data.json")
print(f"\nClean effective? {not os.path.exists('data.json')}")

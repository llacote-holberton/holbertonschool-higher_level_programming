# Overview

This repository will hold exercises related to objects's serialization
  and use through different "exchange formats" such as csv and json.

# General Rules
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
  * Output must match expected formatting exactly.
  * No external libraries are allowed unless explicitly requested.
  * The length of your files will be tested using wc

# Exercises

| Task name                                            | Filename                        |
|------------------------------------------------------|---------------------------------|
| 0. Basic Serialization                               | task_00_basic_serialization.py  |
| 1. Pickling Custom Classes                           | task_01_pickle.py               |
| 2. Converting CSV Data to JSON Format                | task_02_csv.py                  |
| 3. Serializing and Deserializing with XML            | task_03_xml.py                  |

## Details - Task 00

<details>
  <summary>Basic Serialization</summary>

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.
### Instructions

Write a Python module named task_00_basic_serialization.py with the following functions:
```
def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
```

The function `serialize_and_save_to_file` take 2 parameters:
```
    data: A Python Dictionary with data
    filename: The filename of the output JSON file. If the output file already exists it should be replaced.
```

The function `load_and_deserialize` take 1 parameters:
```
    filename: The filename of the input JSON file This function returns a Python Dictionary with the deserialized JSON data from the file.
```

### Execution Output Example:

#### Code

```
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
```

#### Output
```
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

</details>


## Details - Task 01

<details>
  <summary>Pickling Custom Classes</summary>

</details>

## Details - Task 02

<details>
  <summary>Converting CSV Data to JSON Format</summary>

</details>

## Details - Task 03

<details>
  <summary>Serializing and Deserializing with XML</summary>

</details>

# Resources

The following are recommended resources and tools

## Documentation
- https://intranet.hbtn.io/concepts/1190
- https://intranet.hbtn.io/concepts/1191
- https://realpython.com/python-serialize-data/
- https://realpython.com/python-json/
- https://docs.python.org/3/library/pickle.html
- https://www.youtube.com/watch?v=2Tw39kZIbhs
- https://www.geeksforgeeks.org/python/convert-csv-to-json-using-python/
- https://www.datacamp.com/tutorial/python-xml-elementtree
- https://realpython.com/python-sockets/

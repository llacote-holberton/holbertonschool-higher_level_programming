#!/usr/bin/env python3
from task_01_pickle import CustomObject
import os  # To clean up filesystem.

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()

os.remove("object.pkl")
print(f"\nClean effective? {not os.path.exists('object.pkl')}")

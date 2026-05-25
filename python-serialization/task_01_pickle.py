#!/usr/bin/env python3
"""Basic Python dictionary to JSON string serialization module"""

import pickle   # To try and see the difference
import os       # To check file creation and clean up afterwards


class CustomObject():
    """Basic Data object representing a student's key infos"""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        self.__age = value

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, value: bool):
        self.__is_student = value

    def __init__(self, name: str, age: int, is_student: bool) -> None:
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def _presentation(self):
        return (
            f"Name: {self.name}\n"
            + f"Age: {str(self.age)}\n"
            + f"Is Student: {self.is_student}"
        )

    def display(self):
        print(self._presentation)

    def __str__(self):
        return self._presentation

    def serialize(self, filename):
        try:
            # MUST add mode 'b' (BINARY) as pickle serialization is BYTES ONLY
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
                return True
        except OSError as e:
            return False

    @classmethod
    def deserialize(cls, filename):
        try:
            # Same here: must precise 'r' for read AND 'b' for binary
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (OSError, pickle.PickleError) as e:
            # print(e)
            return None

    # IMPORTANT: If no implementation of that magic method, Python would just
    #   compare the memory addresses so a deserialized object could NEVER be
    #   considered the same as the "original one" even if nothing was changed.
    def __eq__(self, other):
        # First check is of same class (using dynamic name for best precision).
        if not isinstance(other, self.__class__):
            return False
        return (
            self.name == other.name
            and self.age == other.age
            and self.is_student == other.is_student
        )


if __name__ == "__main__":
    print("===== SELF-TEST: START =====")
    print("\n@dev: Step 0: Creating a test object")
    # @warning: Pycodestyle dislikes spaces in named parameter assignment
    testStudent = CustomObject(name="Laurent", age=42, is_student=True)
    print("\n@dev: Step 1a: testing __str__ magic method")
    print(testStudent)
    print("\n@dev: Step 1b: testing protected read-only attribute")
    print(testStudent._presentation)
    print("\n@dev: Step 1c: testing display")
    testStudent.display()

    print("Just for reference: Serialization error (PickleError)")

    def test():
        pass
    try:
        pickle.dumps(test)
    except Exception as e:
        print(e)

    print("\n@dev: Step 2a: trying deserialization of inexisting file")
    CustomObject.deserialize("absent_file")

    print("\n@dev: Step 2b: trying deserialization of corrupted data")
    CustomObject.deserialize(b"not a valid pickle")

    print("\n@dev: Step 3a: pickling my object to filesystem")
    test_file = "my_pickled_student.tmp"
    testStudent.serialize(test_file)
    print("\n@dev: Step 3b: checking file was created")
    print(f"File {test_file} exists? {os.path.exists(test_file)}")
    print("\n@dev: Step 3c: checking file content looks like pickle")
    with open(test_file, 'rb') as f:
        print(f.read())
    print("\n@dev: Step 4a: deserializing from filesystem")
    recreated = CustomObject.deserialize(test_file)
    print("\n@dev: Step 4b: checking values are the same")
    recreated.display()
    print(f"Original and created are the same? {testStudent == recreated}")

    print(f"\n@dev: Step 5: cleaning up filesystem (rm {test_file}")
    os.remove(test_file)
    print(f"@dev: file removed? {not os.path.exists(test_file)}")
    print("\n===== SELF-TEST: END =====")

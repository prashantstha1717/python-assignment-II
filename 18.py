# 18. Find a package in the Python standard library for dealing with JSON.
# Import the library module and inspect the attributes of the module.
# Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string. Deserialize the JSON back into Python.

import json
# help(json)

# Serializing
info = {
  "name": "Prashant",
  "age": 19
}
with open("info.json", "w") as write_file:
    json.dump(info, write_file)

# Deserializing
with open("info.json", "r") as read_file:
    result = json.load(read_file)
print(result)

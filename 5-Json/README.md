# Python built-in module JSON

## Convert from JSON to Python object (A Dictionary)
The Deserialization of JSON means the conversion of JSON objects into their respective Python objects
```
import json

# JSON string
emp = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(emp))

print("\nNow convert from JSON to Python")

# Convert string to Python dict
d = json.loads(emp)
print("Converted to Python", type(d))
print(d)

print(y["id"])

Output:

This is JSON <class 'str'>

Now convert from JSON to Python
Converted to Python <class 'dict'>
{'id': '09', 'name': 'Nitin', 'department': 'Finance'}
09
```

## Convert from Python object to JSON

```
import json

# JSON string
d = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(d))

print("\nNow Convert from Python to JSON i.e. Serialization (Convert to json)") 

# Convert Python dict to JSON
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj)

Output:
This is Python <class 'dict'>

Now Convert from Python to JSON
Converted to JSON <class 'str'>
{
    "id": "09",
    "name": "Nitin",
    "department": "Finance"
}
```

```
# This will produce a JSON formatted string with a comma separator between key-value pairs and a colon separator between keys and values:
json_data = json.dumps(data, separators=(",", ":"))

# Use the sort_keys parameter to specify if the result should be sorted:
json_data = json.dumps(data, sort_keys=True)

# This will produce a JSON formatted string with an indentation of 2 spaces for each level of nesting:
json_data = json.dumps(data, indent=2)

# serialize Python object and write to JSON file
python_obj = {'name': 'John', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(python_obj, file)

# read JSON file and parse contents
with open('data.json', 'r') as file:
    python_obj = json.load(file)
print(python_obj)  

# output: {'name': 'John', 'age': 30}
```

```
You can convert Python objects of the following types, into JSON strings and produce this equivalent json strings:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null

```

Helping guide:
1. https://www.w3schools.com/python/python_json.asp
2. https://www.datacamp.com/tutorial/json-data-python
3. https://www.geeksforgeeks.org/read-json-file-using-python/
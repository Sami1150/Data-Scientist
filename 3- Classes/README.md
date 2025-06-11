# Class

a_string = "Cool String"
an_int = 12

print(type(a_string))

```
prints "<class 'str'>"
```
```
print(type(an_int))
```
```
prints "<class 'int'>"
```

class CoolClass:
    pass

# Attribute Functions

```
class NoCustomAttributes:
pass

attributeless = NoCustomAttributes()

try:
attributeless.fake_attribute
except AttributeError:
print("This text gets printed!")

# prints "This text gets printed!"
```

```
hasattr(object, “attribute”) has two parameters:

1. object : the object we are testing to see if it has a certain attribute
2. attribute : name of attribute we want to see if it exists

```

```
getattr(object, “attribute”, default) has three parameters (one of which is optional):
1. object : the object whose attribute we want to evaluate
2. attribute : name of attribute we want to evaluate
3. default : the value that is returned if the attribute does not exist (note: this parameter is optional)
```

```
hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
```

# Everything in Python is Object:

fun_list = [10, "string", {'abc': True}]

type(fun_list)

```
Prints <class 'list'>

print(dir(fun_list))

# Prints ['**add**', '**class**', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Note: Functions are objects too

# STRING REPRESENTATION:

**__repr__**() is a method we can use to tell Python what we want the string representation of the class to be. **repr**() can only have one parameter, self, and must return a string.

```
class Employee():
def __init__(self, name):
self.name = name

def __repr__(self):
return self.name

argus = Employee("Argus Filch")
print(argus)

# prints "Argus Filch"
```

# INHERITANCE

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
Example:
Create a class named Student, which will inherit the properties and methods from the Person class:

```
class Student(Person):
pass
```
And if we define **init** function in Student class, then it overrides the **init**() method of the parent class.

Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

```
class Student(Person):
def **init**(self, fname, lname):
super().**init**(fname, lname)
```

By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Try Except

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

```
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```

# Raise an Exception
```
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```
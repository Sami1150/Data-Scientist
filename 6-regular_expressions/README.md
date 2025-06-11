# Regular Expressions 
 
```
import re

txt = "The rain in Spain"
x = re.search("rain", txt)

print("The first white-space character is located in position:", x)

Output:
# Span tells where is the match in `text`
The first white-space character is located in position: <re.Match object; span=(4, 8), match='rain'>

# re.search ( pattern , text)
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 

Output:
# Tells the start position
The first white-space character is located in position: 3
```

## Find All Occurences:

```
Define text and pattern

matches = re.finditer(pattern, text)
for match in matches:
    print(match)

# Get text (In loop)
print(text[match.span()[0]:match.span()[1]])

# Example 2 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

Output:
<re.Match object; span=(0, 17), match='The rain in Spain'>

```

## Split

```
# Split at each white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# ['The', 'rain', 'in', 'Spain']

# Split the string only at the first occurrence:


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# ['The', 'rain in Spain']

```

## Sub

```
# Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
```

## Find All

```
import re
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
regex = '\d+'

match = re.findall(regex, string)
print(match)

#Output: ['123456789', '987654321']

```

The Match object has properties and methods used to retrieve information about the search, and the result:

1. .span() returns a tuple containing the start-, and end positions of the match.
2. .string returns the string passed into the function
3. .group() returns the part of the string where there was a match

Helping guide:
1. regexr.com

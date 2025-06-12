# Dunder Methods

These are also called `Data Model` or `Magic Methods`

You can inspect any element and see what magic methods it implemented

```
from queue import Queue
import inspect

q = Queue
print(inspect.getSource(Queue))

#You can see all class defination 
# Not need to see in VS Code, hover and you can see!
```

You can write your own dunder methods:

```
from queue import Queue as q

class Queue(q): # Override
    def __repr__(self):
        print(f"Queue({self._qsize()})")
qu = Queue()

print(qu) # Will use our dunder method - repr
```

## Resources
https://docs.python.org/3/reference/datamodel.html


# Decorators

```
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time
        rv = func()
        total = time.time - start
        print("Total time taken", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(10000):
        pass

@timer
def test2():
    time.sleep(2)
    for _ in range(10000):
        pass

test()
test(2)

Output: 
Total time taken 0.015934
Total time taken 2.015934
```

## Resources:
https://www.youtube.com/playlist?list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP

# Generators:

## The problem:
It's common to get memory issue:

```
x = [i**2 for i in range(10000000000)]

for item in x:
    print(item)

# We get memory error

```
What we want to achieve is:
```
for i in range(1000000000):
    print(i**2)
```

The logic behind generators is:
 - Not to store entire sequence but see one value at a time
 - i.e. print squares for up to some number then we may get Memory error


```
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last**2
        self.last+=1
        return rv

g = Gen(10000000000)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
```

Now follow the generator pattern, the above and down function does the same thing but we are following different pattern to do this:

```
def Gen(n):
    for i in range(n):
        yield i**2

# return stops the execution, yield pauses the execution

g = Gen(100000000)

for i in g:
    print(i)

# Bcz of yield it gets output let's say 0, then wait for the second iteration then gives output 1 then again wait for third iteration etc.
# Other way instead of loop is:
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9 and so on

# At point where we reach last number and if we do call and so now there is no more yield / value so we get StopIteration error
```

Other way is:

```
squares = [print(x**2) for x in range(10000000000000)]
```

But it again consumes a lot of memory etc: 
See here:

```
import sys
def gen(n):
    for i in range(n):
        yield i**2

x = [i**2 for i in range(10000)]

y = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(y))

Output:
43816
64 # Generator pattern is more efficient
```



# Multiprocessing

Downloading file without multiprocessing is slow:

```
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
for i in range(10):
    downloadFile(url, i)
```

Use multiprocessing to speed up your downloading:

```
import multiprocessing
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"
pros = []
for i in range(50):
    downloadFile(url, i)
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()

# On network tab you would see a lot of threads with the name of `Python3`
```

Like threadPoolExecutor there is `ProcessPoolExecutor`

```
import concurrent.futures
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 
url = "https://picsum.photos/2000/3000"

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)
```

Another example of multiprocessing:
```
# create three functions that does some calculations

numbers_list = list(raneg(1000000))

p1 = multiprocessing.Process(target=func1, args = (numbers_list,))
p2 = multiprocessing.Process(target=func2, args = (numbers_list,))
p3 = multiprocessing.Process(target=func3, args = (numbers_list,))

print(end_time)

It will create three processes basically

It will print end_time first while calculations are still undergoing, so to aovid this we use join method.
Cuz we wawnt processes complete then we print the end_time

p1 = multiprocessing.Process(target=func1, args = (numbers_list,))
p2 = multiprocessing.Process(target=func2, args = (numbers_list,))
p3 = multiprocessing.Process(target=func3, args = (numbers_list,))


p1.join()
p2.join()
p3.join()
```

Other workaround is:

```

with concurrent.futures.ProcessPoolExecutor() as ececutor:
    f1 = executor.submit(func_name, _args)
    f2 = executor.submit(func_name, _args)
    f3 = executor.submit(func_name, _args)

    print(f1.result()) # Considering func_name will return sth
    print(f2.result())
    print(f3.result())

OR

with concurrent.futures.ProcessPoolExecutor() as ececutor:
    results = [executor.submit(func_name, args) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

```

# Threading

```
import threading

def square(numbers):
    print("Hi")
    for i in numbers:
        time.sleep(0.2)
        print(f"Square for number {i} is: {i**2}")
    print("Bye")

def cube(numbers):
    print("Hi")
    for i in numbers:
        time.sleep(0.2)
        print(f"Cube for number {i} is: {i**3}")
    print("Bye")

t = time.time()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t1 = threading.Thread(target = square, args = (l,))
t2 = threading.Thread(target = cube, args = (l,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in", time.time() - t)
```


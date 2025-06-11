# Assignment 1
## Python Mini-Project: Barebones "Read-Only" HTTP Server

### 1. Create Virtual Environment

```
python -m venv myfirstproject

source myfirstproject/bin/activate
```

### 2. Run script

1. Open script `server.ipynb`
2. Run the first cell to install dependencies and run server
3. You will get the output:

    ```
    [*] Server running on http://127.0.0.1:8000
    ```

### 3. Test the Server

#### 🖥️ Using a Web Browser

You can test the server by visiting the following URLs:

| Description                      | URL                                      | Expected Response                          |
|----------------------------------|------------------------------------------|--------------------------------------------|
| ✅ Get all items                 | [http://localhost:8000/items](http://localhost:8000/items)       | Returns a JSON array of all items          |
| 🔍 Get item with ID `3`         | [http://localhost:8000/items/3](http://localhost:8000/items/3)   | Returns the item with ID `3` (JSON)        |
| ❌ Get non-existing item (ID 4) | [http://localhost:8000/items/4](http://localhost:8000/items/4)   | Returns `404 Not Found` with error message |
| 🚫 Invalid path                 | [http://localhost:8000/invalid](http://localhost:8000/invalid)   | Returns `404 Not Found` with error message |



#### 🧪 Using `curl` (Command Line)

You can also test the server using `curl` from the command line:

```bash
# ✅ Get all items
curl http://localhost:8000/items

# 🔍 Get item with ID 3
curl http://localhost:8000/items/3

# ❌ Get non-existing item (e.g., ID 4)
curl http://localhost:8000/items/4

# 🚫 Invalid path
curl http://localhost:8000/invalid

# 🚫 Unsupported method (e.g., POST instead of GET)
curl -X POST http://localhost:8000/items

```

#### 4. Close the server
You can close the server by running the second cell on server script `server.ipynb`
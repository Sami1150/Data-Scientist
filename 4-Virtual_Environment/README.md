# Create Virtual Environment

You may use two cmds after you are in a folder where you want to create virtual environment (Use cd {directory}):

```
python -m venv myfirstproject

source myfirstproject/bin/activate
```

<i> If you see any Permission denied exception use </i>

```
chmod +x project_1/bin/activate
```

## Run code in Virtual environment

1. Create a test.py file, anywhere, preferred in the directory where environment is created
2. Install dependency `pip install cowsay`
3. Save this code in that file

```
import cowsay

cowsay.cow("Good Mooooorning!")
```

4. Run file in Virtual environment

```
python test.py
```

5. You must see this output on console

```
  _________________
| Good Mooooorning! |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||

```

Close the environment:
```
deactivate
```

Delete the environment:
```
rm -rf myfirstproject
```

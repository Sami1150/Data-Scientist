How to create virtual env?

You can use pipenv:
Install pipenv: pip install --user pipenv
- Note: You might see warnings to setup PATH variables

```bash
To Initialize use:
pipenv --three 
# or if you want the latest version of python3.x then do this:
pipenv --python 3.6

To install cmds:
pipenv install numpy==1.15.2

To use custom env:
Use cmd: pipenv shell

To exit: exit() or CTRL + D


We see Pipfile that contains the imports summary that we can use

Pipfile.lock is a file that contains metadata and details of our imports and that our env can support
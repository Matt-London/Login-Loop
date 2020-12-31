# Login-Loop
A program that submits a form with randomly generated emails and passwords.


## Setup
Run the following in order to install the required Python modules:

```bash
pip3 install --user -r requirements.txt
```

Change the values on lines 10 through 15, if applicable.
For example:

```python
loginURL = "example.com"
useDelay = True
formID = "test"
firstTerm = "email"
secondTerm = "pass"
emailExt = ["example.com"]
```

Breaking down each term:
Set this to the url of the website:

```python
loginURL = ""
```

Set this to True or False depending on if you want to use the random delay function:

```python
useDelay = True
```

Set this to the form ID on the webpage:

```python
formID = "test"
```

Set this to the first term in the form that will be supplied as email addresses:

```python
firstTerm = "email"
```

And the same for the second term which will supply passwords:

```python
secondTerm = "pass"
```

Use the following to give all domain names that will be randomly assigned to generated email addresses:

```python
emailExt = ["example.com"]
```


## Executing/Usage

Run the following to launch the program:

```bash
python3 loginLoop.py
```
or
```bash
./loginLoop.py
```

Since all arguments are supplied within the code, there is no need for command-line arguments


## Contributing
If you would like to contribute, you may make a pull request. It will be helpful if you first open an issue describing the change that you are interested in contributing.


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Disclaimer
<b>This is strictly for educational purposes and should not be deployed against any forms with which the user does not have permission to test. I disclaim any and all responsibility for the actions of the users of this program.<b>

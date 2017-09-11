#Python Script to remove white spaces

## Description
As a developer, many times we may run into trouble due to whitespaces. Leading whitespaces are easier to identify, but trailing whitespaces can get you in huge trouble. Consider below example of *cfg* file:

```
property1=value1 
property2 = value2
```

From above cfg file, we can clearly identify leading whitespace in *property2* definition. But above file has trailing whitespace after *value1*.

This script comes in rescue for such unusual faults.

##Getting Started

* consider directory **/etc/config** having all the config files having all the config files, create a new file: **script.py** in config directory, and paste below code snippet
```python
import os
from os import path

separator = '='
current_file = __file__ # get path of current working directory

files = filter(path.isfile, os.listdir(os.getcwd())) # get all files in current directory, os.getcwd() can be replaced with custom path ie: /etc/config

for file in files:
    # skip script files for updation
    if not file.endswith('.py'):
        print 'updating file: ' + file
        file_object = open(file, "r+") # get file object
        lines = file_object.readlines()
        file_object.seek(0)
        file_object.truncate()
        for line in lines:
            tokens = [x.strip() for x in line.split(separator)] # separate line by '=' and strip white spaces for each token
            line = separator.join(tokens)
            file_object.write(line+'\n')
        print "file updated\n",
    else:
        print 'skipped: ' + file,


```
* run
`script.py`

* script will execute and remove all leading and trailing whitespaces for all lines separated by **=** (equals)

## Demo

* checkout project and jump to checkout directory ie:
`cd <PATH_TO_CHECKOUT_DIRECTORY>`
* Before executing script, verify the config files in **test-config** directory. Both files has leading and trailing whitespaces seperated by **=**
* jump to config directory consisting of script ie: `cd config-test`
* run `script.py`
* executing above command will remove all the white spaces, and you will get the desired output

##Questions ??

Reach out to author @ [Tarang Bhalodia - LinkedIn](https://www.linkedin.com/in/tarang-bhalodia-48870494/)
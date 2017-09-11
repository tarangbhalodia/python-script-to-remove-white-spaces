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

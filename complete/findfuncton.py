# find count_divisors

import re
import os

def find_function(filename, function_name):
    f = open(filename, "r")
    #lines = list()
    for line in f:
        if function_name in line:
            print function_name + " in " + filename
            break
        else:
            continue

def create_filenames():
    filenames = list()
    files = os.listdir(".")
    files = [x for x in files if re.match(r".*\.py", x)]
    files = [x for x in files if re.match(r"^problem", x)]
    return files

def main():
    filenames = create_filenames()
    function_name = "str_reverse"
    for filename in filenames:
        print filename
        find_function(filename, function_name)


if __name__ == '__main__':
    main()

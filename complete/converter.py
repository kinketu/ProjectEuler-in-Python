# convert "ProjectEuler" into "projecteuler" in a script

import os
import re

def sub(filename):
    f = open(filename, "r")
    lines = list()
    for line in f:
        if "ProjectEuler" in line:
            line = line.replace("ProjectEuler", "projecteuler")
            #print line
        lines.append(line)
    f.close()

    new_file = open(filename, "w")
    new_file.writelines(lines)
    new_file.close()

def create_filenames():
    filenames = list()
    files = os.listdir(".")
    #print files
    files = [x for x in files if re.match(r".*\.py", x) and "run" not in x]
    files = [x for x in files if "problem" in x]
    #print files
    #print len(files)
    return files

def main1():
    for i in range(11, 51):
        filename = "problem" + str(i) + ".py"
        sub(filename)

def main2():
    filenames = create_filenames()    
    for filename in filenames:
        sub(filename)
    
    print "Done"

if __name__ == '__main__':
    main2()

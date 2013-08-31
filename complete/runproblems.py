# Run Project Euler's problems

import os
import sys
import re

def create_filenames1(end, start=1):
    lst = list()
    string = "problem"
    for i in range(start, end):
        lst.append(string+str(i)+".py")
    return lst

def create_filenames2():
    filenames = list()
    files = os.listdir(".")
    #print files
    files = [x for x in files if re.match(r".*\.py", x) and "run" not in x]
    files = [x for x in files if "problem" in x]
    #print files
    #print len(files)
    return files

def test1():
    print "problem1"
    os.system("pypy problem1.py")
    print "problem2"
    os.system("pypy problem2.py")

def test2():
    sys.stdout = open("log.txt", "a")
    filenames = create_filenames(6)
    #print filenames
    for i in range(len(filenames)):
        print "problem" + str(i+1)
        os.system("pypy "+filenames[i])
        print "\n"

def main1():
    start = 1
    end = 51
    filenames = create_filenames1(end, start)
    for i in range(len(filenames)):
        print "\nproblem " + str(i+start)
        os.system("pypy "+filenames[i])

def main2():
    filenames = create_filenames2()
    for filename in filenames:
        print filename
        os.system("pypy "+filename)


if __name__ == '__main__':
    main1()

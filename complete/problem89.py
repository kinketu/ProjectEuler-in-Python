# Project Euler problem 89

#from roman import fromRoman as frr
#from roman import toRoman as tor
from projecteuler import time_func

def subtractive(roman):
    result = roman
    replacements = [
        ("VIIII", "IX"),
        ("IIII", "IV"),
        ("LXXXX", "XC"),
        ("XXXX", "XL"),
        ("DCCCC", "CM"),
        ("CCCC", "CD"),
        ]
    for old, new in replacements:
        result = result.replace(old, new)
    return result

def main():
    f = open('problem89.txt', 'r')
    lines = []
    for line in f:
        lines.append(line[:-1])
    f.close()
    #print lines

    current = 0
    improved = 0
    for line in lines:
        current += len(line)
        improved += len(subtractive(line))
    print current - improved


if __name__ == '__main__':
    time_func(main)

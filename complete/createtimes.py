# create "times.txt"


def create_list():
    f = open("time.txt", "r")
    lines = list()
    for line in f:
        lines.append(line[:-1])
    while "" in lines:
        lines.remove("")
    lines = lines[:150]
    return lines

def main():
    f = open("calctimes.txt", "w")
    lines = create_list()
    for i in range(len(lines)):
        if i % 3 == 2:
            f.write(lines[i]+"\n")
        else:
            f.write(lines[i]+",")
    f.close()
            

if __name__ == '__main__':
    main()

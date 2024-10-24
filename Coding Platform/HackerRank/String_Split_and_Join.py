def split_and_join(line):
    # write your code here
    new = ""
    for i in line:
        if(i == " "):
            new += "-"
        else:
            new += i
    return new

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
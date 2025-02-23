import textwrap

def wrap(string, max_width):
    new = ""
    Loop = 0
    for i in range(int(len(string)/max_width)):
        new += string[i*max_width : i*max_width+max_width]
        new += "\n"
        Loop += max_width
    if(Loop != len(string)):
        new += string[Loop:]
    return new

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
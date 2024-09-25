def mutate_string(string, position, character):
    new = string[0:position]
    new += character
    new += string[position+1:]
    
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
def count_substring(string, sub_string):
    string = list(string)
    count = 0
    while(sub_string[0] in string):
        index = string.index(sub_string[0])
        check = ""
        if(index+len(sub_string) <= len(string)):
            for i in range(index,index+len(sub_string)):
                check += string[i]
        if(check == sub_string):
            count += 1
       
        string.pop(index)
        
    return(count)
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
def TwoSum(array,Target):
    for i in range(len(array)):
        Find = Target - array[i]
        if(Find in array[i+1:]):
            return([i,array.index(Find,i+1)])
        else:
            continue


print(TwoSum([2, 7, 11, 15], 9))
print(TwoSum([3, 2, 4], 6))
print(TwoSum([3, 3], 6))
print(TwoSum([1, 2, 3, 4], 7))
print(TwoSum([-1, -2, -3, -4], -7))
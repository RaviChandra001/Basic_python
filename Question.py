# Finding a maximum even number from a list

def highest(value):
    #making a another list name even
    even = []
    for item in value:
        if item%2 == 0:
            even.append(item)
    
    return max(even)


result = highest([10,12,14,2,11,3,7,8,20])
print("Highest maximum is : ", result)
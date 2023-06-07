# Exercise
picture = [
    [1,1,1,1,1,1,1],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [1,1,1,1,1,1,1]
]

for image in picture:
    for img in image:
        if(img == 1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

"""
output -->  

*******
  ***  
  ***  
  ***  
  ***  
*******

"""

# Another image generating 
picture = [
    [1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1],
    [0,0,1,1,1,1,1],
    [0,0,0,1,1,1,1],
    [0,0,0,0,1,1,1],
    [0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1]
]

for image in picture:
    for img in image:
        if(img == 1):
            print("*",end="")
        else:
            print("",end="")
    print()

"""
Output -->

*******
*******
******
*****
****
***
**
*

"""
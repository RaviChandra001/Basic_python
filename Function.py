picture = [
    [1,1,1,1,1,1,1],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [1,1,1,1,1,1,1]
]

def show():
    for image in picture:
        for img in image:
            if(img == 1):
                print("*",end="")
            else:
                print(" ",end="")
        print()

show()
show()



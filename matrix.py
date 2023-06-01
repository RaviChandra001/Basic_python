# Matrix is a collection of rows and columns and we can say that it is a multi - dimensional array . Which means array insdie the array 

# syntax --> matrix_name = [[ ]]

matrix1 = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

print(matrix1[0][1])  # 1
print(matrix1[0][0])  # 1
print(matrix1[1][1])  # 1

print(matrix1)

matrix2=[
    [1,1,1],
    [1,1,1],
    [1,1,1],
]

print(matrix2)

# addition of matrix1 and 2 
matrix3 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# addition using itreative approach
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    
print("Resultant matrix is : ",matrix3)

matrix_size = int(input("Enter size of matrix: "))
matrix = []
for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        row.append(int(input("Enter elements of matrix: ")))
    matrix.append(row)
for i in range(matrix_size):
    for j in range(matrix_size-i-1,-1,-1):
        k = matrix[i][i]
        matrix[i][i] = matrix[i][j]
        matrix[i][j] = k
        break
print(matrix)

        

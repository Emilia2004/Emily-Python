size = int(input("Enter size of the matrix: "))
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(input("Enter elements of the matrix: ")))
    matrix.append(row)
transposed = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        transposed[size-i-1][size-j-1] = matrix[i][j]
print(transposed)
        

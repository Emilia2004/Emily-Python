size = int(input("Enter the size of the matrix: "))
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(input("Enter elements of matrix: ")))
    matrix.append(row)
k = 0
transposed = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        transposed[j][i] = matrix[i][j]
print(transposed)

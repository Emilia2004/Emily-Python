size = int(input("Enter size of matrix: "))
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(input("Enter elements of matrix: ")))
    matrix.append(row)
sum = 0
for i in range(size):
    for j in range(size):
        if i == j:
            sum += matrix[i][j]
print(sum)

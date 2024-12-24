size = int(input("Enter size of the matrix: "))
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(input("Enter elements of the matrix: ")))
    matrix.append(row)
for i in range(size):
    sum = 0
    for j in range(size):
        sum += matrix[i][j]
    print(f"The sum of the elements of {i} row is {sum}")

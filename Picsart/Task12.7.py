row_count = int(input("Enter count of rows: "))
column_count = int(input("Enter count of columns: "))
matrix = []
for i in range(row_count):
    row = []
    for j in range(column_count):
        row.append(int(input("Enter elements of matrix: ")))
    matrix.append(row)
sum = 0
for i in range(row_count):
    for j in range(column_count):
        sum += matrix[i][j]
print(sum)

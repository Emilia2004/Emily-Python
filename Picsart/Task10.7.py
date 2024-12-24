word = input()
arr = []
for i in word:
    arr.append(i)
for i in range(len(arr)):
    if arr[i] == "a":
        arr[i] = "x"
for i in arr:
    print(i, end = "")

word = "radar"
arr = []
for i in range(len(word)-1,-1,-1):
    arr.append(word[i])
for i in range(len(arr)):
    if arr[i] != word[i]:
        print("No")
        break
else:
    print("Yes")

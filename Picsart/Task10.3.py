sentence = "hello world. are you ready?"
arr = []
for i in sentence:
    arr.append(i)
for i in range(len(arr)):
    x = 0
    if arr[i] == " ":
        x = ord(arr[i+1])-32
        arr[i+1] = chr(x)
x = ord(arr[0])-32
arr[0] = chr(x)
for i in arr:
    print(i,end = "")

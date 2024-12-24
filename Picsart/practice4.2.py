arr1 = [14,15,32,66]
arr2 = [14,15,32,66,55]
st1 = set(arr1)
st2 = set(arr2)
if len(st1) < len(st2):
    print(st2 - st1)
else:
    print(st1 - st2)

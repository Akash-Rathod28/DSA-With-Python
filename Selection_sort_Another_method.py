arr = [10,40,30,60,50]
arr1 = []
while True:
    b = min(arr)
    n = arr.index(b)
    arr1.append(b)
    arr.pop(n)
    if len(arr) == 0:
        
        break
print(arr1)

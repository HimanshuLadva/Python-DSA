arr1 = [1,2,3]
arr2 = [1,2,'hello']
arr3 = [1,2,3]

for a,b,c in zip(arr1, arr2, arr3):
    print(f"a = {a} b = {b} c = {c}")
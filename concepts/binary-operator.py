# << operator
a = 1
n = 1
while a < 100:
    print(f"before a = {a} in bin = {bin(a)}")
    a <<= n # a * (2 ** n)
    print(f"after a = {a} in bin = {bin(a)}")

print("-----------------------------------------")
b = 128
n = 1
count = 0
while count < 10:
    print(f"before b = {b} in bin = {bin(b)}")
    b >>= 1 # b // (2 ** n)
    print(f"after b = {b} in bin = {bin(b)}")
    count += 1
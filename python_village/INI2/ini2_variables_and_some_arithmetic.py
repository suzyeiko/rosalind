
with open("rosalind_ini2.txt") as f:
    lines = f.read()
numbers = lines.split()
a = int(numbers[0])
b = int(numbers[1])
h = a**2 + b**2
print(h)

f.close()

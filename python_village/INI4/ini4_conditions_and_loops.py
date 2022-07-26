with open("rosalind_ini4.txt") as f:
    text=f.read()
numbers = text.split()
a = int(numbers[0])
b = int(numbers[1])+1

n = 0
for i in range(a, b):
    if i%2 == 1:
        n = n + i
    else:
        continue
print(n)

f.close()

with open("rosalind_ini3.txt") as f:
    lines = [x.strip() for x in f.readlines()]
text = lines[0]
numbers= lines[1].split()
ini1 = int(numbers[0])
fin1 = int(numbers[1])+1
ini2 = int(numbers[2])
fin2 = int(numbers[3])+1

word1 = text[ini1:fin1]
word2 = text[ini2:fin2]
result = word1 + " " + word2
print(result)
f.close()

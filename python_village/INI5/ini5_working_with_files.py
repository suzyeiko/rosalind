final = ""
with open("rosalind_ini5.txt") as f:
    text = f.readlines()
    
    for l in range(len(text)):
        if l%2 == 1:
            final = final + text[l]
    print(final)
f.close()

with open("rosalind_ini6.txt") as f:
    text = f.read()
    words = text.split()
    d = {}
    for word in words:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word] = 1
    for key, value in d.items():
        print key, value

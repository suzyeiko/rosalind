# Import file
#with open("sample_dataset.txt") as f:
with open("rosalind_revc.txt") as f:

    dna = f.read() #read file
    dna = dna.rstrip() #remove newlines
    dna = dna.upper() #convert to uppercase

    # Reverse string
    rev = dna[::-1]
    
    # Get the complement of each nucleotide
    revc = ""
    for nt in rev:
        if nt == "T":
            revc += "A"
        elif nt == "A":
            revc += "T"
        elif nt == "C":
            revc += "G"
        elif nt == "G":
            revc += "C"
        else:
            revc += nt

    print(revc)

f.close()

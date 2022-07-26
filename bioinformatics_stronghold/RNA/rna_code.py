# Import file
#with open("sample_dataset.txt") as f:
with open("rosalind_rna.txt") as f:
    dna = f.read() #read file
    dna = dna.upper() #convert to uppercase
    rna = ""
    for nt in dna:
        if nt == "T": #if a nucleotide is "T", change to "U"
            rna += "U"
        else: #if a nucleotide is NOT "T", keep it
            rna += nt
    print rna
f.close()

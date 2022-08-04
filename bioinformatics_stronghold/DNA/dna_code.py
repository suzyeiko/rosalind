# Import file
#with open("sample_dataset.txt") as f:
with open("rosalind_dna.txt") as f:
    dna = f.read() #read file
    dna = dna.upper() #convert to uppercase
    counts = {}
    for nt in dna:
        if nt in counts: #if a nucleotide was already counted, sum + 1 to the current value
            counts[nt]=counts[nt]+1
        else: #if a nucleotide was still not counted, add to a dictionary with value of 1
            counts[nt]=1
    print(counts["A"], counts["C"], counts["G"], counts["T"])
f.close()

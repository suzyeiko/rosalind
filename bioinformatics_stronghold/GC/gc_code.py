#Import fasta file
#arquivo = "sample_dataset.fna"
arquivo = "rosalind_gc.txt"
with open(arquivo) as f:
    headers = []
    seqs = []
    for line in f: # Read each line
        if line.startswith(">"): # Line starting with ">" is a fasta header
            ID = line.replace(">","").strip()
            headers.append(ID) # Append header to a list
            seqs.append("") # Append an empty string to the sequence list
        else:
            nts = line.strip()
            if len(nts) > 0: # If last string is empty, add the sequence to the last item on the list
                seqs[-1] = seqs[-1] + nts

# Count GC content in a string
def count_gc(seq):
    GC = 0
    for nt in seq:
        if nt == "G":
            GC = GC + 1
        elif nt == "C":
            GC = GC + 1
        else:
            continue
    GCcontent = round(GC*100.0000/len(seq), 6)
    return GCcontent


# Count GC content for each sequence
highGC = 0
highheader = ""
for x in range(len(seqs)):
    gc_cont = count_gc(seqs[x])
    #print headers[x]
    #print gc_cont
    
    # Get the sequence with the highest GC content
    if highGC < gc_cont:
        highGC = gc_cont
        highheader = headers[x]
    else:
        continue

print(highheader)
print(highGC)

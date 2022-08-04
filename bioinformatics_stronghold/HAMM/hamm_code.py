# Import input data
#arquivo="sample_dataset.txt"
arquivo="rosalind_hamm.txt"

with open(arquivo) as f:
    seqs=f.readlines()
    seqA=seqs[0].rstrip()
    seqB=seqs[1].rstrip()

# Count number of point mutations
def count_point_mutations(seqA, seqB):
    hamming=0
    for i in range(len(seqA)):
        #print(seqA[i], seqB[i])
        if seqA[i] != seqB[i]: #compare nucleotides between both sequences. If it is different, add 1 to Hamming distance.
            hamming+=1
        else:
            continue
    return hamming

result = count_point_mutations(seqA, seqB)
print(result)


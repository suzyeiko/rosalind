#Import fasta file
#arquivo = "sample_dataset.fna"
arquivo = "rosalind_cons.txt"
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

def get_consensus_profile(list_of_seqs):
    seqA = []
    seqC = []
    seqG = []
    seqT = []

    position = 0
    
    while position < len(list_of_seqs[0]):
        
        A = 0
        C = 0
        G = 0
        T = 0
        for seq in list_of_seqs:
            if seq[position] == 'A':
                A = A + 1
            elif seq[position] == 'C':
                C = C + 1
            elif seq[position] == 'G':
                G = G + 1
            elif seq[position] == 'T':
                T = T + 1
        seqA.append(A)
        seqC.append(C)
        seqG.append(G)
        seqT.append(T)
        position = position + 1

    #print(seqA)
    #print(seqC)
    #print(seqG)
    #print(seqT)
    
    profile = {"A":seqA, "C":seqC, "G":seqG, "T":seqT}
    
    consensus = ""
    
    for n in range(len(seqA)):
        nt = [profile["A"][n], profile["C"][n], profile["G"][n], profile["T"][n]]
        #print(nt)
        maximum = nt[0]
        index = 0
        for i in range(1,len(nt)):
            if nt[i] > maximum:
                maximum = nt[i]
                index = i
        if index == 0:
            consensus = consensus + "A"
        elif index == 1:
            consensus = consensus + "C"
        elif index == 2:
            consensus = consensus + "G"
        elif index == 3:
            consensus = consensus + "T"

    return consensus, profile

output = get_consensus_profile(seqs)

print (output[0])
profile = output[1]

print("A:", ' '.join(str(x) for x in profile["A"]))
print("C:", ' '.join(str(x) for x in profile["C"]))
print("G:", ' '.join(str(x) for x in profile["G"]))
print("T:", ' '.join(str(x) for x in profile["T"]))




#Import fasta file
#arquivo = "sample_dataset.fna"
arquivo = "rosalind_grph.txt"

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

def get_adjacency_list(list_of_headers, list_of_seqs):
    adj_list = []
    # Compare each pair of sequences
    for n1, seq1 in enumerate(list_of_seqs):
        for n2, seq2 in enumerate(list_of_seqs):
            if list_of_headers[n1] == list_of_headers[n2]: 
                #print(list_of_headers[n1], list_of_headers[n2])
                continue
            elif seq1[-3:] == seq2[:3]:
                adj_list.append( list_of_headers[n1]+" "+list_of_headers[n2] )
                #print(list_of_headers[n1], seq1)
                #print(list_of_headers[n2], seq2)
                #print()
            
    return adj_list

output = get_adjacency_list(headers, seqs)

print(*output ,sep='\n')

f.close()

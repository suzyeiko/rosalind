#Import fasta file
#arquivo = "sample_dataset.fna"
arquivo = "rosalind_prot.txt"

# Get mRNA codon table
#with open("rna_codon_table.txt") as f:
#    codons=f.read()
#    codons=codons.rstrip()
#    codons=codons.split()
#    codon_dict={}
#    for i in range(len(codons)):
#        if i%2==0:
#            codon_dict[codons[i]]=codons[i+1]
#        else:
#            continue
    #print(codon_dict)
codon_dict={'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'ACU': 'T', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': 'Stop', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'UGA': 'Stop', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGA': 'R', 'GCU': 'A', 'UAG': 'Stop', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

# Import file
with open(arquivo) as f:
    seq = f.read()

### Function for converting RNA to protein sequence ###
def convert_rna_to_prot(seq):
    found_start_codon = False
    prot_seq=""
    
    #Identify starting codon position and extract sequence
    for i in range(len(seq)):
        if seq[i:i+3]=="AUG" and found_start_codon == False:
            temp_seq = seq[i:]
            temp_seq = temp_seq.rstrip()
            found_start_codon = True
        else:
            break

    #Work with sequence from starting codon
    codons = [temp_seq[i:i+3] for i in range(0, len(temp_seq), 3)]
    for codon in codons:
        if codon_dict[codon] == 'Stop':
            break
        else:
            prot_seq = prot_seq + codon_dict[codon]
    return prot_seq

result = convert_rna_to_prot(seq)
print result


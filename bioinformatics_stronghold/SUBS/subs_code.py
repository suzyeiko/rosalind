import re

#Import fasta file
#arquivo = "sample_dataset.txt"
arquivo = "rosalind_subs.txt"
with open(arquivo) as f:
    text = f.readlines()
    string = text[0].rstrip() #remove break line
    sub = text[1].rstrip() #remove break line
    #print(sub)
    #print(string)
    index = []
    
    #Loop for different frames of a string considering the substring length
    for i in range(len(string)):
        frame = string[i:]
        # Find all index positions of the substring in the current frame using regular expression
        index_pos = [m.start() for m in re.finditer(sub, frame)]
        # Verify if the each index position was already added to the list. If not, add it.
        for j in index_pos:
            if i+j+1 not in index:
                index.append(i+j+1)
    #Sort index numbers from lower to higher.
    index.sort()

    #print items from the list separated by space " "
    print(*index)



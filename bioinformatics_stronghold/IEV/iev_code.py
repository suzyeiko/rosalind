#Import file
#arquivo="sample_dataset.txt"
arquivo="rosalind_iev.txt"

with open(arquivo) as f:
    numbers = f.read()
    numbers = numbers.split(" ")
    AA_AA = int(numbers[0]) # Get number of months
    AA_Aa = int(numbers[1]) # Get how many months the rabbits live for
    AA_aa = int(numbers[2])
    Aa_Aa = int(numbers[3])
    Aa_aa = int(numbers[4])
    aa_aa = int(numbers[5])

def get_offspring_dom(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa):
    AA_AA_os = AA_AA * 2
    AA_Aa_os = AA_Aa * 2
    AA_aa_os = AA_aa * 2
    Aa_Aa_os = Aa_Aa * 1.5
    Aa_aa_os = Aa_aa * 1
    #aa_aa_os = aa_aa * 0
    
    offspring = AA_AA_os + AA_Aa_os + AA_aa_os + Aa_Aa_os + Aa_aa_os #+ aa_aa_os

    return offspring

offspring = get_offspring_dom(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa)
print(offspring)

f.close()


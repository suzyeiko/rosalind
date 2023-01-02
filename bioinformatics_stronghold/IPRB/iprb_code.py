#Import fasta file
#arquivo = "sample_dataset.txt"
arquivo = "rosalind_iprb.txt"

# Import file
with open(arquivo) as f:
    numbers = f.read()
    numbers = numbers.rstrip()
    pop = numbers.split(" ")
    #print(pop)
    AA = int(pop[0])
    Aa = int(pop[1])
    aa = int(pop[2])

    #print(AA, Aa, aa)

def get_prob_dominant(AA, Aa, aa):
    total = AA+Aa+aa

    # Example: AA = 2, Aa = 2, aa = 2
    #X is AA = 2/6  Y is AA = 1/5   (2/6)(1/5) = 1/15
    #               Y is Aa = 2/5   (2/6)(2/5) = 2/15
    #               Y is aa = 2/5   (2/6)(2/5) = 2/15
    
    
    #X is Aa = 2/6  Y is AA = 2/5   2/15
    #               Y is Aa = 1/5   1/15
    #               Y is aa = 2/5   2/15
    
    
    #X is aa = 2/6  Y is AA = 2/5   2/15
    #               Y is Aa = 2/5   2/15
    #               Y is aa = 1/5   1/15
    
    #AA x __ = 4/4 * 5/15 = 5/15
    #Aa x AA = 4/4 * 2/15 = 2/15
    #Aa x Aa = 3/4 * 1/15 = 3/60 = 1/20
    #Aa x aa = 1/2 * 2/15 = 2/30 = 1/15
    #aa x AA = 4/4 * 2/15 = 2/15
    #aa x Aa = 1/2 * 2/15 = 2/30 = 1/15
    
    # 5/15 + 2/15 + 1/20 + 1/15 + 2/15 + 1/15 = 11/15 + 1/20 = 0.78333
    
    # Probability of selecting two mating organisms
    AAxAA = AA/total * (AA-1)/(total-1)
    AAxAa = AA/total * (Aa)/(total-1)
    AAxaa = AA/total * (aa)/(total-1)

    AaxAA = Aa/total * (AA)/(total-1)
    AaxAa = Aa/total * (Aa-1)/(total-1)
    Aaxaa = Aa/total * (aa)/(total-1)

    aaxAA = aa/total * (AA)/(total-1)
    aaxAa = aa/total * (Aa)/(total-1)
    aaxaa = aa/total * (aa-1)/(total-1)
    
    # Probability of producing an individual possessing a dominant allele for each combination of mating organisms
    dom_AAxNN = AAxAA + AAxAa + AAxaa
    dom_AaxAA = 1 * AaxAA
    dom_AaxAa = 0.75 * AaxAa
    dom_Aaxaa = 0.5 * Aaxaa
    dom_aaxAA = 1 * aaxAA
    dom_aaxAa = 0.5 * aaxAa

    result = dom_AAxNN + dom_AaxAA + dom_AaxAa + dom_Aaxaa + dom_aaxAA + dom_aaxAa
    
    return result
    
output = get_prob_dominant(AA, Aa, aa)
print(round(output, 5))

f.close()

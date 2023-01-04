#Import file
#arquivo="sample_dataset.txt"
arquivo="rosalind_fibd.txt"

with open(arquivo) as f:
    numbers = f.read()
    numbers = numbers.split(" ")
    n = int(numbers[0]) # Get number of months
    m = int(numbers[1]) # Get how many months the rabbits live for

def get_mortal_fibonacci_rabbits(n, m):
    rabbits = []
    for month in range(n):
        if month == 0: # On first month, number of pairs of rabbits is one
            rabbits = [1]
        elif month == 1: # On second month, number of pairs of rabbits is still one
            rabbits.append(1)
        elif month < m:
            newrabbits = rabbits[month-1] + rabbits[month-2]
            rabbits.append(newrabbits)
        else:
            # Current litter of rabbit pairs equals the sum of the rabbit pairs from the last m months to the second last month )
            #print("month:", month, rabbits(-m:-1])
            newrabbits = sum(rabbits[-m:-1])
            rabbits.append(newrabbits)
    return rabbits

rabbits = get_mortal_fibonacci_rabbits(n,m)
print(rabbits[-1])

f.close()


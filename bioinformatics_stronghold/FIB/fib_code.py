#Import file
#arquivo="sample_dataset.txt"
arquivo="rosalind_fib.txt"
with open(arquivo) as f:
    numbers = f.read()
    numbers = numbers.split(" ")
    n = int(numbers[0]) # Get number of months
    k = int(numbers[1]) # Get how many k rabbit pairs are produced by every pair of reproduction-age rabbits

    rabbits = []
    for month in range(n):
        if month == 0: # On first month, number of rabbits is one
            rabbits = [1]
        elif month == 1: # On second month, number of rabbits is still one
            rabbits.append(1)
        else:
            # Current litter of rabbit pairs equals the sum of the rabbit pairs in the last month + (k * rabbit pairs in the second last month)
            newrabbits = rabbits[month-1] + rabbits[month-2]*k
            rabbits.append(newrabbits)
    print(rabbits[-1])
f.close()


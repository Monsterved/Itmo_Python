from random import randint
# First part
part1 = [randint(1, 100) for i in range(100)]
part2 = part1.copy()
for i in range(len(part2)):
    if part2[i] > 50:
        part2[i] = "HIGH"
    else:
        part2[i] = "LOW"

print(part2)


# Second part
def pages(): 
    import re, pages, numpy as np 
 
    Part1 = [] 
    Part2 = [] 
    NamesAll = np.array([''.join(pages.get_first_name()) for _ in range(elemuntCount)]) 
 
    for name in firstNames: 
        if (str(name)[0] == "A"  or str(name)[0] == "M"): 
            Part1.append(name) 
 
        else : 
            Part2.append(name) 
 
    print("Names:", Part1, Part2, sep="\n")

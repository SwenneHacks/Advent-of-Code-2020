

day_one = open("input.txt", "r") #mode r=read w=write r+=read+write
array = day_one.readlines()
target = 2020
clean = []

#array has newlines attached to the numbers so I can't summ them.
#print(array)

for x in array:
    val=x.strip()
    clean.append(int(val))

#now managed to clear the white spaces and newlines and cast int (200 elements)
#print(clean)
#print(len(clean))

def brute_force(clean, target):
    for i in range(len(clean)-1):
        for j in range(i + 1, len(clean)-1):
            for z in range (j + 1, len(clean)-1):
                if clean[i] + clean[j] + clean[z] == target:
                    print(clean[i] * clean[j] * clean[z])
                    return True
    return False

print(brute_force(clean, target))

day_one.close()
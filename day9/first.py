# day1

from itertools import combinations

#          i  j           z  
test = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

text = open("input.txt", "r") #mode r=read w=write r+=read+write
array = text.readlines()

numbers = []

#array has newlines attached to the numbers so I can't summ them.
#print(array)

for x in array:
    val=x.strip()
    numbers.append(int(val))

#now managed to clear the white spaces and newlines and cast int.
#print(numbers)
#print(len(numbers))

tmp = []
tmp = test[0: 5]
for i in combinations(tmp, 2):
    print(sum(i))
print(tmp)

def xmas(test):
    z = 5
    s = 0
    for i in range(len(test) - 1):
        for j in range(i + 1, z):
            s += 1
            # print(test[i] , test[j], test[z], s)
            if test[i] + test[j] == test[z]:
                # print(test[i], test[j], test[z], "<<<<<<<")
                z += 1
                s = 0
                tmp = test[z - 5: z]
                combinations(tmp, 2)
                # print(tmp)

    return (False, test[z])

print(xmas(test))

text.close()
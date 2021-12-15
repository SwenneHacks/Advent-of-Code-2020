
fileName = "input.txt";

result = open(fileName, "r") #mode r=read w=write r+=read+write
instructions = open(fileName, "r").read().split("\n")
array = result.readlines()
counter = 0

#array has newlines attached to the numbers so I can't summ them.
#print(array)

clean = []
for x in array:
    val=x.strip()
    clean.append(val)
#now managed to clear the white spaces and newlines
# print(clean)
# print(len(clean))

done = [False] * len(clean)
sample = []
values = []
tmp = []

binary = []

for x in array:
    val=x.strip()
    values.append(int(val))

# for i in range(len(clean) - 1):
#     nbr = clean[i]
#     bits = bits.append(nbr)
#     one = bits.count(1)
#     zero = bits.count(0)
# print(one, zero)

def xmas(clean, counter):

    a = 0
    for j in range(len(instructions)):
        bits = 0
        for i in range(len(instructions)):
            go = instructions[i]
            if go[a][0:1] == '1':
                bits += 1
            # print(go[a][0:1], bits)
        i = 0
        tada = len(values) / 2
        # print(tada)
        if tada < bits:
            tmp.append(1)
        else:
            tmp.append(0)
        print('x')
        a += 1
        print(tmp)
    return(True)
    

print(xmas(clean, counter))



result.close()
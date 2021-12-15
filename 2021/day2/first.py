
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
numbers = []
commands = []

#first values:

def xmas(clean, counter):
    
    for i in range(len(clean) - 1):
        data = clean[i].split(' ')
        cmd = data[0]
        nbr = data[1]
        commands == commands.append(cmd[0:2])
        values == values.append(nbr)
        # print(nbr, cmd[0:2])
        # print(values[i], commands[i])
    
    up = commands.count('up')
    fo = commands.count('fo')
    do = commands.count('do')
    print(up, fo, do)

    depth = 0
    horiz = 0
    for i in range(len(instructions) - 1):
        go = instructions[i]
        val = int(values[i])
        if go[0:2] == "up":
            depth -= val
        if go[0:2] == "do":
            depth += val
        if go[0:2] == "fo":
            horiz += val
        print(depth, horiz, go)
    print(depth, horiz)
    result = depth * horiz
    print(result)
print(xmas(clean, counter))

result.close()
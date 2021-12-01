# day8

result = open("input.txt", "r") #mode r=read w=write r+=read+write
instructions = open("input.txt", "r").read().split("\n")
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

nop = 0
values = []
numbers = []
commands = []
def weird_game(clean, counter):
    
    i = 0
    acc = 0
    done = [False] * len(clean)
    while i < len(instructions):
        if done[i] == True:
            break
        done[i] = True
        call = instructions[i]
        if call[0:3] == "nop":
            i += 1
            continue
        elif call[0:3] == "acc":
            acc += int(call[4:])
        elif call[0:3] == "jmp":
            i += int(call[4:]) - 1
        i += 1
    print(acc)

    for i in range(len(clean) - 1):
        data = clean[i].split(' ')
        cmd = data[0]
        nbr = data[1]
        commands == commands.append(cmd)
        values == values.append(nbr)

    #print(commands)
    
    for plus in values:
        val=plus.strip("+")
        numbers.append(int(val))
    # print(numbers)

    nop = commands.count('nop')
    print(nop)
    

print(weird_game(clean, counter))

result.close()
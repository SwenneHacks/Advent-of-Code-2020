# day8

result = open("input.txt", "r") #mode r=read w=write r+=read+write
array = result.readlines()
counter = 5

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

    # for n in range(len(commands) - 1):
    #     if commands[n] == "nop":
    #         nop == nop + 1
    nop = commands.count('nop')
    print(nop)

print(weird_game(clean, counter))

result.close()
 # day8
result = open("input.txt", "r").read().split("\n")

def weird_game(result):

    i = 0
    acc = 0
    done = [False] * len(result)
    while i < len(result):
        if done[i] == True:
            return([False, acc])
        done[i] = True
        call = result[i]
        if call[0:3] == "nop":
            i += 1
            continue
        elif call[0:3] == "acc":
            acc += int(call[4:])
        elif call[0:3] == "jmp":
            i += int(call[4:]) - 1
        i += 1
    return([True, acc])

# res = weird_game(result)
# if res[0] == True:
#         print(res[1])
#         quit()
# for i in range(len(result) -1, 0, -1):
#     tmp = []
#     tmp += result
#     if result[i][:3] == "jmp":
#         tmp[i] = tmp[i].replace("jmp", "nop")
#     elif result[i][:3] == "nop":
#         tmp[i] = tmp[i].replace("nop", "jmp")
#     else:
#         continue
#     res = weird_game(tmp)
#     if res[0] == True:
#         print(res[1])
#         quit()

print(weird_game(result))
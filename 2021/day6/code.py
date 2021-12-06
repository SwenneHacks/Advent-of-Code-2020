fish = open("day6.txt").readlines()
for i in range(len(fish)):
    fish = [int(x) for x in fish[i].split(',')]

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for something in fish:
    arr[int(something)] += 1

for j in range(256):
    tmp = arr[0]
    arr[0] = 0
    for i in range(8):
        arr[i] = int(arr[i + 1])
        arr[i + 1] = 0
    arr[6] += int(tmp)
    arr[8] += int(tmp)
tmp = 0
for nbr in arr:
    tmp += int(nbr)
print(tmp)

### PART ONE

# print(fish)
# # new = [[0 for x in range(len[fish])] for y1 in range(len(fish))]
# for j in range(256):
#     for i in range(len(fish)):
#         if fish[i] == 0:
#             fish[i] = 7
#             fish.append(8)
#         fish[i] -= 1
#     print(fish)
# print(len(fish))



# day1
# As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. 
# On a small screen, the sonar sweep report (your puzzle input) appears: 
# each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

#For example, suppose you had the following report:
# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
#200 (decreased)
#207 (increased)
#240 (increased)
#269 (increased)
#260 (decreased)
#263 (increased)
#In this example, there are 7 measurements that are larger than the previous measurement.
#How many measurements are larger than the previous measurement?


day_one = open("/Users/sofferha/Codam/Side-Projects/Advent-of-Code-2021/day1/input.txt", "r") #mode r=read w=write r+=read+write
array = day_one.readlines()

#array has newlines attached to the numbers so I can't summ them.
#print(array)

num = []
for x in array:
    val=x.strip()
    num.append(int(val))

#                    i  j             
test = [35,20,15,25,47,40,62,55,65,95,20,10,55,90]

tmp = []
# tmp = test[0: 5]
# for i in combinations(tmp, 2):
    # print(sum(i))
# print(tmp)


def xmas(num):
    v = 0
    print(len(num))
    for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                print(i, num[i], num[i + 1], "<<<<<<<")
                v += 1
            else: print(i, num[i] , num[i + 1])
    if (num[0] > num[1]):
        return (False, v)
    else:
        print(num[0], num[1])
        return (True, v - 1)


print(xmas(num))

day_one.close()
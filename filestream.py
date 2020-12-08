day_one = open("py.txt", "r") #mode r=read w=write r+=read+write

#this one returns true/false (but only r mode)
#       print(day_one.readable())

#this one reads all lines (now printing it)
#       print(day_one.read())

#this one reads the first line the continues when you repeat it
#       print(day_one.readline())
#       print(day_one.readline())

#this one puts all lines in a array, with \n, separated by commas
#       print(day_one.readlines())

#this one returns the 3rd element of the array
#        print(day_one.readlines()[3])

#now using a loop to print each element (one by one) casted to int
#       for number in day_one.readlines():
#           print(int(number))

array = day_one.readlines() # array of char* (strings)

day_one.close()
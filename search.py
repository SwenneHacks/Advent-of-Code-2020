A = [13248,1324123,4132,34523,5245,2,3,3,2354,5,433,423,23,5,54,2,23,23,423,4,2345,467,78,89,98797,8,9,75,1,646,234]
n = 7

def brute_force(A, n):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)-1):
            if A[i] + A[j] == n:
                print(A[i], A[j])
                return True
    return False

print(brute_force(A, n))










# pos = -1

# def search(list, n):
#     i = 0
#     j = 0

#     while 1 < len(list):
#         if list[i] + list[j] == n:
#             globals()['pos'] = i
#         i = i+1
#         j = j+1
#     print(i,"+",j,"=7")


# if search(list,n):
#     print("Found at ", pos+1)
# else:
#     print("Not Found")
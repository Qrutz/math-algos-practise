# # goal is to find the longest subarray and print the len of that subarray

# import numpy as np
# arr = np.array([1, 2, 2, 3, 1, 2])
# inpt = arr.tolist()

# # get ze subarrays


# def pickingNumbers(a):
#     base = []
#     subarray = [base]
#     for i in range(len(a)):
#         new = a[i]
#         orig = subarray[:]
#         for j in range(len(subarray)):

#             subarray[j] = subarray[j] + [new]
#         subarray = orig + subarray
#     return subarray

# # get the longest ones lengt
# # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# def findLongest(x):

#     # if len of x[i] > len of x[i+1] , answer = x[i]
#     n = 0
#     highest = 0

#     for i in range(n, len(x)-1):
#         print(len(x[i+1]), len(x[i]))
#         if len(x[i]) > highest:
#             highest = len(x[i])
#             print(highest, " this the high")
#             if highest > 0 and len(x[i+1]) > highest:
#                 highest = len(x[i+1])
#                 return highest
#     #     if len(x[i+1]) > highest:
#     #         highest = len(x[i+1])
#     #         print("swapped vars", highest)
#     # return highest
#     # highest == len(x[i+1])

#     # highest = len(x[i+1])
#     # return highest
#     # emptyarr.insert(len[x+1])
#     # return emptyarrS
#     # print(len(x[i+1]), len(x[i]))

#     # if len(x[i+1]) > len(x[i]):

#     # for j in range(n+1, len(x)):
#     #     print(x[j], "666")

#     #  if len(x[j]) >= len(x[i]):
#     #      print(len(x[j]))
#     #      print(len(x[j]), len(x[i]))


# y = pickingNumbers([1, 2, 3])
# abba = y[3]


# print(findLongest(y))

# arr1 = [3, 7, 2, 1]
# arr2 = [6, 3, 4, 7]


# def mergeSorted(a=arr1, a2=arr2):
#     merged = []
#     for i in range(len(a)):
#         merged.append(a[i])
#     for j in range(len(a2)):
#         merged.append(a2[j])

#     return sorted(merged)


# print(mergeSorted())


# Average word length
#  sum(len(word)) / amount of words

sentence1 = "Greetings summoners how you doing today sir, do u want to buy some fish"
sentence2 = "Hoppie hooeee foooor soooore r w a s gadgsadf gasdf"


def averageWords(s=sentence1):
    x = s.split()
    len_of_x = len(x)
    print(len(s)/len(x))


print(averageWords())

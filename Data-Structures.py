# Arrays
# def reverseArray(a):
#     copy = a.copy()
#     copy.reverse()
#     return copy


# inpt = ["1", "2", "3", "4"]
# inpt2 = [3, 2, 3, 4]

# print(reverseArray(inpt))
# print(reverseArray(inpt2))

# Doing it the hard way-


arr = [1, 2, 3, 4, 5]
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i]),
print("Array in reverse order: ")
# Loop through the array in reverse order
for i in range(len(arr)-1, -1, -1):
    print(arr[i])


for i in range(5, -1, -1):
    print(i)

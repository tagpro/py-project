'''
INSERTION SORT NAIVE PROGRAM

This program does the following things
1. Takes the length of the array that needs to be sorted in asscending order from the console
2. Accepts the elements of the array in a linear fashion
3. Sorts the array using Insertion Sort Algorithm
'''

arr_length = int(raw_input('Insert the number of Elements in array'))
arr = []
for i in range(0, arr_length):
    print i+1, ' -> ',
    arr.append(int(raw_input()))
print (arr)
for i in range(1, arr_length):
    k = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > k:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = k
print (arr)
# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")


def bubbleSort(arr):
  for compare in range(len(arr) - 1, 0, -1):
    for i in range(compare):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]

def selectionSort(arr, x):
  for i in range(x):
    minimumIndex = i
    for minimumValue in range(i+1, x):
      if arr[minimumValue] < arr[minimumIndex]:
        minimumIndex = minimumValue
    (arr[i], arr[minimumIndex]) = (arr[minimumIndex], arr[i])

def insertionSort(arr):
  for i in range(1, len(arr)):
    value_to_sort = arr[i]
    currentValue = i-1
    while currentValue >= 0 and arr[currentValue] > value_to_sort:
      arr[currentValue+1] = arr[currentValue]
      currentValue -= 1
    arr[currentValue+1] = value_to_sort
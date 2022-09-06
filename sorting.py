###sorting###
import random
import time

length = input("What length list do want to test: ")
lis = [0]*int(length)
for i in range (0,len(lis)-1):
    lis[i] = random.randint(0, 1000)
bubble = lis[:]
insertion = lis[:]

print(lis)

#bubble sort:
bubbleS = time.clock()
flag = True
while flag == True:
    flag = False
    for i in range (0, len(bubble)-1):
        if bubble[i] > bubble[i+1]:
            hold = bubble[i]
            bubble[i] = bubble[i+1]
            bubble[i+1] = hold
            flag = True
bubbleE = time.clock()
print("Bubble sort done in " + str(bubbleE - bubbleS))
print(bubble)

#insertion sort:
insertionS = time.clock()
for j in range (1, len(insertion)):
    while j > 0 and insertion[j] < insertion[j-1]:
        hold = insertion[j]
        insertion[j] = insertion[j-1]
        insertion[j-1] = hold
        j = j - 1
insertionE = time.clock()
print("In insertion sort done in " + str(insertionE - insertionS))
print(insertion)

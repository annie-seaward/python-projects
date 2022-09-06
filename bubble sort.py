#Bubble Sort
val = 5
flag = True
list = [78, 384, 3985, 374, 44, 24, 432, 2398, 23, 2535, 5]
while flag == True:
   flag = False
   for i in range (0, len(list)-1):
      if list[i] > list[i+1]:
         hold = list[i]
         list[i] = list[i+1]
         list[i+1] = hold
         flag = True

print (list)

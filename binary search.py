#binary search
val = 100
list = [3, 7, 15, 19, 67, 89, 96, 97, 98, 106, 139, 167, 249, 589, 1000]
found = False
low = 0
high = len(list) - 1
while found == False and low != high:
   mid = (low + high)//2
   print(mid)
   print(list[mid])
   if list[mid] == val:
      found = True
   elif list[mid] < val:
      low = mid + 1
   elif list[mid] > val:
      high = mid - 1

if found == True:
   print("item found")
else:
   print("item not in list")

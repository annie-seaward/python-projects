#Insertion Sort
list = [95, 5348, 54983, 38, 4949, 444, 4945, 24, 3459, 248, 345, 54309, 2, 459, 0]
for i in range (1, len(list)):
   while i > 0 and list[i] < list[i-1]:
      hold = list[i]
      list[i] = list[i-1]
      list[i-1] = hold
      i = i - 1
print(list)

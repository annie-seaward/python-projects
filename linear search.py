###linear search efficency checker###
import random
lisLen = 0     #stores how long the list is in each iteration
lisLenRec = []    #stores the list length to a list for output to the csv file
averLen = []      #stores the average number checks to find the x
REPEATS = 10000   #constant to control the number of repeats for each list length

while lisLen < 10000:
   lisLen = lisLen + 1000     #increases list length at each iteration
   lis = ["o"]*lisLen
   lis[random.randint(0,len(lis)-1)] = "x"      #puts in a random x
   total = 0         #stores the total number checks across all repeats for the averages
   for j in range(0,REPEATS):
      for i in range(0,len(lis)-1):
         if lis[i] == "x":
            total = total + i
   lisLenRec.append(lisLen)      #appends the lists with data about length and checks
   averLen.append(total/REPEATS)

csvFile = open("linearSearch.csv", 'w+')  #opens/creates a csv file
for numb in lisLenRec:
   csvFile.write(str(numb)+",")     #writes the list length
csvFile.write("\n")
for numb in averLen:
   csvFile.write(str(numb)+",")     #writes the average number of checks
csvFile.close()

print("results saved to file")      #lets the user know the program is finished
   
            

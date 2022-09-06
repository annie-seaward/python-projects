#STACK SIMULATOR

def push():
   global pointer
   pointer=pointer+1
   if pointer == 5:
      print("Stack Overflow")
      pointer = pointer-1
   else:
      choice=input("What would you like to push")
      stack[pointer-1]=choice
      printStack()

def pop():
   global pointer
   if pointer < 0:
      print("Stack Empty")
   else:
      pointer=pointer-1
      printStack()

def printStack():
   for i in range (0,5):
      if i<=pointer:
         print(stack[i])
         

stack=[""]*6
pointer=0
choice=""
while choice != "end":
   choice=input("Would you like push, pop or end")
   if choice == "push":
      push()
   elif choice == "pop":
      pop()
   elif choice == "end":
      printStack()
      print("END")
   else:
      print("try again")
         

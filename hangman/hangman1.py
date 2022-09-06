#=================Random Import and Global Variables=================#

import random
global guessedLetters
global attempts
global randNum
global clueGiven

#=================Hangman ASCII=================#

Hangman=["\n  _________\n    |    ||\n    0    ||\n   _|_   ||\n    |    ||\n   / \   ||\n         ||\n============","\n  _________\n    |    ||\n    0    ||\n   _|_   ||\n    |    ||\n   /     ||\n         ||\n============","\n  _________\n    |    ||\n    0    ||\n   _|_   ||\n    |    ||\n         ||\n         ||\n============","\n  _________\n    |    ||\n    0    ||\n   _|_   ||\n         ||\n         ||\n         ||\n============","\n  _________\n    |    ||\n    0    ||\n   _|    ||\n         ||\n         ||\n         ||\n============","\n  _________\n    |    ||\n    0    ||\n    |    ||\n         ||\n         ||\n         ||\n============","\n  _________\n    |    ||\n    0    ||\n         ||\n         ||\n         ||\n         ||\n============","\n _________\n    |    ||\n         ||\n         ||\n         ||\n         ||\n         ||\n============","\n  _________\n         ||\n         ||\n         ||\n         ||\n         ||\n         ||\n============","\n         ||\n         ||\n         ||\n         ||\n         ||\n         ||\n============","\n============"]

#=================sub-routines=================#

#prints the contents of guessWord to the screen
def guessWord_print():
    for letter in guessWord:
        print (letter+" ", end='')

#returns the contents of guessWord as s string
def guessWord_string():
    string=""
    for letter in guessWord:
        string=string+letter
    return string

#randomly selects a word from wordsFile
def word_select():
    global randNum
    words=[]                                                #creates a list to hold all the words in the dictionary file
    for line in wordsFile:
        line=line[:len(line)-1]
        words.append(line)
    randNum = random.randint(0,len(words)-1)         #generate random number, for random word and matching clue
    word=words[randNum]              #selects word
    return word

def clue_select():
    global randNum
    clues=[]
    for line in cluesFile:
        line=line[:len(line)-1]
        clues.append(line)
    clue=clues[randNum]
    return clue

#checks if the user has found the word
def word_found(word):
    guess=guessWord_string()        #calls sub-routine to create a string of guessWord
    if guess==word:
        return True
    else:
        return False

#checks that the users guess is a valid guess
def guess_check(guess):
    global guessedLetters
    while True:
        if len(guess) != 1:                 #checks only one letter is entered
            guess=input("Sorry, there's something wrong with your guess, try again: ")
        elif guess in guessedLetters:       #checks the letter hasn't been guessed before
            guess=input("Sorry, there's something wrong with your guess, try again: ")
        elif guess not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":     #checks the input is really a letter
            guess=input("Sorry, there's something wrong with your guess, try again: ")
        else:
            return guess

#takes the users guess and checks if it is right or wrong
def main_sequence(word,lives):
    global attempts
    global guessedLetters
    global clueGiven
    if word_found(word)== True:
        return "True"
    elif lives==0:
        return "False"
    else:
        print("\n")
        guessWord_print()                           #calls the sub-routine to print guessWord 
        print("\nSo far you have guessed: "+guessedLetters)     #print guessed letters

        if clueGiven==False:
            guess=input("Take a guess (or ask for a clue...but you'll lose two lives): ")               #lets user input a guess
            if guess == "Clue" or guess == "clue":
                clue=clue_select()
                print("\n\nYour clue is...\n'"+clue+"'")
                lives=lives-2
                print(Hangman[lives])
                print("You have "+str(lives)+" remaining")
                clueGiven=True
                return""+main_sequence(word,lives)
        if clueGiven==True:
           guess=input("Take a guess: ")
                       
        guess=guess_check(guess)                #calls the sub-routine to check the guess is valid

        attempts = attempts+1                   #counts the attempt
        count = -1                              #Initialises count to know the letter position
        correct = False                         #Initialises the boolean variable
        guessedLetters=guessedLetters+guess+" "     #records the guess
        
        for letter in word:         #checks if guess is correct
            count = count + 1
            if letter == guess:
                   guessWord[count]=guess
                   correct = True

        if correct==True:               #outputs to the user that the guess is correct
                print("\nYay! That's in the word!")
        else:                           #outputs to th user that the guess is wrong
                lives=lives-1     #loses a life
                print(Hangman[lives])
                print("Oh No! Sorry you lose a life")
                print("You have "+str(lives)+" remaining")
    return ""+main_sequence(word,lives)

#=================MAIN=================#

print("WELCOME TO HANGMAN!!!")
print(Hangman[0])
play=True
clueGiven=False

while play==True:
   guessedLetters=""
   attempts=0
   clueGiven=False
   level=(input("Choose a level: Easy, Medium or Hard: "))         #User enters a level

   check=False         #used as a boolean check
   while check==False:
       if level == "Easy" or level == "easy":          #checks what the user has typed
           level=3
           wordsFile = open('easy.txt', 'rt')          #opens the correct dictionary
           cluesFile = open('easy_clue.txt', 'rt')
           check=True
       elif level == "Medium" or level == "medium":
           level=5
           wordsFile = open('medium.txt', 'rt')
           cluesFile = open('medium_clue.txt', 'rt')
           check=True
       elif level == "Hard" or level == "hard":
           level=7
           wordsFile = open ('hard.txt', 'rt')
           cluesFile = open('hard_clue.txt', 'rt')
           check=True
       else:
           level=(input ("Please check your spelling\nChoose a level: Easy, Medium or Hard: "))    #loops if the user enters doesn't enter a correct level

   print("Your word is "+str(level)+" letters long")       #prints the length of the word depending on the level selected
   print("You have 15 lives to get the word...\nGood Luck")
   guessWord=["_"]*level
   word=word_select()

   lives=11

   success=main_sequence(word,lives)
   if success=="True":
       print("\nCONGRATULATIONS AND CELEBRATIONS...\nYou've found the word!\nAnd in only "+str(attempts)+" attempts\nAnd As you know the word was "+word)
   
   elif success=="False":
       print("Sorry you've lost!\nThe word you failed to guess was "+word+"\nIn even "+str(attempts)+" atttempts")

   restart=(input("Enter any key to restart or 'Q' to exit"))
   if restart == "Q" or restart == "q":
      play=False

print("END")

    
    

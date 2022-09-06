def createCard():
   from random import shuffle
   class Card(object):
       def __init__(self, name=None, age=0, power=0, wisdom=0, awesomeness=0):
           self.name = name
           self.age = age
           self.power = power
           self.wisdom = wisdom
           self.awesomeness = awesomeness
   harrypotter = Card('Harry Potter', 18, 89, 64, 47)
   lunalovegood = Card('Luna Lovegood', 17, 74, 84, 85)
   remuslupin = Card('Remus Lupin', 38, 77, 86, 83)
   voldemort = Card('Voldemort', 71, 88, 69, 72)
   albusdumbledore = Card('Albus Dumbledore', 115, 95, 96, 98)
   fredweasley = Card('Fred Weasley', 20, 69, 72, 89)
   deck = [harrypotter,lunalovegood,remuslupin,voldemort,albusdumbledore,fredweasley]
   shuffle(deck)
   i = True
   for card in deck:
      if i == True:
         playerLis.append(card)
         i = False
      else:
         compLis.append(card)
         i = True

def playerMove():
   print("\nYou have " + str(len(playerLis)) + " cards\nYour current card is " + playerLis[0].name)
   print("Age: " + str(playerLis[0].age) + "\nPower: " + str(playerLis[0].power))
   print("Wisdom: " + str(playerLis[0].wisdom) + "\nAwesomeness: " + str(playerLis[0].awesomeness))
   i = False
   while i == False:
      attribute = (input("Choice the attribute you'd like to play: ")).lower()
      if attribute == "age":
         print("\nYou play age at " + str(playerLis[0].age))
         print("The computer's card is " + compLis[0].name + " with an age of " + str(compLis[0].age))
         i = True
         compare(playerLis[0].age, compLis[0].age, compLis[0].name)
      elif attribute == "power":
         print("\nYou play power at " + str(playerLis[0].power))
         print("The computer's card is " + compLis[0].name + " with an power of " + str(compLis[0].power))
         i = True
         compare(playerLis[0].power, compLis[0].power, compLis[0].name)
      elif attribute == "wisdom":
         print("\nYou play wisdom at " + str(playerLis[0].wisdom))
         print("The computer's card is " + compLis[0].name + " with an wisdom of " + str(compLis[0].wisdom))
         i = True
         compare(playerLis[0].wisdom, compLis[0].wisdom, compLis[0].name)    
      elif attribute == "awesomeness":
         print("\nYou play awesomeness at " + str(playerLis[0].awesomeness))
         print("The computer's card is " + compLis[0].name + " with an awesomeness of " + str(compLis[0].awesomeness))
         i = True
         compare(playerLis[0].awesomeness, compLis[0].awesomeness, compLis[0].name)
   compMove()

def compMove():
   print("\nThe computer's card is " + compLis[0].name)
   age = (compLis[0].age - averageLis[0])/averageLis[0]
   power = (compLis[0].power - averageLis[1])/averageLis[1]
   wisdom = (compLis[0].wisdom - averageLis[2])/averageLis[2]
   awesomeness = (compLis[0].awesomeness - averageLis[3])/averageLis[3]
   maximum = max(age, power, wisdom, awesomeness)
   if maximum == age:
      print("The computer plays age at " + str(compLis[0].age))
      print("You're card is " + playerLis[0].name + " with an age of " + str(playerLis[0].age))
      compare(playerLis[0].age, compLis[0].age, compLis[0].name)
   elif maximum == power:
      print("The computer plays power at " + str(compLis[0].power))
      print("You're card is " + playerLis[0].name + " with an power of " + str(playerLis[0].power))
      compare(playerLis[0].power, compLis[0].power, compLis[0].name)
   elif maximum == wisdom:
      print("The computer plays wisdom at " + str(compLis[0].wisdom))
      print("You're card is " + playerLis[0].name + " with an wisdom of " + str(playerLis[0].wisdom))
      compare(playerLis[0].wisdom, compLis[0].wisdom, compLis[0].name)
   elif maximum == awesomeness:
      print("The computer plays awesomeness at " + str(compLis[0].awesomeness))
      print("You're card is " + playerLis[0].name + " with an awesomeness of " + str(playerLis[0].awesomeness))
      compare(playerLis[0].awesomeness, compLis[0].awesomeness, compLis[0].name)
   playerMove()
   
def compare(player, comp, compName):
   if player > comp:
      print("You win the card")
      playerLis.append(compLis[0])
      playerLis.append(playerLis[0])
      del compLis[0]
      del playerLis[0]
      victory()
      average(False)
   elif player < comp:
      print("The computer wins the card")
      compLis.append(playerLis[0])
      compLis.append(compLis[0])
      del playerLis[0]
      del compLis[0]
      victory()
      average(True)

def average(lose):
   averageLis[0] = (averageLis[0] + compLis[0].age)/2
   averageLis[1] = (averageLis[1] + compLis[0].power)/2
   averageLis[2] = (averageLis[2] + compLis[0].wisdom)/2
   averageLis[3] = (averageLis[3] + compLis[0].awesomeness)/2
   if lose == True:
      averageLis[0] = (averageLis[0] + playerLis[0].age)/2
      averageLis[1] = (averageLis[1] + playerLis[0].power)/2
      averageLis[2] = (averageLis[2] + playerLis[0].wisdom)/2
      averageLis[3] = (averageLis[3] + playerLis[0].awesomeness)/2

def victory():
   import sys
   if len(compLis) == 0:
      print("\nThat was the computers last card... YOU WIN!!!")
      sys.exit()
   elif len(playerLis) == 0:
      print("\nThat was your last card... Sorry, you lose :(")
      sys.exit()

playerLis = []
compLis = []
print("Welcome to Harry Potter top trumps!")
createCard()
averageLis = [0]*4
averageLis[0] = compLis[0].age
averageLis[1] = compLis[0].power
averageLis[2] = compLis[0].wisdom
averageLis[3] = compLis[0].awesomeness
playerMove()

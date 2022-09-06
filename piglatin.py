
def vowelCheck(word):
      vowels = ("AEIOUaeiou")
      if word[0] in vowels:
         return True
      else:
         return False

def punctuationCheck(word):
   if word[len(word)-1].isalpha() == False:
      return True
   else:
      return False

def apstropheCheck(word,punctuation):
   if punctuation == True:
      if word[(len(word)-3):] == "'s":
         return True
   elif punctuation == False:
      if word[(len(word)-2)] == "'s":
         return True
   else:
         return False

def capitalCheck(word):
   if word[0].isupper() == True:
      return True
   else:
      return False

def pigLatin(file):
   latin = ""
   english=""
   for word in file.read().split():
      english = english + word
      vowel=vowelCheck(word)
      punctuation=punctuationCheck(word)
      apstrophe=apstropheCheck(word,punctuation)
      capital=capitalCheck(word)
      if vowel == False and punctuation == False and apstrophe == False and capital == False:
         latin = latin + word[1:] + word[0] + "ay "
      elif vowel == True:
         if apstrophe == False and punctuation == False:
            latin = latin + word + "way "
         elif apstrophe == False and punctuation == True:
            latin = latin + word[:(len(word)-2)] + "way" + word[len(word)-1] + " "
         elif apstrophe == True and punctuation == False:
            latin = latin + word[:(len(word)-3)] + "way" + word[(len(word)-2):] + " "
         elif apstrophe == True and punctuation == True:
            latin = latin + word[:(len(word)-4)] + "way" + word[(len(word)-3):] + " "
      elif vowel == False and punctuation == True:
         if capital == True:
            word[0].lower()
            word[1].upper()
         if apstrophe == False:
               latin = latin + word[1:(len(word)-2)] + word[0] + "ay" + word[len(word)-1] + " "
         elif apstrophe == True:
               latin = latin + word[1:(len(word)-4)] + word[0] + "ay" + word[(len(word)-3):] + " "
      elif vowel == False and punctuation == False and apstrophe == True:
         if capital == True:
            word[0].lower()
            word[1].upper()
         latin = latin + word[1:(len(word)-3)] + word[0] + "ay" + word[(len(word)-2):] + " "
      elif vowel == False and punctuation == False and apstrophe == False and capital == True:
         word[0].lower()
         word[1].upper()
         latin = latin + word[1:] + word[0] + "ay "
   print (latin)

#====MAIN====#
print("WELCOME")
myFile = open("english.txt","rt")
pigLatin(myFile)

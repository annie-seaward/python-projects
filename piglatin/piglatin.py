#===SUB ROUTINES==#

def vowelCheck(word):       #checks if the first letter is a vowel by comparing if it is in a string of vowels
      vowels = ("AEIOUaeiou")
      if word[0] in vowels:
         return True
      else:
         return False

def punctuationCheck(word):     #checks if the last letter isn't in the alphabet and therefore punctuation
   if word[len(word)-1].isalpha() == False:
      return True
   else:
      return False

def apstropheCheck(word):       #checks if the word has a 's at the end, taking account for punctuation
    if "'s" in word:
        return True
    else:
        return False

def capitalCheck(word):     #checks if the first letter is capital, using .isupper
   if word[0].isupper() == True:
      return True
   else:
      return False

#MAIN TRANSLATOR
def pigLatin(file):
   latin = ""       #sets the translation to nothing
   for word in file.read().split():       #goes through each word in the file
      vowel=vowelCheck(word)        #checks any values for exception translations
      punctuation=punctuationCheck(word)
      apstrophe=apstropheCheck(word)
      capital=capitalCheck(word)
      if vowel == False and punctuation == False and apstrophe == False:
          word = word[1:] + word[0] + "ay "     #standard translation

      elif vowel == True:
         if apstrophe == False and punctuation == False:    #other translation combinations
            word = word + "way "
         elif apstrophe == False and punctuation == True:
            word = word[:(len(word)-1)] + "way" + word[len(word)-1] + " "
         elif apstrophe == True and punctuation == False:
            word = word[:(len(word)-2)] + "way" + word[(len(word)-2):] + " "
         elif apstrophe == True and punctuation == True:
            word = word[:(len(word)-3)] + "way" + word[(len(word)-3):] + " "

      elif vowel == False and punctuation == True:
         if apstrophe == False:
               word = word[1:(len(word)-1)] + word[0] + "ay" + word[len(word)-1] + " "
         elif apstrophe == True:
               word = word[1:(len(word)-3)] + word[0] + "ay" + word[(len(word)-3):] + " "

      elif vowel == False and punctuation == False and apstrophe == True:
         word = word[1:(len(word)-2)] + word[0] + "ay" + word[(len(word)-2):] + " "

      if capital == True:     #re-capitalizes if apporiate
         word = word.capitalize()

      latin += word     #adds the word to the overall translation
   print (latin)

#====MAIN====#
print("WELCOME")
file = open("english.txt","rt")
pigLatin(file)

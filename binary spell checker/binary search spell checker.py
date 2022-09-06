###binary search spell checker###
def binSearch(word, dic):   #binary search
    low = 0
    high = len(dic)-1
    while low <= high:          
        mid = (low + high)//2   #finds midpoint
        item = dic[mid]
        if word == item:
            return True
        elif word < item:
            high = mid - 1      
        else:                  
            low = mid + 1       
    return False

with open("dictionary.txt") as file:
    dictionary = file.read().splitlines()   #splits dictionary words into a list
    dictionary.sort()

html = open("binarySearch.html", "w+")  #creats the html file
html.write('<html><head><title>Spell Checker</title></head><body><p>')  #inputs title and opening tags

text = input("Enter a sentence to spell check: ")   #gets the sentence to check
text = text.split()
   
for word in text:   #checks each word in turn
    check = binSearch(word,dictionary)
    if check == True:
       html.write(word + " ")
    else:
       html.write('<span style="color: red;">' + word + " " + '</span>')    #turns any mis-spelled words to red
       print(word)
html.write('</p></body></html>')    #closes tags
html.close()

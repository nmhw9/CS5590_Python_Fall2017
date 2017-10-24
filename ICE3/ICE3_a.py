newWordList = []
#Taking input string
inputstring = input("enter the words separated by comma")
words_list = inputstring.split(",")

#to strip spaces before and after each word
for word in words_list:
    newWord = word.strip()
    newWordList.append(newWord)

# To sort the words
newWordList.sort()

#to construct new string with sorted words
sortedString = ", ".join(newWordList)

#print final output
print("The sorted words string is")
print(sortedString)




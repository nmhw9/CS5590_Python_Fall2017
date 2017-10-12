
import nltk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.stem import  WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import wordpunct_tokenize

import string

#Read the file
readtext = file("input.txt").read()
#filter punctuations from text
readtext_nopucnt = readtext.translate(None,string.punctuation)
#tokenizing the words
wordtokens = word_tokenize(readtext_nopucnt)
#tokenizing the sentences
sentencetokens = sent_tokenize(readtext)


#lematizing the tokenized words
lematizedwords=[]
lemmatizer = WordNetLemmatizer()
for x in wordtokens:
    x=lemmatizer.lemmatize(x,pos='v')
    lematizedwords.append(x)
print(" Lematized word are:")
print (lematizedwords)
print
print ("=="*100)


#Using POS, remove all the verbs
print ("Removing the verbs")
noverbs=[]
tagged = pos_tag(lematizedwords)
print (tagged)
for i in tagged:
    if i[1]=="VB":
        print ("removed the verb: ",i)
    else:
        noverbs.append(i[0])
print
print ("remaing words are:")
print (noverbs)
print
print ("=="*100)


#Calculating the word frequency of the remaining words
print ("Word Count - dictionary")
word_count = {}
for w in noverbs:
    if w in word_count.keys():
        word_count[w] = word_count[w]+1
    else:
        word_count[w] = 1
print(word_count)
print
print ("=="*100)


#top five words that has been repeated most
print ("Top five words that has been repeated most and their count:")
import operator
sortedwords = sorted(word_count.items(),key=operator.itemgetter(1))
topfivewords = []
topfive=[]
im = -1
for five in range(1,6):
    topfiveword = sortedwords[im]
    topfivewords.append(topfiveword)
    topfive.append(topfiveword[0])
    im += -1
print (topfivewords)
print
print("=="*100)


#Find all the sentences with those most repeated words
sentcollection = []
filter_picksentence= set()
sentencetokens = sent_tokenize(readtext)
print ("....Finding the sentences with words ",topfive,"..... ")
print
#Extracting the sentences
print ("....extracting sentences...")
print
for every in topfive:
    for eachsent in sentencetokens:
        eachWordInSent = word_tokenize(eachsent)
        if every in eachWordInSent:
            sentcollection.append(eachsent)

#Concatinating the senctence without repeatation
print ("....concatinating sentences...")
print
finalSentence = str()
sentset = set(sentcollection)
for con in sentset:
    finalSentence = str(finalSentence+" "+con)
print ("Final Summary: ")
print (finalSentence)



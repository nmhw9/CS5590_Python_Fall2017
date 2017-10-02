sentence = input("Enter your sentence")
sentence_split=sentence.split(' ')
# print(sentence_split)
sentence_set= set(sentence_split)
# print(sentence_set)
print("You entered following words in the sentence(they are "
      "sorted in alphabetical order)")
sorted_words=sorted(sentence_set)
# print(sorted_words)
for words in sorted_words:
    new_string=' '.join(sorted_words)
print(new_string)

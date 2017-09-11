# list =[(10,2),(2,3),(6,4)]
# print(list)
# print(list[0][0])
# list.append((4,6,"ramu"))
# print(list)
# list.sort()
# print(list)
# a = len(list)-1
# print(a)
# print(list[a])


newlist = []
list = list(input('eneter words separating space').split(' '))
print(list)
for i in list:
    L = len(i)
    newlist.append((L,i))
print('your word lengths are:',newlist)
newlist.sort()
print('After Sorting:',newlist)
le= len(newlist)-1
print('the longest word length is',newlist[le])





# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
# a new list of only the first and last elements of the given list. The purpose behind this is how
# to access the elements of the list, in this example you should return 5 and 25

newlist =[]
String = input("Enter the numbers with space separating")
mylist = list(String.split(' '))
print('list of numbers you entered', mylist)
listlength = len(mylist)
print('Length of the list is',listlength)
newlist.insert(0,mylist[0])
newlist.append(mylist[listlength-1])
print('your new list is',newlist)

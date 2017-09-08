firstnumb = 15
secondnumb = 25.0
name = "naveen"
lastname='macha'
print('welcome',name,lastname)
print(firstnumb,'plus',secondnumb,'is',firstnumb+secondnumb)

print('you should enters the numbers now')
firstsstring = input('enter first value')
secondstring = input('enter second value')
print('I read them as strings')
print('shall i convert them to integers!')
x=input('enter yes/no')
if x=='yes':
    print('converting')
    x1=int(firstsstring)
    x2=int(secondstring)
    print(x1,'plus',x2,'is',x1+x2)
elif x=='no':
    print('i can not add two strings for you')
else :
    print('that is not valid input')
print('thank you! for using me')







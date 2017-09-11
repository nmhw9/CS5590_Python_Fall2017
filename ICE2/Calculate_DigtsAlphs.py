# Get a string and calculate the number of digits and letters. you should use
# isdigit() and isalpha() to recognize which kind of letter or number the
# string contains
digits = 0
alpha = 0
string = input("Enter the string")
for i in range(0,len(string)):
    char = string[i]
    if char.isdigit():
        digits = digits +1
        print('dg',end=' ')
    elif char.isalpha():
        alpha = alpha+1
        print("aph",end=' ')
    else:
        print("other")
print()
print("number of digits %d" %digits)
print("number of letters %d" %alpha)



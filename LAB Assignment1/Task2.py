String = input("plese enter the string")
tuple = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
j = 0
k = 0
for i in tuple:
    if i in String:
        print(i, 'present')
        j = j+1
    else:
        print(i, 'is not present')
        k = k+1
print(j,'alphapets are present', k, ' are not present')



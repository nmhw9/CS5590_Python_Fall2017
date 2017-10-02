n = int(input('Enter  a number '))
mydict={}
for i in range(1, n+1):
    nstring=str(i)
    # print(nstring)
    mydict[nstring]=i*i
print(mydict)

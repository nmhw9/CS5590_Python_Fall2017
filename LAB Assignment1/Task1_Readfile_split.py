
i=0
wordlist = []
wordcount = []
fileName = input('what is the file name?')
infile = open(fileName,'r')
line = infile.readline()

while line!='':
    for xStr in line.split(" "):
        if xStr not in wordlist:
            wordlist.insert(i,xStr)
            wordcount.insert(i,1)
            i=i+1
        else:
            getindex = wordlist.index(xStr)
            indexvalue = wordcount[getindex]
            indexvalue = indexvalue+1
            wordcount[getindex]=indexvalue
    line = infile.readline()
listlength = len(wordlist)
for k in range(0,listlength):
    print('{',wordlist[k],':',wordcount[k],'}',end="  ")

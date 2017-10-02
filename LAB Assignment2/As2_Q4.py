import numpy as np

vector = np.random.random((1,15))

print("Random vector generated is ")
print(vector)
print()

if vector[0,0]>vector[0,1]:
    max = vector[0,0]
    index = 0
else:
    max = vector[0,1]
    index = 1

for i in range(2,15):
    if vector[0,i]>max:
        max = vector[0,i]
        index = i
    else:pass

print("Replacing maximum value ", max,end= " ")
print("at index vector[0,", index,"] with  100 ")
print()

print("New vector is ")
np.put(vector,[index],[100])
print(vector)










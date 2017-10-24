import numpy as np
import matplotlib .pyplot as plt
a = (0,1,2,3,4,5,6,7,8,9)
b = (1,3,2,5,7,8,8,9,10,12)
x = np.array(a)
y = np.array(b)

def linearModel(x,y):
    xm = np.mean(x)
    ym = np.mean(y)
    print("X mean:", xm, "\t", "Y mean", ym)
    print()
    ssxy = 0.
    ssxx = 0.
    beta1 = 0.
    beta0 = 0.
    ypre = []
    for i in range(0,len(x)):
        xi = x[i]
        yi = y[i]
        ssxy = ssxx + ((xi - xm)*(yi - ym))
        ssxx += ((xi-xm)*(xi-xm))
    beta1 = ssxy/ssxx
    beta0 = ym - (beta1*xm)
    for j in range(0,len(x)):
        ypre.append(beta0+(beta1*x[j]))
    ypred = np.array(ypre)
    print("Coefficients fit are")
    print("Slope-Beta1:",beta1)
    print("Intercept-Beta0:", beta0)
    plt.scatter(x,y)
    plt.plot(x,ypred)
    plt.show()
    return

linearModel(x,y)


# xi = 0
# yi = 1
# SSxy = 0
# x_mean = .2
# y_mean = .3
# for i in range(1,5):
#     SSxy = SSxy +((xi-x_mean)*(yi-y_mean))
# print(SSxy)

# a= [1,3,4]
# print(a)
# b = np.array(a)
# print(b)





# import numpy as np
# import matplotlib .pyplot as plt
# a = (0,1,2,3,4,5,6,7,8,9)
# b = (1,3,2,5,7,8,8,9,10,12)
# x = np.array(a)
# y = np.array(b)
# xmean = x.mean()
# print(xmean)
# print(x[0])
# sum = 0
# sqsum = 0
#
# for i in range(0,len(x)):
#     sum += x[i]
#     sqsum += np.power(x[i],2)
# print(sum)
# print(sqsum)


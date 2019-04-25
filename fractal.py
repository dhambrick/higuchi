import numpy as np 
import matplotlib.pyplot as plt
import math
from scipy import stats

def _higuchi(x,k_max):
    N = len(x)
    ensbL_k = []
    ks = np.linspace(1,k_max,num=k_max,dtype="int32")
    for k in ks:
        L = []
        for m in range(0,k):
            end = math.floor((N-m-1)/k)
            sumLKM = []
            normFactor = (N-1)/(end * k )
            for i in range(0,end):
                idx1 = m + (i+1)*k
                idx0 = m + i*k
                summand = np.abs(x[idx1] - x[idx0] )
                sumLKM.append(summand)  
            sumLKM = (1/k)*normFactor*np.sum(np.asarray(sumLKM))
            L.append({"m":m ,"sum":sumLKM})
        avgL_m = 0
        n = 0
        for avg in L:
            avgL_m = avgL_m + avg["sum"] 
            n = n+1
        avgL_m = avgL_m / n
        ensbL_k.append(avgL_m)
    slope, _, _, _, _ = stats.linregress(np.log2(1.0/ks),np.log2(np.asarray(ensbL_k)))
    return slope
    


N = 2**15
n = 1000
k_max = 2**11
Y = np.zeros(N)
Z = np.random.randn(n+N)
for i in range(n,N):
  Y[i] = np.sum(Z[0:i])

fracDim = _higuchi(Y,k_max)
print("fracDim %f" % fracDim)
plt.figure()
plt.plot(Y)    
plt.show()
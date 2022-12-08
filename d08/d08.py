import numpy as np

l = np.array([[*map(int, line.strip())] for line in open(0)])
n, m = l.shape

print(sum(
    any(sl.max(initial=-1) < l[i][j] 
        for sl in [l[:i,j], l[i+1:,j], l[i,:j], l[i,j+1:]]) 
    for i in range(n) for j in range(m)
))
l = np.pad(l[1:-1, 1:-1], 1, constant_values=9)
print(max(
    np.array([np.argwhere(sl >= l[i][j])[0,0] + 1 
        for sl in [l[:i,j][::-1], l[i+1:,j], l[i,:j][::-1], l[i,j+1:]]]).prod() 
    for i in range(1,n-1) for j in range(1,m-1)
))

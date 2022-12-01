l=sorted(sum(map(int,l.split()))for l in open(0).read().split('\n\n'))
print(l[-1],sum(l[-3:]))

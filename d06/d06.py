l=input()
for n in 4,14:print([i for i in range(len(l)+1)if len({*l[i-n:i]})==n][0])

print(*map(sum,zip(*[(lambda a,b:((b-a+1)%3*3+b,(a+b)%3-2+b*3))(ord(a)-64,ord(b)-87)for a,b in map(str.split,open(0))])))

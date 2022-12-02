print(*map(sum,zip(*[(((b:=ord(d)-87)-(a:=ord(c)-64)+1)%3*3+b,(a+b)%3-2+b*3)for c,d in map(str.split,open(0))])))

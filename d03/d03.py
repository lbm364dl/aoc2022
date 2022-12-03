# take dx copies of iterator
# apply zip to them -> grouping each dx of them
# why does it not return just dx copies of each element?
# because iterator consumes each element, and we dont have deep copies
parts = lambda l, dx: zip(*[iter(l)]*dx)

# take common element and map it to score
# subtract 96: 'a' -> 1, 'A' -> -31
# send 'A' to 27 -> -31 % 58 == 27 -> apply mod 58
score = lambda part: (ord(set.intersection(*map(set, part)).pop())-96)%58

inp = open('input.txt').read().split()

print(sum(score(parts(l, len(l)//2)) for l in inp))
print(sum(map(score, parts(inp, 3))))

l = [[set(range(*[int(p)+i for i, p in enumerate(s.split('-'))])) for s in l.split(',')] for l in open(0)]
print(sum((a&b in [a, b]) for a, b in l))
print(sum(bool(a&b) for a, b in l))

*l, = map(str.split, open(0))
delta = {'U': 1j, 'R': 1, 'D': -1j, 'L': -1}

def star(knots):
    visited = {0}
    hs = [0] * knots
    
    for d, v in l:
        for _ in range(int(v)):
            hs[0] += delta[d]
            for i in range(1, knots):
                diff = hs[i-1] - hs[i]
                re, im = diff.real, diff.imag
                if max(abs(re), abs(im)) > 1:
                    diff -= re/2 * (abs(re) == 2)
                    diff -= im/2 * (abs(im) == 2) * 1j
                    hs[i] += diff
    
            visited.add(hs[-1])
    
    return len(visited)

print(star(knots=2))
print(star(knots=10))

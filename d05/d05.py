from functools import reduce

stack, moves = open(0).read().split('\n\n')
stack = [[]] + [''.join(l).strip()[::-1] for l in zip(*[l[1::4] for l in stack.split('\n')[:-1]])]
moves = [[*map(int, m[1::2])] for m in map(str.split, moves.split('\n')[:-1])]

def f(acc, move):
    st, dx = acc
    cnt, p_from, p_to = move
    st[p_to] += st[p_from][-cnt:][::dx]
    st[p_from] = st[p_from][:-cnt]
    return st, dx

star = lambda dx, st: ''.join(c[-1] for c in reduce(f, moves, (st, dx))[0][1:])
print(star(-1, stack.copy()), star(1, stack.copy()))

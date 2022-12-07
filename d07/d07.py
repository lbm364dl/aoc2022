from collections import defaultdict

*l, = map(str.split, open(0).read().split('\n')[:-1])
ls_done = set()
cur_ls = None
sizes = defaultdict(int)
st = ['']
join = lambda l: '/'.join(l)

# assuming there could be more than one ls for each directory

for m in l:
    if m[0] == '$':
        if cur_ls:
            ls_done.add(join(st))
            cur_ls = None

        if m[1] == 'cd':
            if m[2] == '..':
                st.pop()
            elif m[2] == '/':
                st = ['']
            else:
                st.append(m[2])
        else:
            cur_ls = join(st)
    elif m[0] != 'dir' and join(st) not in ls_done:
        for i in range(len(st)):
            sizes[join(st[:i+1])] += int(m[0])


print(sum(v for v in sizes.values() if v <= 100000))
need = 30000000 - (70000000 - sizes[''])
print(min(v for v in sizes.values() if v >= need))

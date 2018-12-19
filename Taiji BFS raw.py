init=input()
op=input()
n=len(init)
assert n>0 and len(op)==n
tonum=lambda s:eval('0b%s'%s)
tobin=lambda i:bin(i)[2:].rjust(n,'0')
rev_target=(1<<n)-1
paths=[tonum(op[i:]+op[:i]) for i in range(n)]
start=tonum(init)
track={start:(-1,start)}
layer=[start]
solved=False
while layer:
    next_layer=[]
    for prev in layer:
        for i in range(n):
            next=prev^paths[i]
            if next in track:
                continue
            next_layer.append(next)
            track[next]=(i,prev)
    layer=next_layer
    if 0 in track or rev_target in track:
        solved=True
        break
if solved:
    ptr=(rev_target in track) and rev_target
    res=[]
    while ptr!=start:
        node=track[ptr]
        res.append(node)
        ptr=node[1]
    for i in res[::-1]:
        print(tobin(i[1]),i[0])
else:
    print('无解')
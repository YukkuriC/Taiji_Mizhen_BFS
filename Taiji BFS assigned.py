init=input('初始场景：')
op=input('黑线设置：')
target=input('目标设置：')
n=len(init)
assert n>0 and len(op)==len(target)==n
tonum=lambda s:eval('0b%s'%s)
tobin=lambda i:bin(i)[2:].rjust(n,'0')
targets=set(tonum(target[i:]+target[:i]) for i in range(n))
paths=[tonum(op[i:]+op[:i]) for i in range(n)]
start=tonum(init)
visited=set()
track={start:(-1,start)}
layer=[start]
solved=False
while layer:
    next_layer=[]
    for prev in layer:
        for i in range(track[prev][0]+1,n):
            next=prev^paths[i]
            if next in track:
                continue
            next_layer.append(next)
            track[next]=(i,prev)
            visited.add(next)
    layer=next_layer
    if visited&targets:
        solved=True
        break
if solved:
    ptr=list(visited&targets)[0]
    res=[]
    while ptr!=start:
        node=track[ptr]
        res.append(node)
        ptr=node[1]
    for i in res[::-1]:
        print(tobin(i[1]),i[0])
else:
    print('无解')
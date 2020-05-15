list=[]
n=int(input('N>>>'))
for i in range(0,10):
    x=int(input('input 10 numbers>>>'))
    list.append(x)
    if x==n:
        a=list.index(x)
print(list)
print(a)

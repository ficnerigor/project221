list=[]

for i in range(0,10):
    x=int(input('input 10 numbers>>>'))
    list.append(x)

def most_frequent(list):
    return max(set(list), key=list.count)

#  верно, но решение работает за O(N^2), а можно было решить за O(N)
print(most_frequent(list))



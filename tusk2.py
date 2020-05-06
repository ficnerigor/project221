a = int(input('add in list>>> '))
list = []
while True:
    try:
        list.append(a)
        a = int(input('add in list>>> '))
    except:
        print(list)
        print(max(list))
        p=list.index(max(list))
        list.pop(p)
        break
print(max(list))
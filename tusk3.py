list = []
while True:
    try:
        a = int(input('add in list>>> '))
        if a==0:
            list.insert(0, a)
        else:
            list.append(a)
    except:
        break
print(list)
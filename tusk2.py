a = int(input('add in list>>> '))
list = []
while True:
    try:
        list.append(a)
        a = int(input('add in list>>> '))
    except:
        break
print(list)
print(max(list))
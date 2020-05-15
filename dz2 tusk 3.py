import random
x=int(input('>>>'))
y=random.randint(1,10)
while x!=y:
    if x!=y:
        print('False')
        x = int(input())
    elif x==y:
        break
print('True')
print(x)


#Программа загадывает целое число в промежутке [1; 10] (от 1 до 10 включительно)
#и просит пользователя отгадать его. Программа не завершается, пока число не будет отгадано.

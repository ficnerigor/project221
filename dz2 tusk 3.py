import random

# обращай внимание на предупреждения PEP8 (pycharm подчеркивает их желтым цветом)
# 1. между оператором и выражениями должен быть пробел
# 2. после , должен быть пробел
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

# очень запутанно получилось
# ты мог бы изменить порядок операций, и стало бы намного проще, например:
y = random.randint(1, 10)

while x != y:
    x = int(input('>>>'))
    if x == y:
        break
    print('False')

print('True')
print(y)


#Программа загадывает целое число в промежутке [1; 10] (от 1 до 10 включительно)
#и просит пользователя отгадать его. Программа не завершается, пока число не будет отгадано.

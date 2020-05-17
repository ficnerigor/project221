import calendar

d=int(input('day:'))
m=int(input('month:'))
y=int(input('year:'))
day=calendar.weekday(y,m,d)
# можно было использовать calendar.day_name
if day==0:
    print('Monday')
elif day==1:
    print('Tuesday')
elif day==2:
    print('Wednesday')
elif day==3:
    print('Thursday')
elif day==4:
    print('Friday')
elif day==5:
    print('Saturday')
elif day==6:
    print('Saturday')



#Пользователь вводит дату своего рождения в формате DD.MM.YYYY. Вывести
#название дня недели, в который родился пользователь.



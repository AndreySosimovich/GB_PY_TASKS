# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = 123456
# n = [int(i) for i in str(n)]
# if n[0]+n[1]+n[2]==n[3]+n[4]+n[5]:
#     print('yes')
# else: print('no')

n = 123456
a = n%10
n = n//10
b = n%10
n = n//10
c = n%10
n = n//10
d = n%10
n = n//10
e = n%10
f = n//10
if (a+b+c==d+e+f):
     print('yes')
else: print('no')

# print(a,b,c,d,e,f)




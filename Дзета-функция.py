'''
Задача №3447. Дзета-функция.
А вот другой ряд, в котором вычисляется значение дзета-функции для числа 2:
((1/1**2+1/2**2+1/3**2+1/4**2+1/5**2+1/6**2+1/7**2+1/8**2+1/9**2+1/10**2)*6)**0.5
'''
x=sum([1/i**2 for i in range(1,11)])
x1=(x*6)**0.5
print(x1)
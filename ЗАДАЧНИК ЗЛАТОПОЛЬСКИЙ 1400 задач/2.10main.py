print("Введите первое число ",end='')
a=input()
a=int(a)
b=int(input("Введите второе число "))
#вычисляем среднее арифметическое
sa=(a+b)/2
#вычисляем среднее геометрическое
import math
sg=math.sqrt(a*b)
print("Среднее арифметическое равно ",sa)
print("Среднее геометрическое равно ",sg)
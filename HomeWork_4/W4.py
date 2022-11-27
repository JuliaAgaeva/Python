#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
from random import randint
k=int(input())
list=[randint(0,101) for i in range(k+1)]
print(list)
numbers=[]
for i in range(len(list)):
    b = k-i
    numbers.append(b)
print(numbers)  
file=open('out.txt', 'w')
file.write(str(list) + "\n")
file.write(str(numbers))
file.close()
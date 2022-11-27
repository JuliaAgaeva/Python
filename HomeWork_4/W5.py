#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint
k1=int(input())
list1=[randint(0,101) for i in range(k1)]
print(list1)
numbers1=[]

for i in range(len(list1)):
    b = k1-i-1
    numbers1.append(b)
print(numbers1)  
file=open('out1.txt', 'w')
file.write(str(list) + "\n")
file.write(str(numbers1))
file.close()

k2=int(input())
list2=[randint(0,101) for i in range(k2)]
print(list2)
numbers2=[]
for i in range(len(list2)):
    b = k2-i-1
    numbers2.append(b)
print(numbers2)  
file=open('out2.txt', 'w')
file.write(str(list) + "\n")
file.write(str(numbers2))
file.close()

summ=[]

for i in range(len(list2)):
    b = list1[numbers1[i]]+list2[numbers2[i]]
    summ.append(b)
summ.reverse()
print(summ) 

file=open('out3.txt', 'w')
file.write(str(summ) + "\n")
file.close()

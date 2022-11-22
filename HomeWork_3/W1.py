 #Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list=list(map(int,input().split()))
sum = 0
for i in range(0, len(list)):
 if i%2 !=0:
    sum +=list[i]
print(sum)




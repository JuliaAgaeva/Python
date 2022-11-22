#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list=list(map(int,input().split()))
n=len(list)
numbers = []
for i in range(0, n//2):
  prop=list[i]*list[n-1-i]
  numbers.append((prop))
print(numbers)


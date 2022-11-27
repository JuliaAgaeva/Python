#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
list_inp = list(map(int,input().split()))
set_res = set(list_inp) 
print("The unique elements of the input list using set():") 
list_res = (list(set_res))
print(*list_res)



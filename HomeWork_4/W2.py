#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n=int(input())
def simpleDividers(n):
   answer = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           answer.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       answer.append(n)
   return answer
print(simpleDividers(n))
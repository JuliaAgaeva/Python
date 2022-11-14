# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = float(input('ax='))
ay = float(input('ay='))
bx = float(input('bx=:'))
by = float(input('by:'))
import math
distans = round((math.sqrt((ax-bx)**2+(ay-by)**2)),2)
print(f'Растояние между A и B = {distans}' )

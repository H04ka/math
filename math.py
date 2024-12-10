print("Задание", 1)
import math as m

a = int(input("введи число"))
b = int(input("введи число"))
c = int(input("введи число"))

d = ((m.pow(b, 2)) - (4*a*c))
print(d)
if d > 0:
   x1 = (-b + m.sqrt(d)) / (2*a)
   x2 = (-b - m.sqrt(d)) / (2*a)
   print("2 корня", {x1}, {x2})
elif d == 0:
    x = (-b/ 2* a)
    print("1 корень", {x})
else:
    print("нет корней")
    
print("Задание", 2)

AB = int(input("Введите длинну первого катета"))
AC = int(input("Введите длинну второго катета"))
BC = m.sqrt((AB**2 + AC**2))
print("третий катет:", BC)

S = AB * AC / 2
P = AB + AC + BC

print("Площадь", S)
print("Периметр", P)

print("Задание", 3)

r = int(input("Введите радиус круга"))
S = float(m.pi) * r**2
print(S)

print("Задание", 4)

z = int(input("введи число"))
v = int(input("введи число"))
n = int(input("введи число"))

if z+v > n:
    print("треугольник существует")
elif z+v < n:
    print("треугольник не существует")

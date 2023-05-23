from math import pi
figure_type = str(input())
S = 0

if figure_type == "square":
    x = float(input())
    S = x * x

elif figure_type == "rectangle":
    x = float(input())
    y = float(input())
    S = x * y

elif figure_type == "circle":
    r = float(input())
    S = pi * (r * r)

elif figure_type == "triangle":
    x = float(input())
    h = float(input())
    S = x * (h / 2)
print(f'{S:.3f}')

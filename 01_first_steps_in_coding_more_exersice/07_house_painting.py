x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 * 1.5
square_wall = x * x
rectangle_wall = x * y
walls_total_painted_area = (square_wall * 2 - door) + (rectangle_wall * 2 - window * 2)

triangle_roof = x * h/2
rectangle_roof = x * y
roof_total_painted_area = triangle_roof * 2 + rectangle_roof * 2

green_expense_litres = walls_total_painted_area / 3.4
red_expense_litres = roof_total_painted_area / 4.3

print(f'{green_expense_litres:.2f} l.')
print(f'{red_expense_litres:.2f} l.')

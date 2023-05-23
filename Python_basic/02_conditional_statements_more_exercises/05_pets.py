from math import floor, ceil

number_of_days = int(input())
total_food_kg = int(input())
dog_eats_food_kg = float(input())
cat_eats_food_kg = float(input())
turtle_eats_food_g = float(input())

food_eaten_total = number_of_days * (dog_eats_food_kg + cat_eats_food_kg + turtle_eats_food_g / 1000)

if total_food_kg >= food_eaten_total:
    print(f"{floor(total_food_kg - food_eaten_total)} kilos of food left.")
else:
    print(f'{ceil(food_eaten_total - total_food_kg)} more kilos of food are needed.')


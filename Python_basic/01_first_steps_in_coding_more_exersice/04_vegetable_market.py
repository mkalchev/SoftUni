veg_price_per_kg = float(input())
fruit_price_per_kg = float(input())
veg_total_kg = int(input())
fruit_total_kg = int(input())

veg_total_revenue = veg_price_per_kg * veg_total_kg
fruit_total_revenue = fruit_price_per_kg * fruit_total_kg
revenue_in_eu = (veg_total_revenue + fruit_total_revenue) * 1.94

print(f'{revenue_in_eu:.2f} EU')
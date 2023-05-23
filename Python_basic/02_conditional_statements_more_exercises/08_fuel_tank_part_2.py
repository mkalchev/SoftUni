fuel_type = str(input())
quantity_fuel = float(input())
membership_card = str(input())

GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

price_fuel = 0

if membership_card == 'Yes':
    GASOLINE_PRICE -= 0.18
    DIESEL_PRICE -= 0.12
    GAS_PRICE -= 0.08

if fuel_type == "Gasoline":
    price_fuel = GASOLINE_PRICE
elif fuel_type == "Diesel":
    price_fuel = DIESEL_PRICE
elif fuel_type == "Gas":
    price_fuel = GAS_PRICE

total_price = quantity_fuel * price_fuel

if 20 <= quantity_fuel <= 25:
    total_price *= 0.92
elif quantity_fuel > 25:
    total_price *= 0.90

print(f'{total_price:.2f} lv.')

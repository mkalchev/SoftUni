vacation_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
toy_trucks_count = int(input())

PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TOY_TRUCK_PRICE = 2

total_toys_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + toy_trucks_count
total_price = puzzles_count * PUZZLE_PRICE + talking_dolls_count * TALKING_DOLL_PRICE\
              + teddy_bears_count * TEDDY_BEAR_PRICE + minions_count * MINION_PRICE\
              + toy_trucks_count * TOY_TRUCK_PRICE

if total_toys_count >= 50:
    total_price *= 0.75

#before final calc rent needs to be paid rent is 10%
rent = total_price * 0.10
revenue = total_price - rent

if revenue >= vacation_price:
    print(f'Yes! {revenue - vacation_price:.2f} lv left.')
else:
    print(f'Not enough money! {vacation_price - revenue:.2f} lv needed.')


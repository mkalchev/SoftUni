movie_budget = float(input())
number_of_extras = int(input())
price_for_outfit = float(input())

decor_price = movie_budget * 0.10

if number_of_extras > 150:
    price_for_outfit *= 0.90

total_price_outfits = number_of_extras * price_for_outfit
expenses_total = total_price_outfits + decor_price

if expenses_total <= movie_budget:
    print("Action!")
    print(f'Wingard starts filming with {movie_budget - expenses_total:.2f} leva left.')
else:
    print("Not enough money!")
    print(f'Wingard needs {expenses_total - movie_budget:.2f} leva more.')


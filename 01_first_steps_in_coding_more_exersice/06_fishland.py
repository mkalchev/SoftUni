skumria_price = float(input())
tcatca_price = float(input())
palamud_quantity_kg = float(input())
safrid_quantity_kg = float(input())
midi_quantity_kg = int(input())

palamud_price = skumria_price * 1.6
safrid_price = tcatca_price * 1.8
midi_price = 7.50

total_sum_fish = palamud_quantity_kg * palamud_price + safrid_quantity_kg * safrid_price \
                 + midi_quantity_kg * midi_price

print(f'{total_sum_fish:.2f} lv.')

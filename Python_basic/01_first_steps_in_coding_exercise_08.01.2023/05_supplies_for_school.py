#how many packets of pens
num_pen_packets = int(input())
#how many packets of markers
num_marker_packets = int(input())
#how much cleaning solution in litres
litres_cleaning_solution = int(input())
discount_percentage = int(input()) / 100

price_pen_packets = 5.80
price_marker_packets = 7.20
price_per_litre_cleaning_solution = 1.20

#total price for the pens
total_price_pens = num_pen_packets * price_pen_packets
#total price for the markers
total_price_markers = num_marker_packets * price_marker_packets
#total price for the cleaning solution
total_price_cleaning = litres_cleaning_solution * price_per_litre_cleaning_solution
#just the discount sum
total_discount = (total_price_pens + total_price_markers + total_price_cleaning) * discount_percentage
#total sum with discount
total_sum = (total_price_pens + total_price_markers + total_price_cleaning) - total_discount

print(f'{total_sum} lv.')



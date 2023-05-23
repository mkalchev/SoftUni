from math import floor, ceil

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

MAGNOLIA_PRICE = 3.25
HYACINTH_PRICE = 4
ROSE_PRICE = 3.50
CACTUS_PRICE = 8

total_revenue_before_tax = magnolias_count * MAGNOLIA_PRICE + hyacinths_count * HYACINTH_PRICE\
                + roses_count * ROSE_PRICE + cactus_count * CACTUS_PRICE

total_revenue_after_tax = total_revenue_before_tax * 0.95

if total_revenue_after_tax >= present_price:
    print(f'She is left with {floor(total_revenue_after_tax - present_price)} leva.')
else:
    print(f'She will have to borrow {ceil(present_price - total_revenue_after_tax)} leva.')


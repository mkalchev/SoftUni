req_quantity_nylon = int(input())
req_quantity_paint = int(input())
req_quantity_paint_thinner = int(input())
hours_work_workers = int(input())

#mats prices
price_nylon_sqr_m = 1.50
price_paint_liter = 14.50
price_paint_thinner_liter = 5.00
nylon_bags = 0.40

#cost for nylon
extra_nylon = 2
extra_nylon_price = extra_nylon * price_nylon_sqr_m
total_sum_nylon = (req_quantity_nylon * price_nylon_sqr_m) + extra_nylon_price

#cost for paint
extra_req_paint = (req_quantity_paint * 0.1)
total_req_paint = extra_req_paint + req_quantity_paint
total_sum_paint = total_req_paint * price_paint_liter

#cost for paint thinner
total_sum_paint_thinner = req_quantity_paint_thinner * price_paint_thinner_liter
total_sum_mats = total_sum_nylon + total_sum_paint + total_sum_paint_thinner + nylon_bags

#cost of labor per hour
workers_wage_hour = total_sum_mats * 0.3
#cost of total labor
workers_total_wage = workers_wage_hour * hours_work_workers

#total costs for labor and mats
total_sum_all = total_sum_mats + workers_total_wage

print(f'{total_sum_all} lv.')

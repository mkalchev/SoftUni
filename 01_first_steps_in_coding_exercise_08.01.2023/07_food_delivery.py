#number of menus
num_chicken_menus = int(input())
num_fish_menus = int(input())
num_veggy_menus = int(input())

#prices
chicken_menu = 10.35
fish_menu = 12.40
veggy_menu = 8.15
delivery_price = 2.50

#total sum for ordered chicken menus
total_chicken_cost = chicken_menu * num_chicken_menus
#total sum for ordered fish menus
total_fish_cost = fish_menu * num_fish_menus
#total sum for ordered veggy menus
total_veggy_cost = veggy_menu * num_veggy_menus
#total sum without the delivery added
total_sum_no_delivery = total_chicken_cost + total_fish_cost + total_veggy_cost

desert_price = total_sum_no_delivery * 0.2
#total sum all
total_check_sum = total_sum_no_delivery + delivery_price + desert_price

print(f"{total_check_sum} lv.")

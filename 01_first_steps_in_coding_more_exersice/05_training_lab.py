w = float(input())
h = float(input())

desks_in_w = (w * 100) // 120
desks_in_h = ((h * 100) - 100) // 70

num_total_desks = (desks_in_w * desks_in_h) - 3

print(num_total_desks)

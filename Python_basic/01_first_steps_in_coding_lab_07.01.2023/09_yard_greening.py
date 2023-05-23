sqr_m = float(input())
sqr_m_price = 7.61
discount = 0.18
total_price = sqr_m * sqr_m_price
total_discount = total_price * discount
final_price = total_price - total_discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {total_discount} lv.")

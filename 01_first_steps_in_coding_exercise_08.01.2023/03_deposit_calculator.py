#депозирана сума
deposit_amount = float(input())
#срок на депозита
term_of_deposit = int(input())
#годишен лихвен процент
annual_percentage_rate = float(input()) / 100

#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
total_sum = deposit_amount + (term_of_deposit * ((deposit_amount * annual_percentage_rate) / 12))

print(total_sum)

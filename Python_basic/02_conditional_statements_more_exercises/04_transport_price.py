number_of_kilometres = int(input())
day_or_night = str(input())

TAXI_FIRST_FARE = 0.70
TAXI_DAY_FARE = 0.79
TAXI_NIGHT_FARE = 0.90
BUS_FARE = 0.09
TRAIN_FARE = 0.06

if number_of_kilometres < 20:
    if day_or_night == 'day':
        print(f'{TAXI_FIRST_FARE + TAXI_DAY_FARE * number_of_kilometres:.2f}')
    else:
        print(f'{TAXI_FIRST_FARE + TAXI_NIGHT_FARE * number_of_kilometres:.2f}')
elif 20 <= number_of_kilometres < 100:
    print(f'{BUS_FARE * number_of_kilometres:.2f}')
elif number_of_kilometres >= 100:
    print(f'{TRAIN_FARE * number_of_kilometres:.2f}')



holidays = int(input())

holidays_play_time = 127
work_days_play_time = 63
work_days = 365 - holidays

total_play_time = holidays * holidays_play_time + work_days * work_days_play_time

if total_play_time >= 30000:
    print(f'Tom will run away')
    print(f'{(total_play_time - 30000) // 60} hours and {(total_play_time - 30000) % 60} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{(30000 - total_play_time) // 60} hours and {(30000 - total_play_time) % 60} minutes less for play')
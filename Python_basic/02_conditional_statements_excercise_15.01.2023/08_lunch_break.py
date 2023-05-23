from math import ceil

serial_name = str(input())
episode_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4

total_time_needed = episode_length + lunch_time + relax_time
#time_left = break_time - total_time_needed

if break_time >= total_time_needed:
    print(f'You have enough time to watch {serial_name} and left with'
          f' {ceil(break_time - total_time_needed)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need"
          f" {ceil(total_time_needed - break_time)} more minutes.")


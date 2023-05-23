record_seconds = float(input())
distance_metres = float(input())
time_seconds_for_1m_distance = float(input())

water_resistance = distance_metres // 15
time_water_resistance = water_resistance * 12.5
ivan_total_time = time_seconds_for_1m_distance * distance_metres + time_water_resistance

if record_seconds > ivan_total_time:
    print(f" Yes, he succeeded! The new world record is {ivan_total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {ivan_total_time - record_seconds:.2f} seconds slower.")


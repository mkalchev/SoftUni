budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

GPU_PRICE = 250
gpu_total_price = GPU_PRICE * gpu_count
CPU_PRICE = gpu_total_price * 0.35
RAM_PRICE = gpu_total_price * 0.10

total_sum = gpu_total_price + cpu_count * CPU_PRICE + ram_count * RAM_PRICE

if gpu_count > cpu_count:
    total_sum *= 0.85

if total_sum <= budget:
    print(f"You have {budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")


V_pool = int(input())
pipe1_debit_per_hour = int(input())
pipe2_debit_per_hour = int(input())
H_worker_missing = float(input())
pool_filled_percentage = 0

pool_filled = H_worker_missing * (pipe1_debit_per_hour + pipe2_debit_per_hour)
pool_filled_percentage = 0
percentage_filled_pipe1 = 0
percentage_filled_pipe2 = 0

if pool_filled <= V_pool:
    pool_filled_percentage = (pool_filled / V_pool) * 100
    percentage_filled_pipe1 = ((pipe1_debit_per_hour * H_worker_missing) / pool_filled) * 100
    percentage_filled_pipe2 = ((pipe2_debit_per_hour * H_worker_missing) / pool_filled) * 100
    print(f"The pool is {pool_filled_percentage}% full. Pipe 1: {percentage_filled_pipe1:.2f}%."
          f" Pipe 2: {percentage_filled_pipe2:.2f}%.")

if pool_filled > V_pool:
    print(f"For {H_worker_missing} hours the pool overflows with"
          f" {pool_filled - V_pool:.2f} liters.")


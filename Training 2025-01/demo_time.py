import time

t0 = time.time_ns()

# function ....
print('Power nap')
time.sleep(2)
print('Wakker worden!')

t1 = time.time_ns()

print(f'{t1 - t0} nanoseconden geslapen')
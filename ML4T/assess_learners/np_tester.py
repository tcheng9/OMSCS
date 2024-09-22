import time

start_time = time.time()
time.sleep(1)
end_time = time.time()


print('start is', start_time)
print('wait is', end_time)

print((end_time-start_time))
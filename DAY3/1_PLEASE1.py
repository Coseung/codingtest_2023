import time
import os
import psutil
process = psutil.Process(os.getpid()) 
start_time = time.time()

n=25

k=4
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1 
    n //= k
result += (n - 1) 

print('1이 도달하기 까지 연산 횟수 :', result) 

end_time = time.time()
print("time :",end_time - start_time)
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) 
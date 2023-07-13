import time
import os
import psutil
h = int(input("1시~23시 사싱 시간 입력 :"))

start_time = time.time()
process = psutil.Process(os.getpid()) 
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if'3' in str(i)+ str(j) +str(k):
                count += 1
        #print(count)
        
        
print('최종 3이 카운트 된 결과는 :', count)

end_time = time.time()
print (end_time - start_time)
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0))
import time

s = input('암호화된 문자열을 입력하세요 :')
mo = ['a','e','i','o']
lst =[]
start_time = time.time()
for i in range(len(s)):
    if (s[i-1] in mo and s[i] =='g') or (s[i] in mo and s[i+1] =='g') :
        #if s[i+1] =='g':
        
        continue 
        
    else:
        lst.append(s[i])
    
print(''.join(lst))
end_time = time.time()
print("time:", end_time - start_time)


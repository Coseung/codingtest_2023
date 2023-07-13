N, M = map(int, input('열과 행 개수를 입력하시오 :').split())
mi = []
cardlst= [[0] * M for i in range(N)]  #다시한번 이해 하기

for i in range(N):
    for j in range(M):
        a = int(input(f"차례로 숫자를 입력하시오{[i]}{[j]}: "))
        cardlst[i][j] =a
        
for i in range(N):
    cardlst[i].sort()
    a = cardlst[i][0]
    mi.append(a)
    
      
print(max(mi))





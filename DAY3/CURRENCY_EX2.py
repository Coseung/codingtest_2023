lst =[]

n, k = map(int, input("동전의 총 개수와, 가격의 합을 입력하시오 :").split())
count = 0

for i in range(n):
    lst += [int(input(f"동전 {n}개를 순서대로 입력하시오 :"))]
lst.sort(reverse =True)

print(lst)    

for i in lst:
    if k >=i :
        count += k//i
        k %= i
        if k <= 0:
            break
    
print('동전의 거스름돈 최소개수는:',count)








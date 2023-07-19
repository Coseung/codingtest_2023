from bisect import bisect_left, bisect_right

def mac(n1, m, m1):
    s1 = []
    for i in m1:
        index = bisect_left(n1, i)
        if n1[index] == i:
            print('Yes',end =' ')
            
        else:
            print('No', end=' ')
            
            
        


n = int(input('전자매장 부품 개수 :'))
n1 = []
m1 = []
for i in range(n):
    a = int(input(f'전자매장 보유 부품{i + 1} :'))
    n1.append(a)

m = int(input('손님이 원하는 부품 개수 :'))
for i in range(m):
    b = int(input(f'손님이 원하는 부품{i + 1} :'))
    m1.append(b)
n1.sort()
m1.sort()
mac(n1,m,m1)


a = int(input('1부터 9 까지 숫자를 입력하시오 :'))
b = 9
for i in range(2,a+1):
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")
#f를 사용하면 숫자를 나타낼 수 있다.
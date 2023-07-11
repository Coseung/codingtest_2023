array =[]
while True:
    a = input("문자열을 입력하시오: ")
    
    if a =="": break
    array.append(a)
#print(array[:-1])


for a in array:
    print(a, end =',')
print()
c =tuple(array)
print("튜플로 변환한 값 :")
for i in c:
    print(i, end="\n")
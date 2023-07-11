array =[]
while True:
    a = input("문자열을 입력하시오: ")
    
    if a =="": break
    array.append(a)
#print(array[:-1])


for a in array:
    print(a, end =',')

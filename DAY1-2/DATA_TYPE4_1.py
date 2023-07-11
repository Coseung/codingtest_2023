n =4
m =3 
array =[[0]*m for i in range(n)]#N X M 크기의 2차원 리스트 초기화: 대괄호, 리스트 컴프리헨션
print(array)
print(type(array))

array[2][1] = 5

print(array)

a= [1,4,3]
print("기본리스트: ",a)

a.append(2)
print("삽입: ",a)

a.sort()
print("오름차순 정렬: ",a)

a.sort(reverse = True)#내림차순 정령
print("내림차순 정렬: ",a)

a.reverse()
print(a)

a.insert(2, 3) # 특정 인덱스에 데이터 추가
print("인덱스 2에 3 추가: ", a)

print("값이 3인 데이터 개수: ", a.count(3)) # 특정 값인 데이터 개수 세기

a.remove(1) # 특정 값 데이터 삭제
print("값이 1인 데이터 삭제: ", a)

a = [1, 2, 3, 4, 5, 5, 5] 
remove_set = {3, 5} # 특정 원소 모두 제거, 집합 자료형 활용

result = [i for i in a if i not in remove_set] # remove_list에 포함되지 않은 값만을 저장 not 해당하지 않은 
print(result)



#오름 차순 정렬, 내림차순 정렬 별표 많이나옴, append 는 문자 삽입 가능 
#sort는 문자가 있으면 오름차순 정렬이 안됨
#remove - 특정 값 데이터를 삭제 함 




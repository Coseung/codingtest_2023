# 자료형
a = (1,2,3,4,5,6,7,8,9) #  튜플, 소괄호로 선언 및 초기화
this_is_not_tuple = ("Seoul")
print(type(this_is_not_tuple))  # 튜플 주의! 서울은 튜플인가? 타입 출력
this_is_tuple = ("Seoul",)
print(type(this_is_tuple))  # , 콤마를 최소 1개 이상 추가 필요, 타입 출력

print(a[3]) # 네 번째 원소만 출력
print(a[1:4]) # 2~4번째 원소 출력, 인덱스/슬라이싱 지원
print(a[:]) # 전체 원소 출력
print(type(a)) # 현재 자료구조 타입 확인


#튜플은 하나이상 콤마가 있어야함
# 튜플은 데이터 타입이 달라도 입력가능 

#a[1] = 'i' 특정 인덱스의 데이터 직접 수정 불가

b = (1, 'apple', 'banana', 3.13, [1, 2, 3, 4, 5]) # 서로 다른 데이터/자료구조 입력
c = tuple(range(1, 10)) # range 함수로 초기화 가능
print(b) # 전체 출력

for c_tuple in c:
    print(c_tuple) # for문으로 loop 순회 출력, 1개씩 접근
print(c) # 전체 출력



# 자료형
b = (2, 'bakery', 'coffee', 3.13, [5, 4, 3, 2, 1]) # 서로 다른 데이터/자료구조 입력
b = b + (1.3, 'name', 5) # 데이터 변경 방법 1, but 변경된 것이 아님(새로 생성됨)
t_length = len(b) # 튜플의 길이 len 함수
print(t_length) # 튜플의 길이를 출력
print(b) # 전체 출력

lst = list(b) # 데이터 변경 방법 2, 리스트로 변환 내용 수정
lst.append('add') # 리스트 내용 추가
c = tuple(lst) # 리스트를 튜플로 변환
print(c) # 전체 출력
del c # del 키워드로 튜플 삭제

if 'coffee' in b: # if in으로 특정 데이터 존재 확인
    print('커피가 존재합니다.')
if '3.333' not in b: # if not in으로 특정 데이터가 존재하지 않는지 확인
    print('3.333은 존재하지 않습니다.’)

d = (3, 4444, (55, 55), 6) # 튜플내 자료 중첩도 가능
print(d) # 전체 출력







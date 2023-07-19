
n = int(input())

array = []
for i in range(n):
        input_data = input('나이와 이름을 순서대로 입력하시오 :').split()
        # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
        array.append((int(input_data[0]), input_data[1]))
        array = sorted(array, key=lambda student: student[0]) # 람다식, 키 기준 정렬

for student in array:
    print(student[0], student[1])



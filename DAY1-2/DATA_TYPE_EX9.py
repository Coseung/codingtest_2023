dic_sum ={'국어':0, '수학':0, '영어':0,'도덕':0, '물리':0}
sm =0

for key in dic_sum:
    dic_sum[key] =input(f"{key}의 점수를 입력하시오 :")
    sm += int(dic_sum[key])
    
print("전체 점수 :",sm)
print("과목 개수:", len(dic_sum.keys()))



print("평균 점수 :", sm/len(dic_sum.keys()))

s = input('2자리 이상 문자열 숫자와 제거 개수 를 입력하시오 :')
x = int(input('1자리 이상 제거할 숫자 개수를 입력하시오 :'))
if len(s) >1 and x>0:
    from itertools import combinations
    result = list(combinations(s, len(s)-x)) 
    print(''.join( max(result)))
    
    
    
#1번 문제 s,x 를 각각 문자열, 숫자로 입력 받고
#조합 을 사용하여 s의 길이에서 x를 뺀 갯수(출력 숫자 갯수)를 조합 하고 max함수를 사용 
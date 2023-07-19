from bisect import bisect_left, bisect_right


def count_by_value(lst, x):
    l_index = bisect_left(lst,x)
    r_index = bisect_right(lst,x)
    return r_index - l_index


a, x = map(int, input('리스트 길이, 찾는 수 :').split())
lst =[]
for i in range(a):
    lst.append(int(input()))
               
lst.sort()
cnt = count_by_value(lst, x)
print("특정 값의 개수는 {}입니다.".format(cnt))
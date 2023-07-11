lst =[]
def avg(*agr):
    a=0
    b=0
    for i in agr:
        lst.append(i)
        a += i
        b = len(lst)
         
    return a, a/b

a = avg(1, 2, 3, 4)
b = avg(1, 1, 1, 11, 1)

print(a, b)


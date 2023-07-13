s = input('입력하시오: ')
a_list=[-1]*26
a_dic ={}

for i in range(len(s)):
    sa = int(ord(s[i]))- int(ord('a'))
    a_list[sa]=i+1
        
print(a_list)




#딕셔너리 풀이법 
"""
for i in range(97, 123):
    a_dic[i] = -1
    
for i in range(len(s)):
    #if int(ord(s[i]))== a_dic.keys():
    a= int(ord(s[i]))
    a_dic[a] =i 

print(a_dic.values())
"""

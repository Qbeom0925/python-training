'''
자료형의 참과 거짓
자료형의 값을 저장하는 공간, 변수
'''
if[]:  #만약[]가 참이면
    print("true") #true라는 문자열 출력
else:  #만약 []가 거짓이면
    print("flase") #false라는 문자열 출력

a=3
b=3
a is b

#변수를 만드는 다양한 방법
a,b = ('python,','life')
(a,b)='python','life'
[a,b]=['python','life']
a=b='python'

a=3
b=5
a,b = b,a #a와b의 값을 바꿈

a=[1,2,3]
b=a

a=[1,2,3]
b=a
a[1]=4
print(a,b) #a,b는 같은 리스트인 [1,2,3]을 가르키고 있기 때문에 같이 1,4,3이 됨

a=[1,2,3]
b=a[:] #리스트 값의 영향을 받지 않음
a[1]=4
print(a,b)

from copy import copy
b=copy(a)
#b=copy(a)는 b=a[:]과 동일

a=['Life','is','too','short']
result=" ".join(a)
print(result)

a=[1,1,1,2,2,3,3,3,4,4,5]
aset=set(a)
b=aset
print(b)
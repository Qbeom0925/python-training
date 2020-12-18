"""
리스트 자료형
튜플 자료형
"""
a=[1,2,3]
print(a[0]) #첫번째 출력
print(a[0]+a[2]) #1+3

a=[1,2,3,['a','b','c']]
print(a[-1])
print(a[3])
print(a[-1][2])

a=[1,2,3,['a','b',['c','d']]]
print(a[3][2][0])

a=[1,2,3,4,5]
print(a[0:2])
print(a[:2])
print(a[2:])

a=[1,2,3]
b=[4,5,6]
print(a+b)

print(str(a[2])+"hi")

#리스트의 수정, 변경과 삭제
a=[1,2,3]
a[2]=4
print(a)
print(a[1:2])  #a[1]과 a[1:2]는 다른 것임
a[1:2]=['a','b','c']
print(a)

"리스트 관련 삭제"
a[1:3]=[] #삭제
del a[1] #[1]인 것을 삭제

"리스트에 추가관련"
a=[1,2,3]
a.append(4) #리스트 마지막에 4를 추가
print(a)
a.append([5,6]) #리스트 마지막에 [5,6]을 추가
print(a)
a=['a','b','c']
a.reverse()
print(a)
a=[1,2,3]
print(a.index(1)) #위치를 반환
print(a[2])

a=[1,2,3]
a.insert(0,4) #[0]에 4를 삽입
print(a)
a.remove(4) #a안에서 4를 한번 삭제
print(a)
a.pop() #a안에서 마지막 요소를 반환하며 삭제
a.count(2) #a안에서 2가 몇번 들어가는지 카운트
a.extend([4,5]) #+와 동일

"""
튜플은 1가지 요소만 가질수 있음
튜플은 괄호를 생략해도 무방함
"""
t1 =(1,2,'a,','b')
print(t1[0]) #튜플 인덱싱
print(t1[1:]) #튜플 슬라이싱
t2 = 3,4
print(t1+t2) #튜플 더하기
print(t2*3) #튜플 곱하기
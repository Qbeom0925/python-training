'''
딕셔너리 자료형
집합 자료형
'''

dic={'name' :'Tom','phone number':'01012345678','birth':'1225'}

a={1:'hi'}
a={'a':[1,2,3]}
a={1:'a'}
a[2]='b' #{2:'b'}쌍추가
print(a)
a['name']='bay'
print(a)
a[3]=[1,2,3]
print(a)
del a[1]
print(a)

grade={'pey':10,'juliet':99}
print(grade['pey'])

tom부양가족={'부양가족':'아들','부양가족직업':'군인'}
print("부양가족: "+tom부양가족['부양가족'], "부양가족직업: "+tom부양가족['부양가족직업'])

a={1:'a',2:'b'}
print(a[1])

a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())
for k in a.keys():
    print(k)
print(list(a.keys()))

print(a.values())

print(a.items())

print(a.clear())

a={'name':'pey','phone':'01119993323','birth':'1118',}
print(a.get('name'))
print('name'in a)

s1=set([1,2,3])
print(s1)
s2=set("Hello")
print(s2)

s1=set([1,2,3])
i1=list(s1)  #리스트로 변환
print(i1)

t1=tuple(s1)  #튜플로 변환
print(t1)

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
s1&s2 #교집합
s1.intersection(s2)  #교집합
s1|s2 #합집합
s1.union(s2) #합집합
s1-s2 #차집합
s2-s1 #차집합
s1.difference(s2) #차집합
s2.difference(s2) #차집합

s1 = set([1,2,3])
s1.add(4)
print(s1)

s1=set([1,2,3])
s1.update([4,5,6])

s1.set([1,2,3])
s1.remove(2)
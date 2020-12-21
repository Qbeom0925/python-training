"""
제어문
if
while
for
"""

x=3
y=2
print(x>y)
print(x<y)

money=2000
if money >= 3000:
    print("택시타고가라")
else:
    print("걸어가라")

money=2000
card=1
if money>=3000 or card :
    print("택시타고가라")
else:
    print("걸어가라")

1 in [1,2,3]
1 not in [1,2,3]

pocket = ['paper', 'cellphone','money']
if 'money' in pocket:
    print("택시타고가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone','money']
if 'money' in pocket:
    pass
else:
    print("걸어가라")

pocket = ['paper','cellphone']
card=1
if'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

pocket = ['paper','cellphone']
card=1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit ==10:
        print("나무가 넘어갑니다.")



coffe=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffe=coffe-1
    print("남은 커피의 양은 %d개 입니다."% coffe)
    if not coffe:
        print("SOLD OUT")
        break
'''
coffee=10
while True:
    money=int(input("돈을 넣어 주세요: "))
    if money ==300:
        print("커피를 준다.")
        coffee = coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
        coffee=coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''
a=0
while a<10:
    a=a+1
    if a %2 ==0: continue
    print(a)


test_list=['one','two','three']
for i in test_list:
    print(i+'1')

a=[(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)

marks=[90,25,67,45,80]
number=0 #학생에게 부여할 번호
for mark in marks:  # marks의 순서대로 mark에 대입
    number = number+1
    if mark>=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)

marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark < 60:continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

a=range(10)
print(a)

sum=0
for i in range(1,11):
    sum=sum+i

print(sum)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))

for i in range(2,10):  #1번 for문
    for j in range(1,10):  #2번 for문
        print(i*j,end=" ")
    print('')

a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)

print(result)

result=[num*3 for num in a]
print(result)

result=[num*3 for num in a if num %2 == 0]
print(result)

i=0
while True:
    i+=1
    if i>5:break
    print("*" * i)

A=[70,60,55,75,95,90,80,80,85,100]
total = 0
for point in A:
    total+=point
average=(total/len(A))
print(average)

result=0

def adder(num):
    global result
    result +=num
    return result

print(adder(2))
print(adder(5))

result1=0
result2=0

def adder1(num):
    global result1
    result1 += num
    return result1
def adder2(num):
    global result2
    result2 += num
    return result2

class simple:   #클래스 생성
    pass
a=simple() #인스턴스 생성

class Service:
    secret="영구는 두개"
    def __init__(self,name): #인스턴스를 만들때 항상 실행된다.
        self.name=name
    def sum(self,a,b):
        result=a+b
        print("%s님 %s+%s=%s입니다."%(self.name,a,b,result))

pey=Service("홍길동")
pey.sum(1,1)

class FourCal():
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def sum(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result

a=FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)
print(a.sum())
print(round(a.div()))
print(a.mul())
print(a.sub())

#한씨 집안 클래스
class HouseHan():
    lastname="한"
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,place):
        print("%s, %s여행을 가다."%(self.fullname,place))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네"%(self.fullname,other.fullname))
    def __add__(self,other): #연산잔오버로딩
        print("%s,%s 결혼했네"%(self.fullname,other.fullname))
    def fight(self,other):
        print("%s, %s 싸우네"%(self.fullname,other.fullname))
    def __sub__(self, other):
        print("%s과 %s은 이혼을 했네"%(self.fullname,other.fullname))


pey=HouseHan("규범")
pey.travel("부산")

#클라스 상속
class HouseKim(HouseHan):
    lastname = "김"
    def travel(self,place,day):  #메서드 오버라이딩
        print("%s, %s여행을 %d일 가다."%(self.fullname,place,day))

jult=HouseKim("기자")
jult.travel("독도",3)

pey=HouseHan("규범")
jult=HouseKim("기자")
pey.love(jult)
pey+jult
print("-"*50)
pey=HouseHan("규범")
pey.travel("부산")
jult=HouseKim("줄리엣")
jult.travel("부산",3)
pey.love(jult)
pey+jult
pey.fight(jult)
pey-jult
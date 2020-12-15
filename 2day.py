'''
숫자형, 문자열 자료형
'''
#정수형
a=123
a=-178
a=0

#실수형
a=1.2
a=-3.45
a=4.24E10 #a=4.24*10^10
a=4.24e-10 #a=4.24^(-10)

#8진수 (0o,0O)
a=0o177

#16진수 (0x)
a=0x8ff
b=0xABC

#복소수
a=1+2j
b=3-4J

#복소수.real  실수의 부분을 리턴
a=1+2j
a.real  #1.0

#복소수.imag  허수의 부분을 리턴
a=1+2j
a.imag  #2.0

#복소수.conjugate()  켤레복소수를 리턴
a=1+2j
a.conjugate()  #(1-2j)

#abs(복소수) 복소수의 절댓값을 리턴
a=1+2j
abs(a) #2.23606797749979

#사칙연산
a=3
b=4
a+b  #7
a*b  #12
a/b  #0.75

#x의 y제곱
a=3
b=4
a**b #3^4 81

#나눗셈 후 나머지를 반환하는 %연산자
7%3  #1
3%7  #3

#나눗셈 후 아랫자리를 버리는 //연산자
7/4 #1.75
7//4 #1


#문자열 자료형
"Hello world"
'Hello world'
"""Hello world"""
'''Hello world'''
food="python's favorite food is perl"
print(food)
say='"python is very easy." he says.'
food2='python\'s favorite food is perl'
say2="\"python is very easy.\" he says."
print(food2)
print(say2)

multiline1="Life is too short \n You need python"
multiline2='''
Life is too short
You need python
'''
multiline3="""
Life is too short
You need python
"""
print(multiline1)
print(multiline2)
print(multiline3)

"""
\n 문자열 안에서 줄을 변경
\t 문자열 사이에 탭 간격을 줌
\\ 문자를 \그대로 표현할때
\' 작은따옴표(')를 그대로 표현
\" 큰따옴표(")를 그대로 표현 """

#문자열연산
head="python"
tail="is fun"
print(head+tail)

#문자열곱하기
a="python"
b=a*2
print(b)

#multistring.py
print("="*50)
print("My Program")
print("="*50)

#인덱싱=가리킨다, 슬라이싱=잘라낸다
a="Life is too short, You need python"
a[3]
print(a[3])
a="Life is too short, You need python"
a[0] #L
a[12] #s
a[-1] #n
a[-0] #L
b= a[0]+a[1]+a[2]+a[3] #Life
a[0:3] #Lif
a[19:] #You need python
a[:17] #Life is too short
a[19:-7] #You need

a="20010331Rainy"
date=a[:8]
weather=a[8:]
print(date)
print (weather)
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year)
print(day)
print(weather)

#수정
a="pithon"
a[:1] #P
a[2:] #thon
print(a[:1]+'y'+a[2:])

#문자열 포매팅
a = "I eat %d apples." %3
print(a)
b= "I eat %s apples." %"five"
print(b)
number=3
c="I eat %d apples." %number
print(c)
number=10
day="three"
d="i ate %d apples. so i was sick for %s days." %(number, day)
print(d)
'''
%s 문자열 = 어떤 형태든 문자로 입력해서 어느 값이든 가능
%c 문자1개
%d 정수
%f 부동소수'''
e="erro is %d%%" %98
print(e)
f="%10s"%"hi" #전체길이 10개, 공백8개
print(f)
g="%-10sjane."%'hi' #hi가 왼쪽 정렬
print(g)
h="%0.4f"%3.42134234 #소수점 4자리 까지만 출력
print(h)
j="%10.4f"%3.42134234 #소수점 4자리 까지만 출력 전체 길이가 10인 문자열 공간에 오른쪽 정렬
print(j)

a='hobby'
print(a.count('b'))

a="python is best choice"
print(a.find('b')) #b가 처음 나온 위치
print(a.find('k')) #찾는 문자나 문자열이 존재하지 않을 경우 -1을 반환
a=="Life is too short"
print(a.index('t')) #index는 없는 문자입력시 오류 발생
print(a.count('t'))

a=","
print(a.join('abcd'))

a="hi"
print(a.upper()) #소문자 => 대문자

a="HI"
print(a.lower()) #대문자 => 소문자

a=" hi "
print(a.lstrip()) #왼쪽 공백 지우기

a=" hi "
print(a.rstrip()) #오른쪽 공백 지우기

a=" hi "
print(a.strip()) #양쪽 공백 지우기

a="Life is too short"
print(a.replace("Life", "Your leg")) #문자열 바꾸기

a="Life is too short"
print(a.split()) #공백을 기준으로 문자열 나눔

a="a:b:c:d"
print(a.split(':')) #기호를 기준으로 문자열 나눔

#format
a="i eat {0} apples".format(3)
print(a)

a="i eat {0} apples".format("five")
print(a)

number=3
a="i eat {0} apples".format(number)

number=10
day="three"
a="i ate {0} apples. so i was sick for {1} days.".format(number, day)
print(a)

a="i ate {number} apples. so i was sick for {day} days.".format(number=10,day=3)
print(a)

a="I ate {0} apples. so I was sick for {day} days.".format(10,day=3)
print(a)

a="{0:<10}".format("hi") #왼쪽 정렬
print(a)

a="{0:>10}".format("hi") #오른쪽 정렬
print(a)

a="{0:^10}".format("hi") #가운데 정렬
print(a)

a="{0:=^10}".format("hi") #공백 =로 채우기
print(a)

a="{0:!<10}".format("hi") #<쪽으로 공백 !로 채우기
print(a)

y=3.42134234
a="{0:0.4f}".format(y) #소수점 4자리까지만 표출
print(a)

a="{0:10.4f}".format(y) #소수점 4자리까지만 표출 + 10자리까지 출력
print(a)

a="{{and}}".format() #{}를 출력
print(a)
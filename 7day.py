'''
함수
입력과 출력
파일 읽고 쓰기
'''


def sum(a, b):
    result = a + b
    return result


a = 3
b = 4
c = sum(a, b)
print(c)


def say():
    return 'HI'


a = say()
print(a)


def sum(a, b):
    print("%d,%d의 합은 %d입니다." % (a, b, a + b))


a = sum(3, 4)
print(a)


def say():
    print('Hi')


say()


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


result = sum_many(1, 2, 3)
print(result)

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)

result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)


def sum_and_mul(a, b):
    return a + b, a * b


result = sum_and_mul(3, 4)
print(result)


def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)


def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself('Qbeom', 23)

a = 1


def vartest(a):
    a = a + 1
    print(a)


vartest(a)

a = 1


def vartest(a):
    a = a + 1
    return a


a = vartest(a)
print(a)

a = 1


def vartest():
    global a
    a = a + 1


vartest()
print(a)

# a=input()
print(a)

# number=input("숫자를 입력하세요: ")

a = 123
print(a)
a = "Python"
print(a)
a = [1, 2, 3]
print(a)

print("life" + "is" + "too short")
print("life", "is", "too short")

for i in range(10):
    print(i, end='')

f = open("새파일.txt", 'w')
f.close()
'''f=open("D:/새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()'''

f = open("D:/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("D:/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

"""while 1:
    data=input()
    if not data:break
    print(data)"""

f = open("D:/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("D:/새파일.txt", 'r')
data = f.read()
print(data)
f.close

"""f=open("D:/새파일.txt",'a')
for i in range(11,20):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()"""

f = open("foo.txt", 'w')
f.write("Life is too short, You need python")
f.close()

"""with open("foo.txt") as f:
    f.write("Life is too short, you need python")"""

import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')


def fib(n):
    if n == 0:return 0
    if n == 1:return 1
    return fib(n-2)+fib(n-1)

for i in range(10):
    print(fib(i))


f = open("D:/sample.txt", 'r')
lines = f.readlines()
f.close

total=0
for line in lines:
    score = int(line)
    total += score
average = total/len(lines)

f=open("result.txt",'w')
f.write(str(average))
f.close()
'''
예외처리
'''
try:
    4/0
except ZeroDivisionError as e:
    print(e)

try:
    f=open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data=f.read()
    f.close

f=open('foo.txt','w')
try:
    pass
finally:
    f.close()

try:
    f=open("없는파일",'r')
except FileNotFoundError:
    pass

class Bird:
    def fly(self):
        print("very fast")

class Eagle(Bird):
    pass

eagle=Eagle()
eagle.fly()
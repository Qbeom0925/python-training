"내장함수"

#abs
print(abs(3))
print(abs(-3))

#all
print(all([1,2,3]))
print(all([1,2,3,0]))

#any
print(any([1,2,3,0]))
print(any([0,""]))

#chr
print(chr(97))
print(chr(48))

#dir
print(dir([1,2,3]))
print(dir({'1':'a'}))

#divmod
print(divmod(7,3))
print(divmod(1.3,0.2))

#enumerate
for i, name in enumerate(['body','foo','bar']):
    print(i, name)

#eval
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))

#filter
def positive(numberList):
    result=[]
    for num in numberList:
        if num>0:
            result.append(num)
    return
print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x>0
print(list(filter(positive,(1,-3,2,0,-5,6))))

#hex
print(hex(234))
print(hex(3))

#id
a=3
c=3
print(id(c))
print(id(3))
print(id(a))
b=a
print(id(b))

#input
#a=input()
#b=input("Enter: ")

#int
int('3')
int(3.4)
int('11',2)

#isintance
class Person: pass

a=Person()
print(isinstance(a,Person))
b=3
print(isinstance(b,Person))

#lambda
sum=lambda a,b:a+b
sum(3,4)

myList=[lambda a,b:a+b, lambda a,b:a*b]
myList[0]
myList[0](3,4)
myList[1](3,4)

#len
len("Python")
len([1,2,3])
len((1,'a'))

#ist
print(list("python"))
print(list((1,3,)))

#map
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result
result=two_times([1,2,3,4])
print(result)

def two_times(x): return x*2

list(map(two_times,[1,2,3,4]))

#max
max([1,2,3])
max("python")

#min
min([1,2,3])
min("python")

#oct
print(oct(34))
print(oct(12345))

#open
#f=open("binary_file","rb")

#ord
ord('a')
ord('0')

#pow
pow(2,4)
pow(3,3)

#range
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2)))
print(list(range(0,-10,-1)))

#sorted
print(sorted((3,1,2)))
print(sorted(['a','c','b']))
print(sorted('zero'))

#str
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

#tuple
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#zip
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc","def")))
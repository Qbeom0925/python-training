import sys
print(sys.argv)

import pickle
f=open("text.py",'wb')
data={1:'python',2:'you need'}
pickle.dump(data,f)
f.close

import os
os.environ
os.chdir("C:\WINDOWS")
os.getcwd()
os.system("dir")
f=os.popen("dir")

import shutil
shutil.copy("src.txt","dst.txt")

import glob
glob.glob("C:\python\quiz.py.bak")

import tempfile
filename=tempfile.mktemp()
filename

import time
time.time()
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('출력할 형식 포맷 코드',time.localtime(time.time())))
print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))
for i in range(10):
    print(i)
    time.sleep(0)

import calendar
print(calendar.prmonth(2021,1))
print(calendar.weekday(2021,1,1))
print(calendar.monthrange(2021,1))

import random
print(random.random())

def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data: print(random_pop(data))

data=[1,2,3,4,5]
random.shuffle(data)
print(data)

import webbrowser
webbrowser.open("http://google.com")

import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you','need','python']:
    t=threading.Thread(target=say, args=(msg,))
    t.daemon=True
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)

class Calculator():
        def __init__(self, numlist):
            self.numlist = numlist

        def sum(self):
            result = 0
            for num in self.numlist:
                result += num
            return result

        def avg(self):
            total = self.sum()
            return total / len(self.numlist)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())
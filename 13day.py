def compress_string(s):
    _c=""
    cnt=0
    result=""
    for c in s:
        if c!=_c:
            _c=c
            if cnt: result += str(cnt)
            result += c
            cnt=1
        else:
            cnt+=1
    if cnt:result+=str(cnt)
    return result
print(compress_string("aaabbcccccca"))

def chkDupNum(s):
    result=[]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
        return len(result)==10

import re
p=re.compile('ab*')
p=re.compile('[a-z]+')
m=p.match("3python")
print(m)
m=p.search("python")
print(m)
result=p.findall("life is too short")
print(result)
result=p.finditer("life is too short")
print(result)

p=re.compile('[a-z]+')
m=p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
m=p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
p=re.compile('a.b',re.DOTALL)
m=p.match('a\nb')
print(m)
p=re.compile('[a-z]',re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
p=re.compile("^python\s\w+",re.MULTILINE)
data="""python one
life is too short
python two
you need python
python three"""
print(p.findall(data))
p=re.compile('(ABC)+')
m=p.search('ABCABCABC OK?')
print(m)
print(m.group(0))
p=re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")
print(m.group(0))
p=re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
print(m.group(2))
p=re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())
p=re.compile(r"(?P<name>\w+)\s+((\d)+[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
print(m.group("name"))
p=re.compile(".+:")
m=p.search("http://google.com")
print(m.group())
p=re.compile('(blue|white|red)')
print(p.sub('colour','blue socks and red shoes'))

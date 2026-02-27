Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name="Batman"
type(batman)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(batman)
NameError: name 'batman' is not defined
type(name)
<class 'str'>
str()
''
int()
0
fl=7.89
type(fl)
<class 'float'>
float()
0.0
f=.4
f
0.4
g=6.
g
6.0
h=.
SyntaxError: incomplete input

================================ RESTART: Shell ================================
img=2+3j
img
(2+3j)
type(img)
<class 'complex'>
complex()
0j
t=True
f=False
type(t)
<class 'bool'>
bool()
False

================================ RESTART: Shell ================================
intg1, intg2 = 1,2
fl1, fl2 = 2.,4.6
comp1, comp2 = 2+5j, 3+9j
boo1,boo2 = True, False
type(intg1)
<class 'int'>
type(fl2)
<class 'float'>
type(comp1)
<class 'complex'>
type(boo2)
<class 'bool'>
bool()
False
complex()
0j
float()
0.0
int()
0

================================ RESTART: Shell ================================
val = abs(80-765)
val
685
685
685
a=round(7)
a
7
b=round(14.3456,2)
b
14.35
sum([10,20,34])
64
u=round(1999, -2)
u
2000
v=round(1234, -1)
v
1230
g="it's tuesdAY"
G
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    G
NameError: name 'G' is not defined. Did you mean: 'g'?
g
"it's tuesdAY"
f='you're'
SyntaxError: unterminated string literal (detected at line 1)
print(g)
it's tuesdAY
essay=" gggggggggggg hhhhhhhhhhhhhh lllllllllllllllll
SyntaxError: incomplete input
essay="'ffffffffff ggggggggggggg ddddddddddd
SyntaxError: incomplete input
essay=''' hy  sgyftad hebfuagfbakuefj
wbhfjfvwjhvfwhjfvwjcfh
wkfhgfjhfj'''
essay
' hy  sgyftad hebfuagfbakuefj\nwbhfjfvwjhvfwhjfvwjcfh\nwkfhgfjhfj'
print(essay)
 hy  sgyftad hebfuagfbakuefj
wbhfjfvwjhvfwhjfvwjcfh
wkfhgfjhfj

================================ RESTART: Shell ================================
name="Garyy"
len(name)
5
nm="Garry G"
len(nm)
7
nm[6]
'G'
nm[-2]
' '
intro="I am Ishika"
len(intro)
11
intro.index('a')
2
i=intro.index('a')
intro.index('a', i+1)
10
s="Hello this is your Python class"
idx=intro.index('y')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    idx=intro.index('y')
ValueError: substring not found
idx=s.index('y')
nxtidx=s.index('y', idx+1)
idxy=s.index('y', nxtidx+1)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    idxy=s.index('y', nxtidx+1)
ValueError: substring not found

================================ RESTART: Shell ================================
s="Hello this is your Python class everyone"
idx=s.index('o')
nxtidx=s.index('o', idx+1)
idxo=s.index('o', nxtidx+1)
idxo
23
s.count('o')
4
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
s="hi"
s
'hi'
id(s)
2314294798064
s="hello"
id(s)
2314337290544
name="Garry"
name[-4]
'a'
adr="House 20, Block 30, AC Colony, X City, Y State"
adr[round((len(adr)-1)/2)]
' '
adr[(len(adr)-1)//2]
' '

================================ RESTART: Shell ================================
ls=[a,1,w,?]
SyntaxError: invalid syntax
ls=[q,w,e,r,t]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    ls=[q,w,e,r,t]
NameError: name 'q' is not defined
type(ls)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    type(ls)
NameError: name 'ls' is not defined
ls=[o,p,f]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    ls=[o,p,f]
NameError: name 'o' is not defined
ls=[1,2,3,4]
type(ls)
<class 'list'>

================================ RESTART: Shell ================================
ls=['Ishika', '22BCON', 22, '12/11/2003']
ls[1]
'22BCON'
ls[1]='22BCON1055'
LS
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    LS
NameError: name 'LS' is not defined. Did you mean: 'ls'?
ls
['Ishika', '22BCON1055', 22, '12/11/2003']
l=[100, 200, 'Hi', 'Hello', False]
l[2][1]
'i'
>>> ls.append('Ashish')
>>> ls
['Ishika', '22BCON1055', 22, '12/11/2003', 'Ashish']
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
================================ RESTART: Shell ================================
>>> s="Python is not easy"
>>> s['e']
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s['e']
TypeError: string indices must be integers, not 'str'
>>> s[-4]
'e'
>>> s[11]
'o'
>>> s[10]
'n'
>>> s.count('o')
2
>>> s[3][1]
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s[3][1]
IndexError: string index out of range
>>> s[2][1]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    s[2][1]
IndexError: string index out of range
>>> s[0][2][1]
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    s[0][2][1]
IndexError: string index out of range
s[0].count('o')
0

================================ RESTART: Shell ================================
t=1,3,4,4,4,5,,6,7
SyntaxError: invalid syntax
t=1,2,3,4,5,6,7
t
(1, 2, 3, 4, 5, 6, 7)
type(t)
<class 'tuple'>
tuple()
()
ls=['w']
type(ls)
<class 'list'>
tp=('i')
type(tp)
<class 'str'>
tp=('i' ,)
type(tp)
<class 'tuple'>
 dir(tuple)
 
SyntaxError: unexpected indent
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
tup=('Name', 23, '01/01/2001', '22bcon1234')
tup.index(23)
1
tup[0]='Ishikaa'
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    tup[0]='Ishikaa'
TypeError: 'tuple' object does not support item assignment
tt=('Ishikaa', 23)
tt[1].count('a')
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    tt[1].count('a')
AttributeError: 'int' object has no attribute 'count'
tt[0].count('a')
2

================================ RESTART: Shell ================================
setS = {[1,2,3],1}
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    setS = {[1,2,3],1}
TypeError: unhashable type: 'list'
setS={1.2.3.4.5}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
setS={1,2,3,4}
setS
{1, 2, 3, 4}
setS
{1, 2, 3, 4}
setS[1]
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    setS[1]
TypeError: 'set' object is not subscriptable
print(setS)
{1, 2, 3, 4}
setS={'hi','hello',23,2+3j,9.99}
setS
{23, 9.99, (2+3j), 'hello', 'hi'}
setS
{23, 9.99, (2+3j), 'hello', 'hi'}
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
setS.add(5+6j)
setS
{(5+6j), 23, 9.99, (2+3j), 'hello', 'hi'}
setS.remove(2+3j)
setS
{(5+6j), 23, 9.99, 'hello', 'hi'}
setS.pop()
(5+6j)
setS
{23, 9.99, 'hello', 'hi'}
setS
{23, 9.99, 'hello', 'hi'}
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d={1:'garry', 2:23}
d.get(1)
'garry'
d[1][1]
'a'
d[1]='Garry'
d[1]
'Garry'
d[3]='JU'
d
{1: 'Garry', 2: 23, 3: 'JU'}
d.pop(2)
23
d
{1: 'Garry', 3: 'JU'}

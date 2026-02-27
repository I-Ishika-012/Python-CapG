Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[10, 2j, "Python",[2+5j,11, 22.22]]
b="Python is hard as well as easy"
l=["Python","Is", "Not","Easy"]
a[2]
'Python'
b[5][1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b[5][1]
IndexError: string index out of range
b[4][0]
'o'
l[2][1]
'o'
b[18]
'w'
b.split()[4][0]
'w'

==================================== RESTART: Shell ====================================
#Day #
#Day 3
#SLICING
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = "Python"
p[3:5]
'ho'
l[::]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
p[::-1]
'nohtyP'
p[3:5:1]
'ho'
p[::2]
'Pto'
p[::-2]
'nhy'
p[3::]
'hon'
p[3:]
'hon'
p[:]
'Python'
nm="Ishika Dutta"
nm[:6:-1]
'attuD'
nm[0:6:-1]
''
nm[0:5:-1]
''
nm[0][::-1]
'I'
nm[0][0:6]
'I'
nm[0][0:6:-1]
''
n=nm.split()[::-1]
n
['Dutta', 'Ishika']
nm[6::-1]
' akihsI'
nm[1::]
'shika Dutta'
nm[1::2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
nm[1::2]
'siaDta'
nm[::2]
'Ihk ut'
nm[11:6:-1]
'attuD'
nm[-1:6:-1]
'attuD'
#typecasting
tup=([1,2,3],'q','w')
tup[0][1]=22
tup
([1, 22, 3], 'q', 'w')
tup.remove([1,22,3])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tup.remove([1,22,3])
AttributeError: 'tuple' object has no attribute 'remove'

==================================== RESTART: Shell ====================================
str='90'
num=int(str)
type(num)
<class 'int'>
num
90
floating=float(num)
floating
90.0
comp=complex(floating)
comp
(90+0j)
bool(comp)
True
#bool is also an ibuilt fn
# true for non default
b=1.23
int(b)
1
str(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    str(b)
TypeError: 'str' object is not callable

==================================== RESTART: Shell ====================================
b=1.23
str(b)
'1.23'
int(b)
1
complex(b)
(1.23+0j)
bool(b)
True

==================================== RESTART: Shell ====================================
c=10+4j
int(c)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+4j)'
bool(c)
True

==================================== RESTART: Shell ====================================
f=False
str(f)
'False'
int(f)
0
float(f)
0.0
bool(f)
False
complex(f)
0j

==================================== RESTART: Shell ====================================
s="Ishika"
bool(s)
True
int(s)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'Ishika'
dict(s)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
list(s)
['I', 's', 'h', 'i', 'k', 'a']
tuple(s)
('I', 's', 'h', 'i', 'k', 'a')
set(s)
{'h', 'a', 'k', 's', 'I', 'i'}
st='12345'
int(st)
12345
float(st)
12345.0
st='2.6'
int(st)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    int(st)
ValueError: invalid literal for int() with base 10: '2.6'
float(st)
2.6
ls=['q','w',1,2,3]
bool(ls)
True
tuple(ls)
('q', 'w', 1, 2, 3)
set(ls)
{1, 2, 3, 'w', 'q'}
dict(ls)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dict(ls)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l=['Hi', [2,20], 'To', ['Hi', 'Hello']]
dict(l)
{'H': 'i', 2: 20, 'T': 'o', 'Hi': 'Hello'}
>>> t=(1,2,3,4,hi)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    t=(1,2,3,4,hi)
NameError: name 'hi' is not defined
>>> t=(1,2,3,"hi")
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> tt=(11,22,33,"Hi")
>>> dict(tt)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    dict(tt)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> 
==================================== RESTART: Shell ====================================
>>> s={"Hi", "Yo", {2,3}, {'JU', "PU"}}
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    s={"Hi", "Yo", {2,3}, {'JU', "PU"}}
TypeError: unhashable type: 'set'
>>> s={"Hi", "Yo", (2,3), ('JU', "PU")}
>>> dict(s)
{2: 3, 'JU': 'PU', 'Y': 'o', 'H': 'i'}
>>> d={'name':'Ishika', 'age':23, 'dob':'12/1/2003'}
>>> tuple(d)
('name', 'age', 'dob')
>>> str(d)
"{'name': 'Ishika', 'age': 23, 'dob': '12/1/2003'}"
>>> list(d)
['name', 'age', 'dob']
>>> list(d.items())
[('name', 'Ishika'), ('age', 23), ('dob', '12/1/2003')]
>>> list(d.values())
['Ishika', 23, '12/1/2003']
>>> 
==================================== RESTART: Shell ====================================
>>> #gen copy
>>> a=10
>>> b=a //general copy
SyntaxError: incomplete input
>>> b=a #general copy
>>> #copies the content of var space in var space

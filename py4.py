Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[20,30,40]
id(l)
2711482768256
l2=l
id(l2)
2711482768256
id(l)==id(l2)
True
l2[1]=200
l
[20, 200, 40]
l[1]=30
l2
[20, 30, 40]
l3=l.copy();
id(l3)
2711482770304
l3[1]=300
l3
[20, 300, 40]
l
[20, 30, 40]
l4=[10,20,30,[40, 50, 60]]
l5=l4.copy()
l5[3][2]=600
l5
[10, 20, 30, [40, 50, 600]]
l4
[10, 20, 30, [40, 50, 600]]
l5[3][3]=[70,80]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l5[3][3]=[70,80]
IndexError: list assignment index out of range
l5[3].append([70,80])
l5
[10, 20, 30, [40, 50, 600, [70, 80]]]
l5[3][3].append(90)
l5
[10, 20, 30, [40, 50, 600, [70, 80, 90]]]
l4
[10, 20, 30, [40, 50, 600, [70, 80, 90]]]
import Copy
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import Copy
ModuleNotFoundError: No module named 'Copy'
import copy
l6=copy.deepcopy(l5)
l6
[10, 20, 30, [40, 50, 600, [70, 80, 90]]]
l6[4]=100
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l6[4]=100
IndexError: list assignment index out of range
l6[4].aqpend(100)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l6[4].aqpend(100)
IndexError: list index out of range
l6[4].append(100)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l6[4].append(100)
IndexError: list index out of range
l6.append(100)
l6
[10, 20, 30, [40, 50, 600, [70, 80, 90]], 100]
l5
[10, 20, 30, [40, 50, 600, [70, 80, 90]]]

==================================== RESTART: Shell ====================================
a,b=2,3
a+b
5
a-b
-1
a*b
6
a/3
0.6666666666666666
a//b
0
a%b
2
a**3
8
c,d=10.99,4.56
c+d
15.55
c-d
6.430000000000001
c*d
50.114399999999996
c/d
2.4100877192982457
c//d
2.0
c%d
1.870000000000001
a+c
12.99
s="hi"
l=['q'.'w']
SyntaxError: invalid syntax
l='q'.'w']
SyntaxError: unmatched ']'
l=['w']
s+l
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s+l
TypeError: can only concatenate str (not "list") to str
3+26j/4j
(9.5+0j)
3+2j//9j
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    3+2j//9j
TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
10 and 40
40
10 OR 40
SyntaxError: invalid syntax
10 or 40
10
0 or 40
40
0 and 40
0
bool(4)
True
bool(9.0)
True
bool(9+0j)
True
bool('hi')
True
>>> bool([8])
True
>>> bool((7))
True
>>> bool({1:2})
True
>>> not True
False
>>> 100 and []
[]
>>> 100 and [] or '' and []
''
>>> 1!=2
True
>>> Y=7
>>> Y+=8
>>> Y
15
>>> Y-=5
>>> Y
10
>>> Y*=5
>>> Y
50
>>> Y/=5
>>> Y
10.0
>>> Y//=5
>>> Y
2.0
>>> Y%=2
>>> Y
0.0
>>> +69
69
>>> 'abc'=='Abc'
False
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    ord(a)
TypeError: ord() expected string of length 1, but int found
>>> ord('a')
97
>>> ord('A')
65

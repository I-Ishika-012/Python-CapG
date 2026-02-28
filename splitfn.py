#input
l=['p1.py','p2.py','p3.txt','p4.py','p5.txt','p6.com']
#output
{'py': ['p1.py', 'p2.py', 'p4.py'], 'txt': ['p3.txt', 'p5.txt'], 'com': ['p6.com']}
d={}
for i in l:
    ext=i.split(".")[-1]
    if ext in d:
        d[ext].append(i)
    else:
        d[ext]=[i]
print(d)

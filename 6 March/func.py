'''Global / Local Variables'''
a=90

def fun():
    a=100
    print("Inside function a=",a)
fun()
print("Outside function a=",a)

#changing global variable a from inside function
def fun1():
    global a
    a=100
    print("Inside function a=",a)
fun1()
print("Outside function a=",a)

#changing outer scope var in a nested function
def fun2():
    a=90
    print("Inside function 2 a=",a)
    def fun3():
        nonlocal a
        a=100
        print("Inside function 3 a=",a)
    fun3()
    print("Inside function 2 a=",a)
fun2()

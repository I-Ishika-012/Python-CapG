'''
inheritance
1. single inheritance
2. multiple inheritance 
3. multilevel inheritance
'''
# single inheritance
# class A:
#     def __init__(self):
#         print("Class A")
# class B(A):
#     def __init__(self):
#         print("Class B")
#         super().__init__()
        
# obj = B()


# multiple inheritance
class A:
    def __init__(self):
        print("Class A")
class B:
    def __init__(self):
        print("Class B")
class C(A,B):
    def __init__(self):
        print("Class C")
        super().__init__()
        
obj = C()
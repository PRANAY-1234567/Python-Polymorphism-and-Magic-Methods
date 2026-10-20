'''class Point:
    def __init__(self, Pages):
        self.p = Pages

a=Point(100)
b=Point(200)
Traceback (most recent call last):
  File "d:\Python\7) Qspider\OOPS\Polymorphism\Oerator Overloading\operator.py", line 7, in <module>
    print(a+b)
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
'''

#Magic Method or Dunder Method
'''class Operation:
    def __init__(self, book):
        self.b = book

    def __add__(self, other):
        return self.b + other.b
a=Operation(100)
b=Operation(200)
print(a+b)'''

'''class Operation:
    def __init__(self, book):
        self.b = book

    def __add__(self, other):
        print(self.b + other.b)
a=Operation(100)
b=Operation(200)
a+b'''


'''class Operation:
    def __init__(self, book):
        self.b = book

    def __add__(self, other):
        return Operation(self.b + other.b)

#If U want to convert object data addreee to readable format then use __str__ or __repr__{self.b}
    # def __str__(self):
    #     return f'{self.b}'

    def __repr__(self):
        return f'{self.b}'
        
a=Operation(100)
b=Operation(200)
print(a+b)'''

'''class Data:
    def __init__(self,a):
        self.a = a

    def __sub__(self, other):
        return Data(self.a - other.a)

    def __str__(self):
        return f'{self.a}'

d=Data(12)
d1  = Data(10)
print(d-d1)'''

'''class AllOperation:
    def __init__(self,a,b):
        self.a = a
        self.b= b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b

    def __truediv__(self, other):
        return self.a / other.a, self.b / other.b
        

x=AllOperation(100,200)
y=AllOperation(50,100)
print(x+y)
print(x-y)
print(x*y)
print(x/y)'''

#Greater than an d lessthan
class AllOperation:
    def __init__(self,a,b):
        self.a = a
        self.b= b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b

    def __truediv__(self, other):
        return self.a / other.a, self.b / other.b
        
    def __gt__(self, other):
        return self.a >  other.a, self.b > other.b

    def __lt__(self, other):
        return self.a <  other.a, self.b < other.b
    
    def __eq__(self, other):
        return self.a ==  other.a, self.b == other.b
    
    def __pow__(self, power):
        return self.a **  power.a, self.b ** power.b
    
x=AllOperation(1,3)
y=AllOperation(6,2)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x>y)
print(x<y)
print("Equal To", x==y)
print("Power Factor", x**y)

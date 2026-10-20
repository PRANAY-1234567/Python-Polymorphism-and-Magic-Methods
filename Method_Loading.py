# Method Overloading
#It will happen in single class
# Developing a multiple methood with same name and 
# variation in the argument but even thoug it will execute latest one

'''class Information:
    def data (self,x):
        print(x)

    def data (self,x,y):
        print(x,y)
    def data (self,x,y,z):
        print(x,y,z)

i = Information()
i.data(30,34,65)
i.data("Hii",[1,2,3],45)'''

'''class Information:
    def data (self,x):
        print(x)

    def data (self,x,y):
        print(x,y)
    def data (self,x=0,y=0,z=0):
        print(x,y,z)

i = Information()
# i.data(30,34,65)
# i.data("Hii",[1,2,3],45)
i.data(12)
i.data(12,23)'''
"""
class Information:
    def data (self,x):
        print(x)

    def data (self,x,y):
        print(x,y)
    def data (self,*args):
        print(args)

i = Information()
# i.data(30,34,65)
# i.data("Hii",[1,2,3],45)
i.data(12)
i.data(12,23)"""
"""i.data()"""

#Variable Keyword argument

"""class Information:
    def data (self,x):
        print(x)

    def data (self,x,y):
        print(x,y)
    def data (self,**kwargs):
        print(kwargs)

i = Information()
i.data()
i.data()"""

"""
We can achieve Method Overloading by 3 ways
Default Parameters
Variable Keyword Argument
Variable Positional Arguments"""

#Constructor Overloading

'''class Dim:
   def __init__(self):
       print("constructor1")


   def __init__(self, a):
       print("constructor2")


   def __init__(self,a=None ,b=None):
       print("constructor3")


d = Dim(10) '''



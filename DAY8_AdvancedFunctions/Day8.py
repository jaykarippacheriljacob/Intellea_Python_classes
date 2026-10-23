#local scope 
'''
def student():
    name = "John"
    print("student name",name)
student()


# Global variable 

s = "manoj"
def student(): 
    name = "John"
    print("student mname",name)
student()

'''
#*args

'''def generate_sum(*num):
    return sum(num)
print(generate_sum(11,12,45,6.3))

#**kwargs

def addition(**num):
    for key, value in num.items():
        print(key,value)
addition(a=10,b=20,c=30,d=40)


def student(*detail,**info):
    print(detail)
    print(info)
student("manoj","kumar",age = 22 , cit = "chennai", country = "India")



discount = lambda price : price * 0.50
print(discount(100000))


square = lambda x :  x*x
print(square(5)) #25

add = lambda a , b : a +b
print(add(10,20))


a = int(input("enter the a value: "))
b = int(input("enter the b value: "))
c= int(input("enter the c value: "))

large = lambda a , b , c : a if ( a > b and a > c ) else (b if b >c else c)
print("largest number ", large(a,b,c))

'''

def fibo(n):
    if n <= 1:
       return n 
    else:
       return fibo(n-1) + fibo(n - 2)

terms = int(input("enter the terms :"))

for i in range(terms):
   print(fibo(i), end =" ")

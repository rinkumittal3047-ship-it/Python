# function: to make code easier
def greet(name): # name is parameter
     print("hello",name)
     print("welcome to python")
greet("rinku")  #function call
greet("mahak")  #mahak is argument

def say_hello():
     print("hello!")
say_hello()

def addition(a,b):
     print("sum",a+b)
addition(10,20)

def student_name(name,age,grade):
     print("name:",name)
     print("age:",age)
     print("grade:",grade)
student_name("rinku",19,"BCA")

# default parameter have predefined value
# if Python
def function(a,b,c=10):
     print(a,b,c)
     function(a=5,6)

def calculate(a,b):
  print(a+b)
  print(a-b)
  print(a*b)
  return a+b,a-b,a*b
value=calculate(6,5)
print(value)


def show(a,b=3):
     a=a+b
     b=a*b
     return a,b
x,y=show((4))
print(x+y)

def f(x=2,y=3):
    return x+y
print(f(5))

def g(items):
    return [x*x for x in items if x % 2==0]
print(g([1,2,3,4]))

def greet(name):
    print("Hello", name)
    # return name
result = greet("Riya")
print(result) 

def calculate(a, b):     
    print(a + b)    
    return a * b  
result = calculate(3, 4) 
print(result) 

def test():     
    return 5  
    print(10)   
# print(10) 
print(test())

print(10) 
def total(a, b=5, c=2):     
    return a + b * c  
print(total(3))

def total(a, b=5, c=2): 
    return a + b * c 
print(total(3, 4,)) 

def total(a, b=5, c=2):
  return a + b * c 
print(total(c=3, a=2))

def display(a,b,c=10):
  print(a,b,c)
display(1,c=3,b=2)

# def display(a,b):
#     print(a,b)
# display(a=10,20)
    
def display(a,b):
    print(a,b)
display(10,b=20)

def calculate(a,b):
    return a+b,a-b
result=calculate(8,3)
print(result)

def calculate(a,b):
    return a+b,a-b
x,y=calculate(8,3)
print(x*y)

def calculate( ):
    return 10,20,30
a,b=calculate()
print(a,b)

def greet(): 
    return "Hello" 
print(greet()) 

# def calculate_total(): return 100
# def _calculate(): return 100 
# def calculate2(): return 100
# def 2calculate(): return 100 

# def student(name="Guest", age):
#      print(name, age) 

def one():     
    return 1 
def increase(number):    
    return number + 1 
print(increase(increase(one()))) 


def check(number):    
     if number > 0:        
         return "Positive"     
     return "Non-positive"
print(check(6)) 

def first_even(numbers):    
    for number in numbers:      
     if number % 2 == 0:             
      return number      
    return None 
print(first_even([1, 3, 6, 8])) 

def calculate(number): 
    return number + 1
print(calculate(calculate(2)) + calculate(1)) 

def message():
     return print("Python") 
value= message()
print(value) 
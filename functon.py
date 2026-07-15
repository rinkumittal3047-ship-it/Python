# # function: to make code easier
# def greet(name): # name is parameter
#      print("hello",name)
#      print("welcome to python")
# greet("rinku")  #function call
# greet("mahak")  #mahak is argument

# def say_hello():
#      print("hello!")
# say_hello()

# def addition(a,b):
#      print("sum",a+b)
# addition(10,20)

# def student_name(name,age,grade):
#      print("name:",name)
#      print("age:",age)
#      print("grade:",grade)
# student_name("rinku",19,"BCA")

# # default parameter have predefined value
# # if Python
# # def function(a,b,c=10):
# #      print(a,b,c)
# #      function(a=5,6)

# def calculate(a,b):
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   return a+b,a-b,a*b
# value=calculate(6,5)
# print(value)


# def show(a,b=3):
#      a=a+b
#      b=a*b
#      return a,b
# x,y=show((4))
# print(x+y)

# def f(x=2,y=3):
#     return x+y
# print(f(5))

# def g(items):
#     return [x*x for x in items if x % 2==0]
# print(g([1,2,3,4]))

# def greet(name):
#     print("Hello", name)
#     # return name
# result = greet("Riya")
# print(result) 

# def calculate(a, b):     
#     print(a + b)    
#     return a * b  
# result = calculate(3, 4) 
# print(result) 

# def test():     
#     return 5  
#     print(10)   
# # print(10) 
# print(test())

# print(10) 
# def total(a, b=5, c=2):     
#     return a + b * c  
# print(total(3))

# def total(a, b=5, c=2): 
#     return a + b * c 
# print(total(3, 4,)) 

# def total(a, b=5, c=2):
#   return a + b * c 
# print(total(c=3, a=2))

# def display(a,b,c=10):
#   print(a,b,c)
# display(1,c=3,b=2)

# # def display(a,b):
# #     print(a,b)
# # display(a=10,20)
    
# def display(a,b):
#     print(a,b)
# display(10,b=20)

# def calculate(a,b):
#     return a+b,a-b
# result=calculate(8,3)
# print(result)

# def calculate(a,b):
#     return a+b,a-b
# x,y=calculate(8,3)
# print(x*y)

# def calculate( ):
#     return 10,20,30
# a,b=calculate()
# print(a,b)

# def greet(): 
#     return "Hello" 
# print(greet()) 

# # def calculate_total(): return 100
# # def _calculate(): return 100 
# # def calculate2(): return 100
# # def 2calculate(): return 100 

# # def student(name="Guest", age):
# #      print(name, age) 

# def one():     
#     return 1 
# def increase(number):    
#     return number + 1 
# print(increase(increase(one()))) 


# def check(number):    
#      if number > 0:        
#          return "Positive"     
#      return "Non-positive"
# print(check(6)) 

# def first_even(numbers):    
#     for number in numbers:      
#      if number % 2 == 0:             
#       return number      
#     return None 
# print(first_even([1, 3, 6, 8])) 

# def calculate(number): 
#     return number + 1
# print(calculate(calculate(2)) + calculate(1)) 

# def message():
#      return print("Python") 
# value= message()
# print(value) 

#variable  length argument (*args)
# def add_numbers(*numbers):
#     total=0
#     for num in numbers:
#      total+=num
#     return total
# print(add_numbers(10,20))
# print(add_numbers(5,10,15,20))

# def show_name(greet,*names):  # positional argument store one *
#     for name in names:
#      print(greet,name)
# show_name("Hello","Aman","Riya","Karan")   

# def show_value(greet,*values):
#   for num in values:
#     print(greet, num)
# show_value("present",24,26,17,18)

# # keyword argument store (**)
# def show_details(**details):
#   for key,values in details.items():
#     print(key,values)
# show_details(name="rinku",age=21,city="delhi")

# def create_profile(**user):
#   print("user profile")
#   print("Name:",user.get("name"))
#   print("age:",user.get("age"))
#   print("email:",user.get("email"))
# create_profile(name="rinku",age=19,email="rinku@123")

# # global variable:
# count=0

# def increase():
#   global count
#   count+=1
# increase()
# increase()
# print(count)

# # local variable
# language="python"
def subject():
   language="python"
   return language
print(subject())
    


# def square(number):
#   return number*number
# print(square(5))
# print(square.__doc__)   # used for code documentation(__) (double underscore)

# # type hint: show what type of data a function expects and return
# # -> int means the funtion is in which datatype
# def add(a: int,b:int)->int:
#   return a+b
# print(add(10,20))

# # lambda function: it is a function works in small anonymous function.
# # it usually used for short operations
# # syntax : lambda function:expression

# square=lambda x: x*x
# print(square(6))

# add=lambda a,b : a+b 
# print(add(4,9))

# map(), filter(),sorted()

# using function with lists
# # find largest number
# marks=[12,23,34,14,3,54]
# def find_largest(numbers):
#     largest=numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest=number
#     return largest
# print(find_largest(marks))

# # smallest number access 
# marks=[12,23,34,14,3,54]
# def find_smallest(numbers):
#     smallest=numbers[0]
#     for number in numbers:
#         if number < smallest:
#             smallest=number
#     return smallest
# print(find_smallest(marks))

# function calling another function

# def get_square(number):
#     return number*number
# def print_square(number):
#     result=get_square(number)
#     print("square",result)
# print_square(7)

# nested function
# def outer_function():
#     print("this is outer function")
#     def inner_function():
#         print("this is inner function")
#     inner_function()
# outer_function()

# recurssion

# def factorial(n):
#     if n==0: #or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(5))

 












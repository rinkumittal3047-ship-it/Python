# def calculate(a,b=5):
#     return a+b,a*b
# x,y=calculate(4)
# print(x,y)
# print(calculate(4,2)[1])

# def display(a,b,c=10):
#     print(a,b,c)
# display(1,c=3,b=2)
# display(4,5)

# def calculate(number):
#     if number%2==0:
#         return number//2
#     print("odd number")
#     return number*3
# print(calculate(8))
# print(calculate(5))

# def add_item(item,container=[]):
#     container.append(item)
#     return container
# print(add_item(1))
# print(add_item(2))
# print(add_item(3,[]))
# print(add_item(4))    

# def analyse(first,*values):
#     return first,max(values),sum(values[::2])  #:: means reverse the string
# print(analyse(10,3,8,5,2))

# def build_record(**data):
#     data["total"]=sum(
#         value
#         for value in data.values()
#         if isinstance(value,int)
#         )
#     return sorted(data.items())
# print(build_record(a=2,b=3,name="x"))

# def calculate(a,b,c):
#     return a+b*c
# values=(2,3)
# options={"c":4}
# print(calculate(*values,**options))

# def report(name,*,score=0,passed=True):
#     return f"{name}:{score}:{passed}"
# print(report("riya",score=88))
# print(report("kabir",passed=False,score=40))

# def change(number):
#     number+=10
#     return number
# value=5
# print(change(value),value)

# def update(data):
#    data[(0)]+=5
#    data.append(sum(data))
# numbers=[1,2,3]
# update(numbers)
# print(numbers)

# def update(data):
#     data=data+[4]
#     data[0]=99
#     return data
# numbers=[1,2,3]
# new_numbers=update(numbers)
# print(numbers)
# print(new_numbers)

# def update(record):
#     record["b"]=record.get("b",0)+2
#     record={"c":3}
#     return record
# data={"a":1,"b":4}
# result=update(data)
# print(data)
# print(result)

# def modify(data):
#     data[1].append(30)
#     return data+("done",)
# values=(10,[20])
# result=modify(values)
# print(values)
# print(result)

# x=10
# def outer():
#     x=20
#     def inner():
#         global x
#         x+=5
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

# def outer():
#     number=1
#     def inner():
#         nonlocal number
#         number*=3
#         return number
#     print(inner(),inner())
# outer()

# def create_power(exponent):
#     def calculate(number):
#         return number**exponent
#     return calculate
# square=create_power(2)
# cube=create_power(3)
# print(square(4)+cube(2))

# functions=[]
# for number in range(3):
#     functions.append(lambda:number)
#     print([function() for function in functions])

#     def apply(function,values):
#         return[
#             function(value)
#             for value in values
#             if function(value)>5
#         ]
#     def transform(number):
#         return number*number-1
#     print(apply(transform,[1,2,3,4]))

# numbers=[1,2,3,4,5]
# result=list(
#      map(
#         lambda number:number*2,
#         filter(lambda number:number%2==1,numbers)
#     )
# )
# print(result)

# def adda(a,b):
#     return a*b
# def multiply(a,b):
#     return a+b
# operations={
#     "addition": add,
#     "multiplication":multiply
# }
# result=(
#     operations["addition"](2,3)
#     +operations["multiplication"](2,3)
# )        
# print(result)

# def calculate(number):
#     if number<=1:
#         return 1
#     return number + calculate(number-2)
# print(calculate(6))

# def trace(number):
#     if number==0:
#         return 
#     print(number,end=" ")
#     trace(number-1)
#     print(number,end=" ")
# trace(3)

# def flatten(data):
#     result=[]
#     for item in data:
#         if isinstance(item,list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#         return result
#     values=[1,[2.[3,4]],5]
#     print(flatten(values))

def sequence(number):
    while number>0:
        yield number
        number-=2
result=sequence(5)
print(next(result))
print(list(result))

def increase(function):
    def wrapper(number):
        return function(number)+1
    return wrapper
@increase
def square(number):
    return number*number
print(square(4))


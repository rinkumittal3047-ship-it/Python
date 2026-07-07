# Create variables to store:
# Print all values and their data types.

name="rinku"
age=19
height=5.2
student_status=True
print(name,age,height,student_status)

# Swap two numbers without using a third variable.
a=10
b=20
a,b=b,a
print(" a =",a,"b =",b)


# Find the type of these values:
print(type(25))
print(type(25.5))
print(type("25"))
print(type((True)))
print(type([1,2]))
print(type((1,2)))
print(type({1,2}))
print(type({"a":1}))

# Take your full name and print:

name="rinku mittal"
print("first character:",name[0])
print("last character:",name[-1])
print(len(name))
print(name.upper())
print(name.lower())

# Reverse a string using slicing.
student=("rinku mittal")
print(student[::-1])

# Count how many times "a" appears in a string.
course="python programming"
count=course.count("a")
print("number of 'a':",count)

# replace every space with _
text="i am rinku"
result=text.replace(" ","_")
print(result)      

numbers=[10,20,30,40,50]

# Print: First element, Last element, Middle element
num=[12,23,26,74,38]
print(num[0])
print(num[-1])
print("middle number:" ,num[len(numbers)//2])

# Add 100 at the end of the list
number=[12,24,35,47]
number.append(26)
print(number)

t=(5,10,15,20,25)

# Print: First element, Last element, Length
t1=(24,12,26,37,87)
print(t1[0])
print(t1[-1])
print(len(t1))

# Print: Union, Intersection
A={1,2,3,4}
B={3,4,5,6}
C=B.union(A)
print(C)

C=A.intersection(B)
print(C)

# Print: Keys,Values, Items
student={
    "name":"rinku",
    "age":19,
    "height":5.2,
}
print(student.keys())
print(student.values())
print(student.items())

# Remove duplicates from a list using a set.
list2=[12,23,34,45,26,12,26,17,23,84,94,12]
list1=set(list2)
print(list1)

# Convert tuple into list and add one element
max=(12,23,43,45,67,32,75)
max1=list(max)
print(max1)
max1.insert(2,15)
print(max1)

# Capitalize first letter of every word.
message=("hello this is python language.")
print(message.title())
print(message.upper())

# Merge two lists
d=[12,34,26,]
p=[23,45,76]
b=d+p
print(b)


age=18        
 #if statement:
 
if age>=18:
        print("you are an adult")
print("you are not adult")
 
# if else statement:
a=10
b="10"
if a==b:
          print("a is equal to b")
          print("a qual to b")
else:
       print("a is not equal to b")

# nested if statement:
num=20
number=True
if num>=25:
    if number:
     print("num access")
    else:
       print("check number")
else:
   print("less number")

#elseif statement
score=75
if score>=90:
   print("grade:A")
elif score>=80:
   print("grade:B")
elif score>=70:
   print("grade:C")
else:
   print("grade:f")      

# airthmetic operators
a=20
b=10
print("Additon:",a+b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor division:",a//b)
print("modulus:",a%b)
print("power",a**b)

# relational operators
p=20
r=15
print(p==r)   #equal to 
print(p!=r)   #not equal to
print(p>r)    #greater than
print(p<r)    #less than
print(p>=r)    #greater than equal to
print(p<=r)    #less than equal to

# assignment operators
x=20

x+=15     #addition assignment operator
print(x) 
x-=10    #subtraction asssignment operator
print(x) 
x*=10     #multipliction assignment operator
print(x)
x/=2      #division assignment operator
print(x)

# logical operators
i=20
j=10
print(i<j and i>15)    #add operator
print(i>j or i>12)     #or operator
print(not(i<j))        #not operator

# identity operator
k=[1,2]
h=k
t=[1,2]
print(k is h)   #same operator
print(k is t)   #same operator 
print(h is not t )  #different operator

# membership operator
fruits=["apple","banana","orange","mango"]
print("mango" in fruits)    #exist in list
print("litchi" not in fruits)  #not exist in list

# bitwise operators
a1=12
b1=26
print(a1 & b1)    #and operator
print(a1 ^ b1)    #xor operator
print(a1 << b1)   # left shift operator
print(a1 >> b1)   # right shift operator



    



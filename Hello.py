print("hello world") #Basic statements

text="rinku"  # through variable accessing
print(text)

x=10   #int value
y=20.0   #flaot value
z=40+5j  #complex value
print(type(x))   #by using type() function we can find the data type of variable
print(type(y))   
print(type(z)) 

i=complex(x)    #change one datatype into another datatype
print(i) 

a="30"   #by usimg type() functon we can find the data type of variable
print(type(a))  

y=int(a)    #change one datatype into another datatype
print(y) 
 
message="  hello world  "    #string value
print(message) 

print(len(message))  #by using len() function we can find the length of string

print(message.upper())   #by using upper() function we can convert string into upper case

print(message.lower())   #by using lower() function we can convert string into lower case

print(message.capitalize())   #by using capitalize() function we can convert first letter of string into upper case

print(message.strip())   #by using strip() function we can remove the white space from string  

print("hello" in message) # 'in' function used to check the string is present in another string or not

print("hello" not in message)   # 'not in' function used to check the string is not present in another string

print(message.replace("hello","hi"))   #by using replace() function we can replace the string with another string

if("hey" in message):               #condition statement
 print("hey is present in message")   #if statement used to check the condition
else:   
 print("hey is not present in message")   #else statement used to check the condition 

 print(message[5])    #for accessing the string we can use indexing and slicing
 print(message[3:])    #for accessing the string without explain the ending index
 print(message[:5])    #for accessing the string without explain the starting index

x=10         #global variable     #def keyword for create a fuction
def myfunction():    #create a function name
 x=20               #decalre a local variable
 print(x)        #print the local variable
myfunction()      #call function 
print(x)          #print(x)          #print the global variable

name="rinku"      #global variable
def show():        #function create
 global name        #decalre global variable
 name="abcd"       #local variable
 print(name)       #print the global variable
show()      # call function

name="rinku" ,"khusbu","dimpal"
print(name)
n1,n2,n3=name
print(n3,n1,n2)


  

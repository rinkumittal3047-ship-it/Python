#sets= unorderd, mutuable , duplicates is not allowed.
#{} is used
#sets= collection of unique values.
#sets ust be immutable, but we can add or remove items after creation.such as number, string, tuple, boolean, frozenset.

student={"amit","riya","john","amit"}
print(student)

values={12,"rinku",30.0, "True" ,1}
print(values)
print(len(values))
print(type(values))

marks=[12,13,35,57,32,95]
unique_marks=set(marks)   #by using set() function we can convert list into set
print(unique_marks)
print(type(unique_marks))

marks=(12,13,35,57,32,95)
unique_marks=set(marks)   #by using set() function we can convert tuple into set
print(unique_marks)

values.clear()
print(values)

emptyset={}
print(type(emptyset))   #by using type() function we can find the data type of variable

emptyset=set()   #by using set() function we can create empty set
print(type(emptyset))   #by using type() function we can find the data type of variable

numbers={"riyan","amit","anjali",1,True,2}
print("amit" in student)   #by using 'in' function we can check the value is present in set or not
print("riya" not in student)   #by using 'not in' function we can check the value is not present in set

for a in numbers:   #by using for loop we can access the set
 print(a)

 #//add() method is used to add a single element in set.

 skills={"python","java","c++"}
skills.add("html")   #by using add() function we can add the value in set
print(skills)

num1={1,2,3,4,5}
num2={4,5,6,7,8}
#num3=num1.union(num2)   #by using union() function we can add the value in set
#print(num3)   #print the set
num1.update(num2)   #by using update() function we can add the value in set
print(num1)   #print the set

# numbers.remove(2)   #by using remove() function we can remove the value from set
# print(numbers)

numbers.discard(8)   #by using discard() function we can remove the value from set
print(numbers)

del numbers   #by using del keyword we can delete the set


#union....intersection.....update


#dictionery= store the key-value pairs. 
#key always unique and value can be duplicate.
 #dictionery is a collection which is ordered and changeable. Does not allow duplicates.

languages={
    "python":"best",
    "java":"better",
    "c++":"good",
}  
print(languages)  
print(len(languages))   #by using len() function we can find the length of dictionery

languages={
    "python":"best",
    "java":"better",
    "c++":"good",
    "python":"good",
}  
print(languages)  

values=dict()
print(type(values))   #by using type() function we can find the data type of variable
identity=dict(
    name="rinku",
    age=20,
    city="delhi",
)
print(identity)   #print the dictionery
print(type(identity))   #by using type() function we can find the data type of variable 

values=[
    ("name","rinku"),
    ("age",20),
    ("height",25.8),
    ("hobbies",("reading","writing","coding")),
    ("is_student",True)
]
values1=dict(values)
print(values1)   #print the dictionery
print(type(values1))   #by using type() function we can find the data type of variable

print(values1["name"])   #by using key we can access the value of dictionery

#if key does not exist then it will give error. To avoid this we can use get() function.

print(values1.get("email"))   #by using get() function we can access the value of dictionery

print(values1.get("email","email not found"))  
 #by using get() function we can access the value of dictionery and also we can give the default value if key does not exist.

#//add method is used to add a single element in dictionery.
student={
    "name":"rinku",
    "age":20,
}
student["city"]="delhi"   #by using key we can add the value in dictionery
print(student)   #print the dictionery

# #//update method is used to add multiple elements in dictionery.
student["age"]=21   #by using key we can update the value in dictionery
print(student)   #print the dictionery

# #//using  multiple values update method we can add multiple elements in dictionery.
student.update({               #//using update() function we can add the value in dictionery
    "city":"delhi",
    "course":"python",
})
print(student)

# #//pop method is used to remove a single element in dictionery.
removed_value=student.pop("course")   #by using pop() function we can remove the value from dictionery
print(removed_value)   #print the removed value
print(student)   #print the dictionery

student.popitem()   #by using popitem() function we can remove the last inserted value from dictionery
print(student)   #print the dictionery

student={
    
    "name":"rinku",
    "age":20,
    "city":"delhi",
    "course":"python",
}
del student["age"]   #by using del keyword we can delete the value from dictionery
print(student)
student.clear()   #by using clear() function we can remove all the values from dictionery
print(student)

print(student["age"])   #by using key we can access the value of dictionery

print(student.keys())   #by using keys() function we can access the keys of dictionery

print(student.values())   #by using values() function we can access the values of dictionery

for key, value in student.items():   #by using items() function we can access the key-value pairs of dictionery
    print(key,":", value)

for key in student:   #by using for loop we can access the keys of dictionery
    print(key)

    for values in student.values():   #by using for loop we can access the values of dictionery
        print(values)

        for key, value in student.items():   #by using for loop we can access the key-value pairs of dictionery
            print(key,":", value)

for key in student.keys():  #by using for loop we can access the keys of dictionery
    print(key)

students = {
    "student1": {
        "name": "Rinku",
        "age": 20,
        "course": "BCA"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "B.Tech"
    }
}

print(students)

print(students["student1"]["name"])   #by using key we can access the value of dictionery
print(students["student2"]["course"])   #by using key we can access the value of dictionery

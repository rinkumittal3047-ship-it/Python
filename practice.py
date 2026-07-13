# this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
# # print(this_tuple[2])
# # print(this_tuple[1:])
# print(this_tuple[-4:-1])

# values=["rinku@123","dimpal@234","rinku@123","dimpal@234"]
# a=set(values)
# print(set)
# print(a)

python={"rinku","khusbhu","dimpal","mahak",}
SQL={"mahak","jiya","rinku","dimpal",}
print(python.intersection(SQL))

identity={
    "person1": {
        "name":"rinku",
        "age":20,
        "height":5.5,
    },
    "person2": {
        "name":"priya",
        "age":21,
        "height":5.6,

    }
}
print(identity["person1"]["name"])
print(identity["person2"]["height"])

print(identity["person2"].get("course","course not found"))




# def greet(name="rinku"):
#      print("hello",name)
# greet()

# x=5
# y=6
# print(x**y)  #** means power of value

print(bool([]),bool([0]))
# false true

a=15
b=4
result= a // b
print(result)
# // divide 

s="hello"
print(s[:3],s[-2:])


a=[1,2,3,3]
b=a
b.append(4)
print(a)

d={"a":15,"b":16}
print(d.get("c",18))

for i in range(1,5,2):
    print(i,end=" ")






        


# x = 10
# x = str(x) 
# print(x * 2, type(x).__name__)

# value = "5.8"
# number = float(value) 
# print(int(number), bool(number), type(number).__name__)

# What is the output? Observe the local and global variables having the same name.
x = 10 

# def show(): 
#   x = 20 
# print(x, end=" ")
# show() 
# print(x)

# What is the output when the `global` keyword is used? c
count = 5
def update():
     global count
     count += 3
update()
print(count)

# What is the output of the indexing and slicing operations?
text = "Python" 
print(text[1], text[-1], text[1:5:2])

# What is the output after removing outer spaces and changing the letter case? 
text = " PyThOn "
clean = text.strip()
print(clean.lower(), clean.upper())

# What is the output of `replace()` and `count()`? 
text = "banana"
print(text.replace("a", "o", 2), text.count("an"))

# What is the output of `split()` and `join()`? 
text = "red,green,blue"
parts = text.split(",")
print("-".join(parts), len(parts))

# What is the output of `find()`, `startswith()` and `endswith()`?
text = "intern_python.py" 
print(text.find("python"), text.startswith("intern"), text.endswith(".py"))

# What is the output of the string validation methods? 
code = "Python3" 
year = "2026" 
print(code.isalpha(), code.isalnum(), year.isdigit())

# What is the output? 
numbers = [1, 2, 3]
numbers.append([4, 5]) 
print(numbers)

# What is the output?
numbers = [1, 2, 3]
numbers.extend((4, 5)) 
print(numbers)

# What is the output?
values = [10, 30] 
values.insert(1, 20) 
print(values)

# What is the output? 
numbers = [1, 2, 3, 2]
numbers.remove(2) 
print(numbers)

# What is the output? 
numbers = [10, 20, 30] 
value = numbers.pop(1)
print(value, numbers)

# What is the output? 
numbers = [3, 1, 2]
result = numbers.sort() 
print(result, numbers)

# What is the output?
values = [1, 2, 3] 
values.reverse()
print(values)

# What is the output?
a = [10, 20]
b = a
c = a.copy() 
b.append(30)
c.append(40)
print(a, c)

# What is the output?
result = [x ** 2
 for x in range(1, 6) if x % 2 == 0] 
print(result)

# what happens when the following code is executed?
# data = (10, 20, 30) 
# data[0] = 100

# What is the output?
data = (1, 2, [3])
data[2].append(4)
print(data)

# What is the output when elements from a list are added to a tuple through conversion?

data = (1, 2)
extra = [3, 4]
data = data + tuple(extra) 
print(data)

# What is the output?
a, b, *c = (1, 2, 3, 4)
print(a, b, c)

# What is the output?
data = (1, 2, 1, 3)
print(data.count(1), data.index(3))

# What is the output? 
values = {1, 1, 2, 3, 3} 
print(len(values))

# What is the output after using `add()`? 
values = {1, 2}
values.add(3) 
print(len(values), 3 in values)

# What is the output when a tuple is added as one element of a set?
values = {1, 2} 
values.add((3, 4)) 
print(len(values), (3, 4) in values)

# # What happens when the following code is executed?
# values = {1, 2} 
# values.add([3, 4])

# 31. What is the output when a list is passed to `update()`? 
values = {1, 2}
values.update([2, 3, 4]) 
print(len(values), 4 in values)

# What is the output?
values = set() 
values.add("ab") 
print(len(values), "a" in values, "ab" in values)

# What is the output? 
values = set() 
values.update("ab") 
print(len(values), "a" in values, "ab" in values)

# What is the output after using both `remove()` and `discard()`?
values = {1, 2, 3}
values.remove(2) 
values.discard(5) 
print(len(values), 2 in values)

# What is the output? The exact removed value does not need to be known. 
values = {10, 20, 30} 
removed = values.pop() 
print(len(values), removed in values)

# What is the output?
a = {1, 2, 3} 
b = {3, 4} 
print(len(a | b), len(a & b))
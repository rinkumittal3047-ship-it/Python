name=["rinku","mahak","khushbu","dimpal","jaanvi"]    #when we remove the element rmeove after that list  is also complete print 
print(name[2:4])
print(name)

# tuples in python
# ()
number=(1,2,3,4,[5,6,7,8,9],10)    #tuple is a collection which is ordered and unchangeable. Allows duplicate members.
print(number)    #print the tuple
a=list(number)          #
print(a.insert(5, 11))    #insert an element at a specific index
print(a)    #print the tuple
number=tuple(a) 
print(number)
print(len(number))

num=("rinku",2,"khushbu")    #concatenation of tuple
text=("deepika",5,2)
b=num+text
print(b)

number=((1,3,4,34,56),4,6,(8,9,10,11),(14,15,16,17,18),4,6,)    #unpacking of tuple
n1,n2,n3,*n4=number
print(number)
index=number.index(n1)#index of the element  #acess the index number
print(index)
print(n1)
print(n2)
print(n3)
print(n4)
print(number.count(4))   #count the elments repition 

t1=(23,43,"sonakshi",57,8,43,43)
first=t1.index(43)
print(t1[first+1:].index(43)+first+1)








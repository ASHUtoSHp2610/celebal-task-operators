#identity operators
a = ["apple", "banana"]
b = ["apple", "banana"]
c = a
print(a is b)
#returns False because a is not the same object as b, even if they have same content
print(a is c)
# returns True because c is the same object as a

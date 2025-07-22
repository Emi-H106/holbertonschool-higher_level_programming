
# Understanding Python Objects:Everything is object!

## :pencil2:Introduction
In this post, I want to share what I learned about how Python handles different types of objects — especially the differences between mutable and immutable objects. Understanding this is crucial for writing bug-free Python code and for passing technical interviews. I will explain each concept step by step with small code examples.

### :large_orange_diamond:id and type
In Python, everything is an object. We can check the _type_ of any object using the `type` function, and see its unique _identity_ (the memory address in CPython) with `id`.<br>
Example:<br>
```
a = [1, 2, 3]
print(type(a))  # <class 'list'>
print(id(a))    # e.g., 140012345678912
```
The `id` will stay the same as long as the object itself stays the same.<br>

### :large_orange_diamond: Mutable objects
A mutable object can be changed after it is created. <br>
Lists and dictionaries are classic examples:<br>
```
l = [1, 2, 3]
print(id(l))
l.append(4)
print(l)        # [1, 2, 3, 4]
print(id(l))    # Same ID as before
```
The list stays the same object, but its content changes.<br>
### :large_orange_diamond: Immutable objects
An immutable object cannot be changed. Integers, strings, and tuples are immutable in Python.<br>
```
a = 1
print(id(a))
a = a + 1
print(a)        # 2
print(id(a))    # Different ID!

s = "Hello"
print(id(s))
s += " World"
print(s)        # "Hello World"
print(id(s))    # Different ID again
```
When you "change" an immutable object, you are actually creating a new one.<br>

### :diamond_shape_with_a_dot_inside: Why does it matter?
Python treats mutable and immutable objects differently for efficiency and safety. For example, small integers (from -5 to 256) are reused:<br>
```
a = 100
b = 100
print(a is b)   # True

x = 1000
y = 1000
print(x is y)   # Often False

```
Empty tuples are shared:
```
a = ()
b = ()
print(a is b)   # True
```
But non-empty tuples are new objects:
```
a = (1,)
b = (1,)
print(a is b)   # False
```
Mutability also affects operations:
```
l = [1, 2, 3]
print(id(l))
l = l + [4]  # Creates a new list
print(id(l)) # New ID

l = [1, 2, 3]
print(id(l))
l += [4]     # Mutates in place
print(id(l)) # Same ID
```
### :diamond_shape_with_a_dot_inside:  How arguments are passed
In Python, variables are references to objects. When you pass an object to a function, you pass the reference. If the object is mutable, the function can modify it:<br>
```
def add_item(l):
    l.append(4)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 4]
```
But with an immutable type:
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # Still 1
```
The function receives a reference to the integer, but since integers are immutable, the function cannot change the original value.<br>

## :bulb: Conclusion
Understanding `id()`, `type()`, mutability, and how Python passes arguments is critical for debugging, writing clear code, and avoiding unexpected bugs. If you want to master Python, these small details make a big difference!
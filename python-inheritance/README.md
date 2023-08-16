Python - Inheritance
=================================================================================
Resources
Read or watch:

Inheritance [https://intranet.alxswe.com/rltoken/r98rF-KEP_4zklx-Ixo9Lw]
Multiple inheritance [https://intranet.alxswe.com/rltoken/W6NWNCV3JwjVxXZKsTgv5Q]
Inheritance in Python [https://intranet.alxswe.com/rltoken/YmPZF5DTFpaCN-4LywFC3Q]
Learn to Program 10 : Inheritance Magic Methods [https://intranet.alxswe.com/rltoken/vBJ_uP2459h4Tc2wI_blwA]
===============================================================================
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

===============================================================================
General

Why Python programming is awesome
What is a superclass, baseclass or parentclass
What is a subclass
How to list all attributes and methods of a class or instance
When can an instance have new attributes
How to inherit class from another
How to define a class with multiple base classes
What is the default class every class inherit from
How to override a method or attribute inherited from the base class
Which attributes or methods are available by heritage to subclasses
What is the purpose of inheritance
What are, when and how to use isinstance, issubclass, type and super built-in functions
===============================================================================

Requirements

Python Scripts
Recommended editors: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
The length of your files will be tested using wc
===============================================================================

Documentation
Do not use the works import or from inside your comments, the checker will think you try to import some modules
====================================================================================

Quiz questions
Question #0
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        self.id = 89

u = User()
print(u.id)

90


89


1
==============================================================================
Question #1
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id = 89

u = User()
print(u.id)

90


89


1
==============================================================================
Question #2
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id += 99

u = User()
print(u.id)

100


99


1
============================================================================
Question #3
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

for i in range(3):
    b = Base()
print(b.id)

3


None


2


4
=========================================================================
Question #4
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()

u = User()
print(u.id)

0


None


2


1
============================================================================
Question #5
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

for i in range(4):
    u = User()
print(u.id)

3


4


None


5
==================================================================
Question #6
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        self.id = 89
        super().__init__()

u = User()
print(u.id)

90


89


1
====================================================================
Question #7
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)

1


0


3


2
====================================================================
Question #8
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

b = Base()
print(b.id)

0


None


1
=============================================================
Question #9
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

u = User()
print(u.id)

0


None


2


1
=================================================================================

Tasks
0. Exact same object
mandatory
===============================================================================

Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
is_same_class = __import__('0-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

guillaume@ubuntu:~/$ python3 0-main.py
1 is an instance of the class int
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 0-is_same_class.py
  
0/12 pts
1. Same class or inherit from
mandatory
=============================================================================

Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('1-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

guillaume@ubuntu:~/$ python3 1-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 1-is_kind_of_class.py
  
0/12 pts
2. Only sub class of
mandatory
===============================================================================

Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
inherits_from = __import__('2-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

guillaume@ubuntu:~/$ python3 2-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 2-inherits_from.py
  
0/12 pts
3. Geometry module
mandatory
=============================================================================

Write an empty class BaseGeometry.

You are not allowed to import any module
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
BaseGeometry = __import__('3-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

guillaume@ubuntu:~/$ python3 3-main.py
<3-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 3-base_geometry.py
  
0/7 pts
4. Improve Geometry
mandatory
=============================================================================

Write a class BaseGeometry (based on 3-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ python3 4-main.py
[Exception] area() is not implemented
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 4-base_geometry.py
  
0/5 pts
5. Integer validator
mandatory
====================================================================
Write a class BaseGeometry (based on 4-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ python3 5-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 5-base_geometry.py
  
0/12 pts
6. Rectangle
mandatory
============================================================================

Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ python3 6-main.py
<6-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 6-rectangle.py
  
0/12 pts
7. Full rectangle
mandatory
==============================================================================

Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py). (task based on 6-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

guillaume@ubuntu:~/$ python3 7-main.py
[Rectangle] 3/5
15
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 7-rectangle.py

0/12 pts
8. Square #1
mandatory
================================================================== 

Write a class Square that inherits from Rectangle (7-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
Square = __import__('8-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] 13/13
169
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx_python
Directory: python-inheritance
File: 8-square.py
*******************************************************************************
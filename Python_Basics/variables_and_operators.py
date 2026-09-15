print("Hello World")
print("Welcome to Python")
print("Welcome to data Engineering")

print("welcome to data engineering\nwelcome to python")

print("Hello" , end=" ")
print("World")

# printing in the same line
print("Python" , end=" ")
print("is", end =" ")
print("easy")

age=19
if age > 18:
    print("You are eligible to vote")
    print("You can vote in the elections")

print("Outside if block")

# int, str, bool, float, None

name:str="riya"  # str
age:int=25       # int
salary:float=50000.50    # float
is_active:bool=True     # bool
is_inactive=False  # bool
middle_name=None   # absence of value

print(name)
print(age)
print(salary)

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))

name="riya sharma"
print(name)
print(name[0])
print(name[1])
print(len(name))

# string formatting

name="jiya"
age=26
print("my name is " + name + " and my age is " + str(age))
print(f"my name is {name} and age is {age}") # f"string {}"

print(f"Name: {name}, Age: {age}")

customer_id=101
customer_name="Amit"
print(f"Customer ID: {customer_id}, Customer Name: {customer_name}")

# a=10
# b=20
# print(f"Sum is : {a+b}")

# Arithmatic Operators
a=10
b=3
# print(f"Sum is {a+b}")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)
print(a**b)
print(7/2)
print(7//2)#

a = 15
print("initial", a)
a = a + 5
print("changed", a)
a += 5   # a= a+5
print("updated", a)
a -= 5  # a = a-5
a *= 5  # a = a*5
a /= 5  # a = a/5

# comparison operators, returns result in boolean value True or False
a= 10
b= 20

print(a == b)   # equality operator
print(a != b)   # not equal operator
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operators , and, or not
print("-----------------------------------------------------")
age= 25
salary =55000
print( age > 18 and salary > 50000)  # True and True = True
print( age > 18 or salary > 50000)  # True and False = False
print( not age > 18)  # False and True  # !


print("MEMBERSHIP OPERATOR")
# Membership Operator

city="Mumbai"   # where city in ("Mumbai", "Delhi", "Bangalore")
print("M" in city)
print("x" in city)
print("x" not in city)

cities=["Mumbai", "Delhi", "Bangalore"]
print("Mumbai" in cities)

print("IDENTITY OPERATOR") # is is not
# Identity operator
city = "Delhi"
city1 = "Delhi"
print(id(city))
print(id(city1))

print(city == city1)
print(city is city1)

a=[10, 20]
b=[10, 20]

print(id(a))
print(id(b))

print(a == b)
print(a is b)

value="Riya"
print(value is None)

value=None
print(value is None)































































































from Python_Basics.variables_and_operators import cities

# age="25"
# print(type(age))
#
# age = int(age)
# print(type(age))
#
# num=100
# print(type(str(num)))  #   type(str(num))
# print(float(num))
# print(int("100"))
#
# # input()
#
# name= input("Enter your name: ")
# print(f"my name is {name}")
#
# age= input("Enter your age: ")  # "25"
# print(f"age is {age}")
# print(type(age))
# age=int(age)
# print(type(age))
#
# salary = float(input("Enter your salary: ")) # ""
# print(f"salary is {salary}")
# print(salary + 5000)

customer_id=101
customer_name="Amit"
salary=50000.50
city="Delhi"
print(
    f"customer_id: {customer_id}, "
    f"customer_name: {customer_name}, "
    f"salary: {salary},"
    f" city: {city}"
)

# salary =float(input("Enter your salary: "))

salary=60000
if salary > 50000:  # if condition: 51000 > 50000
   print("eligible for bonus")
else:
    print("not eligible for bonus")

# salary =70000
if salary >= 100000:  # if condition: 51000 > 50000
   print("High Salary")

elif salary >= 50000:  # if condition: 51000 > 50000
    print("Medium Salary")

else:
    print("Low Salary")

age=17
is_Active=True

if age >=18:
    if is_Active:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

for i in range(5):      # 0-5 , 0 1 2 3 4
    print(i, end =" ")

print()

for i in range(1,5):      # 1 -5,   1, 2, 3, 4
    print(i, end =" ")
print()

for i in range(2,5):      # 1 -5,    2, 3, 4
    print(i, end =" ")     # range(start, stop, step)

print()

for i in range(1,10, 2):      # 1 -5,    1 3 5 7 9
    print(i, end =" ")

print()
# for i in range(5, 101, 2):
#     print(i, end=" ")

name="riya"
for ch in name:   # ['r', 'i', 'y', 'a']
    print(ch, end=" ")


for i in range(5):     # start end step  (0, 5), end is excluded 0, 1 2 3 4
    print(i)

print()
for i in range(5, 0, -1):       # 5 4 3 3 1
    print(i, end=" ")

print()
for i in range(10, 0, -2):       # 10 8 6 4 2
    print(i, end=" ")
print()

for i in range(1, 11):       # 1 2 3 4 5 6 7 8 9 10
    print(i, end=" ")
print()

for i in range(2, 21,2):   # print even numbers from 2  4 6 8 10 12 ....
    print(i, end=" ")
print()

for i in range(1, 20,2):   # print odd numbers from 1 3 5 7 9 11 13 15 17 19
    print(i, end=" ")
print()

for i in range(10, 0, -1):  # print from 10 to  1
    print(i, end=" ")

# table of 5
print()
for i in range(5, 51,5):   # 5 10 15 20 25 30 35 40 45 50
    print(i, end=" ")

print()
for i in range(1, 11):   # 1 2 3 4 5 6 7 8 9 10
    print(5 * i, end =" ")
print()

for i in range(1, 11):     # 1 2 3 4 5 6 7 8 9 10
    if i % 2 == 0:
        print(f"{i} is even")
print()
name="riya"
cities=["Mumbai" , "Delhi", "Bangalore", "Chennai"]

for i in cities:
    print(i, end=" ")

print()

for i, j in enumerate(cities):
    print(i,j)

for i in range(3):      # 0 1 2
    for j in range(2):  # 0 1
        print(i,j)

for student in range(1,4):
    for test in range(1,3):
        print(f"Student {student} Test {test}")

count = 1
while count <= 5:
    print(count)
    count += 1    # count = count + 1

#
# pin=""
# while pin != "1234":
#     pin=input("Enter your pin: ")
# print("Pin is correct")

for i in range(1, 6):    # 1 2 3 4 5
    if i == 3:
        break
    print(i)

print("CONTINUE KEYWORD")
for i in range(1, 6):    # 1 2 3 4 5
    if i == 3:
        continue
    print(i)

print("PASS  KEYWORD")

for i in range(5):
    if i==3:
      pass
    else:
        print(i)

def process_customer():
    pass

# x= int(input ("enter a number: "))
# if x==1:
#     print("one")
# elif x==2:
#     print("two")
# else:
#     print("invalid")
x= int(input ("enter a number: "))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("invalid")


choice= int(input("Enter your choice: "))

match choice:
    case 1:
        print("load data")
    case 2:
        print("Transform data")
    case 3:
        print("Export Data")
    case _:
        print("Invalid choice")







































































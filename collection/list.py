cities_ex=["Mumbai", "Delhi", "Bangalore"]
numbers_ex=[10, 20, 30, 40, 50]
names=["Riya", "Ananya", "Aarav", "Vivaan"]
data=[10, 20, 30, "Riya", "Ananya", 40.5, 50.6, True, False, "Riya", "Riya"]

new_cities=[]
print(new_cities)
new_cities.append("Mumbai")
new_cities.append("Delhi")
print(new_cities)

# list()
numbers_with_cons = list(range(5))
print(numbers_with_cons)

#        0        1        2         3
names1=["Riya", "Ananya", "Aarav", "Vivaan"]
print(names1[0])
print(names1[1])
print(names1[-1])
print(names1[-2])

names1[0]="Riya Sharma"
print(names1)
print(len(names1))

last_index= len(names1) -1
print(last_index)

cities=["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai"]  # start end

print(cities[1: 4])
print(cities[:3])
print(cities[2:])
print(cities[:])
#
numbers = [10, 20, 30, 40, 50]
numbers[1]=25
print(numbers)
numbers[1:3] = [22, 33]   # 1, 2
print(numbers) # Output: [1

numbers = [10, 20, 30, 40, 50]
numbers.append([60, 70])
print(numbers)
numbers.extend([60, 70])
print(numbers)
numbers.clear()
print(numbers)
# del numbers
# print(numbers)

numbers.insert(2, 25)   # index, value
print(numbers)
# print(numbers.remove(30))
print(numbers)
print(numbers.pop())
print(numbers)
# print(numbers.pop(4))
# print(numbers)

cities=["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai", "Mumbai", "Kolkata", "Mumbai"]
print("Mumbai" in cities)
print("Kolkata" in cities)
print(cities.count("Mumbai"))
print(cities.index("Chennai"))

marks=[10, 20, 30, 50, 15, 40, 50]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

for city in cities:
    print(city, end=" ")

for city in cities:
    if city== "Pune":
       print("Found Pune")

tables=["customers", "orders", "products"]
for table in tables:
    if table=="orders":
        print("apply transformations on orders table")

for i in range(len(cities)):
    print(f"City at index {i} is {cities[i]}")

# last_index = len(list)-1

# finding minimum value from given list
marks=[100, 20, 30, 50, 15, 40, 50]
minimum = marks[0]  # 100

for mark in marks:  # 100 20
    if mark < minimum:
        minimum=mark
print(minimum)

# finding minimum value from given list
marks=[100, 20, 30, 50, 15, 40, 50, 190]
maximum = marks[0]  # 100
for mark in marks:  # 100 20
    if mark > maximum:
        maximum = mark
print(maximum)

# print(max(marks))
# print(min(marks))
# print(sum(marks))

numbers = [1 , 2, 3, 4, 5]    # squares= [ expression for variable in iterable]
squares=[]
for num in numbers:
    squares.append(num * num)
print(squares)

numbers = [1 , 2, 3, 4, 5, 6]
squares = [num * num for num in numbers]
print(squares)

numbers = [1 , 2, 3, 4, 5]
squares=[]
for num in numbers:
    if num%2==0:
        squares.append(num * num)
print(squares)
squares = [num * num for num in numbers if num%2==0]
print(squares)

# def square(x):
#     return x * x
#
# print(square(5))

# square= lambda x: x * x
# print(square(6))

result = list(map(lambda x : x*x, [1 , 2, 3, 4, 5]))  # function , iterable
print(result)


output = list(filter(lambda x : x %2==0, [1 , 2, 3, 4, 5]))  # function , iterable
print(output)

from functools import reduce
output = reduce(lambda x, y: x+y, [1 , 2, 3, 4, 5])  # function , iterable
print(output)


numbers = [10, 20, 30, 40]

for i in numbers:
    print(i, end=" ")

print()

for i, j in enumerate(numbers):
    print(i, j)

names = ["a", "b", "c"]
marks = [70, 75, 75]

for name, mark in zip(names, marks):
    print(name, mark)













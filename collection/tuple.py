
employee = (101, 'amit', 50000.55, 101, 'amit')
print(employee)
print(employee[0])
print(employee[1])

# employee[1] = 'sumit'

print(employee)

number = (10, 20, 30, 40, 50)
numbers = 10, 20, 30, 40

n1= (10,)
print(type(n1))
num= 10,
print(type(num))

# numbers = (10, 20, 30, 40, 50, (1, 2), [2, 3])

print(number[0])
print(number[1])
print(number[-1])
print(number[1:4])  # start, end is excluded

marks = (10, 20, 30, 40, 40, 50, 40, 10, 20, 40)

for m in marks:
    print(m, end=" ")
print()
print(10 in marks)
print(marks.count(40))
print(marks.index(40))

# print(marks.append(90))
# print(marks.extend([90, 50]))
# print(marks.remove(10))
# print(marks.pop())
# print(marks.clear())
# marks[1]=100
# marks[1:3] = (10,55)
# print(marks)
# print(emp_numbers.sort(reverse=True))

# TUPLE UNPACKING

emp = ('E101', 'neha', 50000.12)
emp_id, name, salary = emp
print(emp_id)
print(name)
print(salary)

emp_numbers = (5, 10, 2, 8, 3)
print(min(emp_numbers)) # Output: 2
print(max(emp_numbers)) # Output: 10
print(sum(emp_numbers)) # Output: 28

new_collection=sorted(emp_numbers)
print(new_collection)

# list(), tuple() - Converting Other Data Types to Tuple
t1= (10, 20, 55, 66, 77, 88)
l1 = list(t1)
print(l1)

l2= [11, 22, 33, 55, 66, 99]
t2 = tuple(l2)
print(t2)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print(result) # Output: (1, 2, 3, 4, 5, 6)
# operator overloading
# Tuple Repetition (*)
t1 = (7, 8)
print(t1 * 3) # Output: (7, 8, 7, 8, 7, 8)

# Checking Membership (in and not in)
# t2 = ("Python", "Scala", "Spark")
# print("Scala" in t2) # Output: True
# print("Java" not in t2) # Output: True
# Immutable Nature of Tuples : Tuples cannot be modified after creation.

# t1 = (1, 2, 3)
# t1[0] = 10    #
# However, you can reassign a tuple.
# t1 = (10, 20, 30) # This is allowed

l3 = [10, 20, 35, 40, 45]
result = [i*2 for i in l3 if i %2==0 ]
print(result)


t3 = (10, 20, 35, 40, 45)
result = tuple(i*2 for i in t3 if i %2==0)
print(result)

t4 = (1 , 2, 3, 4, 5)

result = tuple(map(lambda x : x*x, t4 ))  # function , iterable
print(result)

output = tuple(filter(lambda x : x %2==0, t4))  # function , iterable
print(output)

from functools import reduce
output = reduce(lambda x, y: x+y, t4)  # function , iterable
print(output)



































numbers = {10, 20, 30, 20, 10}
print(numbers)

number= set([10, 20, 100])
print(type(number))

print("......................")

s1= {}
print(type(s1))

s2= set()
print(type(s2))

# s3 = {1, 2, 3, 4}
# print(s3[0])

fruits = {"apple", "banana", "cherry"}
fruits.add("mango")
print(fruits)

fruits.add("apple")
print(fruits)

# fruits.add(("grapes", "orange"))
# print(fruits)

fruits.update(["grapes", "orange"])
print(fruits)
#
fruits.remove("banana")
print(fruits)

# fruits.remove("grapes")
# print(fruits)

fruits.discard("cherry")
print(fruits)

fruits.discard("grapes")
print(fruits)

print(fruits.pop())

fruits.clear()
print(fruits)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1.union(set2))  # Union: {1, 2, 3, 4, 5}

print(set1 & set2)  # Intersection: {3}
print(set1.intersection(set2))  # Intersection: {3}

print(set1 - set2)  # Difference: {1, 2}
print(set1.difference(set2))  # Difference: {1, 2}
# issubset(set2)
set1 = {"Kafka", "Spark"}
set2 = {"Hadoop", "Kafka", "Spark", "Flink"}
print(set1.issubset(set2))  # Output: True

# issuperset(set2)
set1 = {"Hadoop", "Kafka", "Spark", "Flink"}
set2 = {"Kafka", "Spark"}
print(set1.issuperset(set2))

crm_ids = {'c101', 'c102', 'c103', 'c104'}
billing_ids = {'c101', 'c104'}

common_ids= crm_ids & billing_ids
print(common_ids)

missing_ids = crm_ids - billing_ids
print(missing_ids)

set1 = {"Delhi", "Mumbai", "Chennai"}
set2 = {"Mumbai", "Kolkata", "Chennai"}
symDiff1 = set1 ^ set2   # Using ^ operator
print( symDiff1) #
symDiff2 = set1.symmetric_difference(set2) # Using method
print( symDiff2) # Output: {'Delhi', 'Kolkata'}


cities = {"Delhi", "Mumbai", "Chennai"}
print("Delhi" in cities)  # Output: True
print("Kolkata" not in cities)  # Output: True

fruits = {"Apple", "Mango", "Banana"}
if "Mango" in fruits:
    print("Mango is available!")
if "Grapes" not in fruits:
    print("Grapes are not available!")

allowed_users = {"admin", "manager", "supervisor"}
user = "employee"
if user not in allowed_users:
    print("Access Denied!")
else:
    print("Access Granted!")

fruits = {"Mango", "Apple", "Banana", "Grapes"}
for f in fruits:
    print(f)

numbers = {1 , 2, 3, 4, 5, 6}
squares = {num * num for num in numbers}
print(squares)


cities = {"Delhi", "Mumbai", "Chennai"}
cityList = list(cities)
print(cityList) # Output: ['Mumbai', 'Delhi', 'Chennai']
cityTuple = tuple(cities)
print(cityTuple) #

l1= [10, 20, 30]
print(set(l1))

t1= (1,2,3)
print(set(t1))

result = set(map(lambda x : x*x, {1 , 2, 3, 4, 5}))  # function , iterable
print(result)

output = set(filter(lambda x : x %2==0, [1 , 2, 3, 4, 5]))  # function , iterable
print(output)

from functools import reduce
output = reduce(lambda x, y: x+y, {1 , 2, 3, 4, 5})  # function , iterable
print(output)

# numbers = {10, 20, 30}
#
# numbers = {10, 20, {"name": "amit"}}
# print(numbers)


# numbers = {(50, 60)}
# print(numbers)
# numbers.add((10, 10, (100, 200)))
# print(numbers)


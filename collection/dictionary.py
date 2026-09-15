
student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}
print(student["name"])
print(student["age"])
print(student["city"])
student["age"] = 21

print(student)

students = {
    "Amit": 85,
    "Rahul": 90,
    "Neha": 95
}
print("Rahul" in students)  # Output: True
print("Priya" not in students)  # Output: True
print(90 in students.values())  # Output: True
print(90 not in students.values())  #

keyList = list(students.keys())
valueList = list(students.values())
tupleList = list(students.items())
print(keyList) # Output: ['Amit', 'Rahul', 'Neha']
print(valueList) # Output: [85, 90, 95]
print( tupleList)

student1 = {"Amit": 85, "Rahul": 90}
student2 = {"Neha": 95, "Rahul": 88}
student1.update(student2)
print(student1)  # Output: {'Amit': 85, 'Rahul': 88, 'Neha': 95}
#
# # Using | operator
merged_student = student1 | student2
print(merged_student)  # Output: {'Amit': 85, 'Rahul': 88, 'Neha': 95}
#
# # Using {**dict1, **dict2}
merged_student = {**student1, **student2}
print(merged_student)  # Output: {'Amit': 85, 'Rahul': 88, 'Neha': 95}

students = {
    "Amit": 85,
    "Rahul": 90,
    "Amit": 95}
print(students)  # Output: {'Amit': 95, 'Rahul': 90}

students = {"Amit": 90, "Rahul": 90, "Neha": 90}
print(students)

# print(students["amit"])  # Output: Amit

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

for i in student:
    print(i)

for i in student.keys():
    print(i)

for i in student.values():
    print(i)

for i, j in student.items():
    print(i, j)


customer = {
    "customer_id" : 101,
    "name" : "amit",
    "city" : "Pune",
    "status" : "Active"
}

for key, value in customer.items():
      print(key, "=", value)

for key, value in customer.items():
      if key == "status":
          print(value)


students = [
    {"id" : 101, "name": "neha", "marks" : 85},
    {"id" : 102, "name": "amit", "marks" : 72},
    {"id" : 103, "name": "rahul", "marks" : 91}
]

for s1 in students:
    print(s1["name"])

for s1 in students:
    if s1["marks"] > 80 :
        print(s1["name"])

#  { key_expression :  value_expression for i in iterable }

numbers = [1, 2, 3, 4, 5, 6]

squares= { num : num * num for num in numbers }
print(squares)

even_squares= { num : num * num for num in numbers  if num % 2 ==0 }
print(even_squares)

name= "python"    # [ "amit", "neha"]   [ 'p', 'y', 't', 'h']
print(name[0])
print(name[1:4])
# name[0]= "j"

for ch in name:
    print(ch)

for i in range(len(name)):
    print(i , name[i])




























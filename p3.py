# list and tuples
marks=[45.6,78.09,89.0,90.0,67.8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1:4])
print(len(marks))
student=["millie",23,78.09,"newyork"]
print(student)
print(student[0])
student[0]="sadie"
print(student)
score=[89,67,54,67,90]
print(score[1:4])
list=[3,6,1,9,7,5]     
list.append(6)
print(list)
# append() method adds an element to the end of the list
list.sort()
print(list)
#sort() method sorts the list in ascending order
list.sort(reverse=True)
print(list)
# reverse=True sorts the list in descending order
list1=["ibiza","malibu","denver","santamonica"]
list1.reverse()
print(list1)
list1.sort()
print(list1)
list2=[3,4,5,6,6,8,9]
# list2.insert(2,7)
# print(list2)
list2.remove(6)
print(list2)
list2.pop(3)
print(list2)

# TUPLES
tup=(4,5,6,7,8)
print(type(tup))
print(tup[1:3])
print(tup.index(5))
print(tup.count(8))
print(len(tup)) 
grade=("D","A","A","H","A")
print(grade.count("A"))
grade=["D","A","A","H","A"]
print(grade.sort())
print(grade)
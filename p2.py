str1="lets go to newyork \n hooray we r in newyork"
print(str1)
str2="london"
str3="city"
concat=str2+str3
print(concat)
print(len(str2))
str4="hello"
print(str4[0])
print(str4[1])
print(str4[2])
print(str4[3])
print(str4[4])
str5="I am a student";
print(str5[0:4])
print(str5[5:len(str5)])
# str6="apple"
# print(str6[-3:-1])
str7="i want to go to monaco"
print(str7.endswith("monaco"))
print(str7.startswith("i want"))
print(str7.capitalize()) 
# capitalizes the first letter of the string and works only once
print(str7.replace("monaco", "paris")) 
print(str7.find("monaco")) 
# -1 if not found, else returns the index of the first occurrence of the substring
print(str7.count("o"))
# name=input("enter your name:")
# print("length of your name is:",len(name))
str8=" i will work in $ for sure. My monthly salary will be $5000000."
print(str8.count("$"))

# conditional statements
age=21
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

light=input("enter the color of traffic light:")
if (light=="green"):
    print("go")
elif (light=="yellow"):
    print("slow down")
elif (light=="red"):
    print("stop")
else:
    print("invalid traffic light color")
marks=int(input("enter your marks:"))
if(marks>=90):
   grade="A"
elif(90>marks>=80):
  grade="B"
elif(80>marks>=70):
    grade="C"
elif(70>marks>=60):
   grade="D"
else:
  grade="F"
print("your grade is:",grade)
number=int(input("enter a number:"))
if(number%2==0):
    print("even number")
else:   
    print("odd number")
# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnRh78LL8nPXCvbsl9V57JJjtUXrGaxS
"""

#1
def area_of_rect(length,breadth):
  try:
    if(length<=0 or breadth<=0):
      raise Exception("Values should be positive")
    return length*breadth
  except:
    print("Enter only postive values")

length=float(input("Enter the length of the rectangle:"))
breadth=float(input("Enter the breadth of the rectangle:"))
area=area_of_rect(length,breadth)
print(area)

#2
def bmi(height,weight):
  try:
    if(height<=0 or weight<=0):
      raise Exception("Values should be positive")
    return weight/((height/100)**2)
  except:
    print("Enter only postive values")

height=float(input("Enter the Height in cm:"))
weight=float(input("Enter the Weight in kg:"))
bmi=bmi(height,weight)
print(bmi)

#3
def display(students):
  for student,details in students.items():
    print(f"Details of student {student}")
    print("Name:",details["name"])
    for i in range(len(details["scores"])):
      print("Subject{}:{}".format(i+1,details["scores"][i]))

no_of_student=int(input("Enter number of students:"))
students={}
for i in range(no_of_student):
  name=input("Enter Student name:")
  score=input("Enter the scores of the student with spaces")
  score=score.split(" ")
  students[i+1]={"name":name,"scores":score}

display(students)

#4
def category():
  try:
    age=int(input("Enter the age of the person:"))
    if(age<=0):
      raise ValueError("Enter only positive values")
    if age<18:
      return "Minor"
    elif age<60:
      return "Adult"
    else:
      return "Senior"
  except:
    print("Enter proper values")

category=category()
print(f"The person is a {category}")

#5
for i in range(1,51):
  print(i)

#6
def promt(password,entry):
  while(True):
    if(password!=entry):
      print("Invalid Password: Enter again.")
      entry=input("Enter Password:")
    else:
      break

passwords={"user1":"aaaaaaa","user2":"bbbbbbb","user3":"ccccccc","user4":"ddddddd","user5":"eeeeeee","user6":"fffffff"}
user_name=input("Enter username:")
password=input("Enter Password:")
promt(passwords[user_name],password)
print("Welcome")

#7
def average(numbers):
  mean=sum(numbers)/len(numbers)
  return mean

numbers=[]
count=int(input("Enter total number of entries:"))
for i in range(count):
   number=float(input(f"Enter number {i+1}:"))
   numbers.append(number)
mean=average(numbers)
print("The average of the given list of numbers is {:.2f}.".format(mean))

#8
def count_vowels(string):
  vowels=('a','e','i','o','u','A','E','I','O','U')
  count=0
  for i in string:
    if i in vowels:
      count+=1
  return count

string=input("Enter the string:")
if(len(string)>0):
  count=count_vowels(string)
else:
  coutn=0
print("The number of vowels in the string:{}".format(count))

#9
import datetime

print(datetime.datetime.now())

#10
def addition():
  num=int(input("Enter the total entries:"))
  numbers=[]
  while(num):
    try:
      number=float(input("Enter number:"))
      numbers.append(number)
      num-=1
    except:
      print("Enter only numerical values")
  return sum(numbers)

result=addition()
print(result)

#11
def validation():
  try:
    num=int(input("Enter the total entries:"))
    return num
  except ValueError as e:
    print(f"Error:{e}")
    return "Enter Proper values"

result=validation()
print(result)

#12
def validation():
  try:
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    return num1/num2
  except ZeroDivisionError as e:
    print(f"Error:{e}")
    return "Do not provide 0 in the denominator"

result=validation()
print(result)

#13
with open("New_file.txt",'w') as file:
  file.writelines("Hello, Python!")

#14
with open("New_file.txt",'r') as file:
  print(file.read())

#15
with open("New_file.txt",'aw') as file:
  file.writelines("\nNew line to write.")
  print(file.read())
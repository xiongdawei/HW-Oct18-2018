#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 23:39:27 2018

@author: davidxiong

UML 
Unified Modeling Language(UML)

className point
x: float
y: float

getX(): float
getY(): float
setx()
sety()

"""


class Student(object):
    def __init__(self,name,age,subject,grades,hair_remain):
        self.name = name
        self.age = age
        self.subject = subject
        self.grades = grades
        self.hair = hair_remain
    
        
    def get_name(self):
        message_c = "This IB student's name is " + self.name
        return message_c

    def get_age(self):
        message_d = "He is " + str(self.age) + " years old"
        return message_d

    def get_subject(self):
        return self.subject

    def get_grades(self):
        message_e = "His economic grades is " + str(self.grades) + "."
        return message_e
    
    def set_name(self,name):
        self.name = name
    
    def set_age(self,age):
        self.age = age
        
    def set_subject(self,subject):
        self.subject = subject
        
    def ave_grades(self):
        return sum(self.grades)/len(self.grades)

    def __str__(self):
        print("name: " + str(self.name))
        print("age: " + str(self.age))
        print("subject: " + str(self.subject))
        print("grades: " + str(self.grades))
    
    def Engene(self):
        if self.grades<60:
            return "Wonderful Student. Is it Your Hobby to get a ZERO?  --- Mr.Engene "
        else:
            return "Good student, I am going to give your more HOMEWORK.  --- Mr.Engene "
          
    def __ave__(self):
        return sum(self.grades)/len(self.grades)
        


class IBstudent(Student):
    def __init__(self,name,age,subject,grades,hair_remain):
        super().__init__(name,age,subject,grades,hair_remain)
     
    
        
    
    def gett_name(self):
        return self.name
    
    def hair_remain(self,days):
        hair = 100
        while days>0:
            hair-=10
            days-=1
        message = "Hair Remain:" + str(hair) + "%"
        return message
    
        

        
    
    
   #S2C6Student = IBstudent('David',177,'CS',80,hair_remain = 100)

#print(S2C6Student.gett_name())
S2C6Student = IBstudent('David Xiong',17,'CS',50,hair_remain = 100)
print(S2C6Student.get_name()) 
print(S2C6Student.get_age())
print(S2C6Student.get_grades())
print(S2C6Student.hair_remain(3))

print(S2C6Student.Engene())
       
        




"""
overide
"""
        














































        
        
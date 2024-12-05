#!/usr/bin/env python
# coding: utf-8

# In[29]:


#ADEENA BINT SALEEM
#FA24-BBD-007
#QUESTION NO.1
class Person:
    def __init__(self, name, age, city):
        self.name = name  
        self.age = age    
        self.city = city 
person1 = Person("Alice", 30, "New York")
print(person1.name,person1.age,person1.city)


# In[30]:


#QUESTION NO.2
class Car:
    def __init__(self, make, model, year):
        self.make = make      
        self.model = model    
        self.year = year   
car1 = Car("Toyota", "Corolla", 2020) 
print(car1.make,car1.model,car1.year)  


# In[31]:


#QUESTION NO .3
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * (self.radius ** 2) 
        self.circumference = 2 * 3.14159 * self.radius
circle1 = Circle(5)  
print("Area:", circle1.area)  
print("Circumference:", circle1.circumference)


# In[32]:


#QUESTION NO .4
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width  
        self.perimeter = 2 * (self.length + self.width)  
rectangle = Rectangle(5, 3)  
print("Area:", rectangle.area)  
print("Perimeter:", rectangle.perimeter)


# In[33]:


#QUESTION NO.5
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name                
        self.marks = marks              
        self.average_marks = sum(self.marks) / len(self.marks) if self.marks else 0  

# Example usage:
student1 = Student("Alice", 101, [85, 90, 78, 92, 88])  
print("Average Marks:", student1.average_marks)  


# In[34]:


#QUESTION NO .6
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title                 
        self.author = author               
        self.publication_year = publication_year  

    def display_info(self):
        """Display the information about the book without using return."""
        print(f"'{self.title}' by {self.author}, published in {self.publication_year}")
book1 = Book("1984", "George Orwell", 1949)  
book1.display_info()  


# In[35]:


#QUESTION NO .7
class Employee:
    def __init__(self, name, salary, designation):
        self.name = name              
        self.salary = salary              
        self.designation = designation    

    def display_info(self):
        """Display the information about the employee."""
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Designation: {self.designation}")
employee1 = Employee("Alice", 50000, "Software Engineer")  
employee1.display_info()  


# In[36]:


#QUESTION NO .8
class Bank:
    def __init__(self, name, account_number, balance=0):
        self.name = name                  
        self.account_number = account_number  
        self.balance = balance           

    def deposit(self, amount):
        self.balance += amount  
        print(f"Deposited: {amount}")
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount 
            print(f"Withdrawn: {amount}")
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient balance for withdrawal")
bank_account = Bank("John Doe", "123456789", 1000)  
bank_account.deposit(500) 
bank_account.withdraw(200) 
bank_account.withdraw(2000)  


# In[ ]:





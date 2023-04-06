#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Write a for loop that iterates over a list of numbers and prints out each number on a new line.

x=[1,2,4,5,6,7,8,9,10]
for i in x:
    print(i)


# In[ ]:


#2.Write a for loop that iterates over a string and prints out each character on a new line.
family='kunal'
for x in family:
        print(x)
else:
     print('finish')


# In[1]:


#3.Write a for loop that iterates over a list of strings and prints out the length of each string.
family=['kunal','nikhil','veera']
for x in family:
    print(len(x))


# In[1]:


#4.Write a for loop that iterates over a range of numbers and prints out the square of each number.
for i in range(1,10):
    print(i**2,'',i)


# In[11]:


#5.Iterate over a list of numbers and print out only the even numbers:
numbers=[1,2,3,4,5,6,7,8,9,10]
new=[]
for evenno in numbers:
    if evenno %2==0:
         new.append(evenno)
print(new)
evenno=[x for x in range(0,11) if x%2==0]
print(evenno)


# In[12]:


#6.Iterate over a list of strings and print out only the strings that contain the letter "a":
strings=['kunal','dhanashree','veera']
for i in strings:
    if 'a' in i:
        print(i)


# In[ ]:


#7.Iterate over a list of tuples, where each tuple contains a name and an age,
# and print out only the names of people who are over 18 years old:
people = [("Alice", 20), ("Bob", 17), ("Charlie", 25)]
for i in people:
    name,age=i
    if age>18:
        print(name,age)


# In[ ]:


#8.Iterating over a list of dictionaries and printing only the names of people who are under 30 years old:
people = [ {"name": "Alice", "age": 25},{"name": "Bob", "age": 30},{"name": "Charlie", "age": 20}]
for i in people:
        name,age=i
        if age<=30:
            print(name,age)


# In[ ]:


#9.Write a loop to print all the numbers between 1 and 10:
for i in range(1,11):
    print(i)


# In[ ]:


#10.Write a loop to print all the even numbers between 1 and 20:
for i in range(1,21):
    if i %2==0:
        print(i)


# In[ ]:


#11.Write a loop to calculate the sum of all the numbers between 1 and 50:
k=0
for i in range(1,6):
    k=k+i
print(k)


# In[ ]:


#12.Write a loop to calculate the reverse of number:

n=int(input('enter no'))
rev=0
while n>0:
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
print(rev)


# In[ ]:


#13.Write a program to print all the even numbers between 0 and 100.
'''i=0
while i<=50:
     if i %2==0:
         print(i)
     i=i+1'''


# In[ ]:


#14.Write a program that prompts the user to enter a password and keeps prompting them until they enter the correct password "python".
i=input('enter password')
while i=='python':
    print('password is correct')
    break
else:
    print('password is incorrect, please try again')


# In[ ]:


#15.Write a program that prompts the user to enter a number between 1 and 10 and keeps prompting them until they enter a valid number.
'''i=int(input('enter number here'))
while i<=10:
    print('valid number')
    break
else:
    print('invalid number, please enter a valid number')'''


# In[ ]:


#16.Write a program that calculates the sum of all the numbers from 1 to 100.
'''sum=0
for i in range(1,101):
    sum=sum+i
print("The sum of all the numbers from 1 to 100 is:", sum)'''


# In[ ]:


#17.Write a loop query that counts from 1 to 10 and displays
#each number in the console.
'''for i in range(1,11):
    print(i)'''


# In[ ]:


#18.Write a loop query that calculates the sum of the first 100  numbers
#and displays the result in the console.
'''k=0
i=1
while i<=100:
      k=k+i
      i=i+1
print('sum of 1 to 100 no', k)'''


# In[ ]:


#19.Write a loop query that calculates the sum of all even numbers between 1 and 100
#and displays the result in the console.
              
k=0   
for i in range(1,101):
    if i %2==0:
        k=k+0
print('sum of all even no',i)


# In[ ]:


#20.print factorial of number
num=int(input('enter the number'))
fac=1
for i in range(1,num+1):
    fac=fac*i
print('factorial of',num,'is',fac)


# In[ ]:


#21.print reverse number from 10 to 0 using while loop
i=10
while i>0:
    print(i)
    i=i-1


# In[ ]:


#22.fibonacci series 0,1,1,2,3,5,8,13,21
n=int(input('enter the no'))
num0=0
num1=1
i=0
while i<n:
    print(num0)
    num3=num0+num1
    num0=num1
    num1=num3
    i=i+1


# In[ ]:


#23: Write a program that prints the numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i)
    i=i+1


# In[ ]:


#24 Write a program that prints the even numbers from 1 to 20 using a for loop.
for i in range(2,21,2):
    print(i)


# In[ ]:


#25: Write a program that asks the user to enter a number and then prints
#the multiplication table for that number from 1 to 10 using a for loop.
k=int(input('multiplication of'))
for i in range(1,11):
    print(k,'x',i,'=',k*i)


# In[ ]:


#26 Write a program that asks the user to enter a password
#and keeps asking until the correct password is entered using a while loop.
i=input('enter a password')
while i!='python':
    print('please input correct password')
    break
if i=='python':
    print('password is correct')


# In[ ]:


#27 Calculate the factorial of a given number using a for loop in Python.
#5=1*2*3*4*5
fac=1
num=int(input('enter the number'))
for i in range(1,num+1):
    fac=fac*i
print('factorial of',num,'is',fac)
    


# In[ ]:


#28 Print the Fibonacci series up to a given number using a for loop in Python. for eg 6=0,1,1,2,3,5
num1=0
num2=1
i=0
fib=int(input('enter the number'))
while i<fib:
    print(num1)
    num3=num1+num2
    num1=num2
    num2=num3
    i=i+1


# In[19]:


a=list(range(1,10))
a


# In[25]:


#if it is even find the square if it is odd find the cube
ni=[]
for i in a:
    if i%2==0:
        ni.append(i**2)
    else:
        ni.append(i**3)
    


# In[26]:


ni


# In[34]:


#Generate a list of even numbers from 1 to 10.
evenno=[x for x in range(1,11) if x%2==0]
evenno


# In[30]:


for x in range(1,11):
    if x%2==0:
        print(x)


# In[32]:


#Generate a list of squares of numbers from 1 to 5.
sq=[x**2 for x in range(1,6)]
sq


# In[35]:


for x in range(1,6):
    print(x**2)


# In[41]:


squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[20]:


#  this is a comment not a code execite with shift and enter
print(7,2)


# In[49]:


# order of logical are not and then or


# In[59]:


### if statement ########
if 5 == 15 / 3 :
    print("Huraay!")


# In[55]:


5 is not 6


# In[67]:


x =1 
if x > 3 :
    print("case1")
else:
    print("case2")


# In[69]:


def  compare_to_five(y):
    if y > 5 :
        return "Greater"
    elif y < 5 :
        return "Less"
    else :
        return "equal"


# In[73]:


print(compare_to_five(2))


# In[75]:


def simple():
    print("My first function")


# In[77]:


simple()


# In[79]:


def plus_ten(a):
    return a + 10


# In[81]:


plus_ten(2)


# In[92]:


def plus_ten(a):
    result = a + 10
    print("outcome")
    return result


# In[93]:


plus_ten(2)


# In[100]:


def wage(w_hours):
    return w_hours*25
def with_bonus(w_hours):
    return wage(w_hours) + 50


# In[104]:


wage(10), with_bonus(8)


# In[109]:


def add_10(m):
    if m >= 100 :
        m=  m + 10
        return m
    else:
        return "Save more !"


# In[113]:


add_10(200)


# In[115]:


def subtract_bc(a,b,c):
    result = a - b*c
    print("paramenter a equals", a)
    print("paramenter a equals", b)
    print("paramenter a equals", c)
    return result


# In[118]:


subtract_bc(10,3,2)


# In[121]:


subtract_bc(b=3,a=10,c=2)
    


# In[125]:


type(10.0)
str(500)


# In[128]:


### important functions ##
max(10,20,30)
z = -20
abs(z)


# In[129]:


list_1 = [1,2,3,4]


# In[130]:


sum(list_1)


# In[131]:


round(3.55,2)


# In[133]:


2 **10


# In[136]:


pow(2,10)
len("niraj")


# In[149]:


### lists ###########
participants = ["john","lelila", "gauri", "cate"]
#### indexing ##################33
participants[1]


# In[145]:


participants[-2]


# In[151]:


## assigning value ########
participants[3]="maria"
######## to del variabl ####
del participants[2]
participants


# In[154]:


####################################  append ##########

participants = ["john","lelila", "gauri", "cate"]
participants.append("divya")
participants


# In[157]:



participants.extend(["divya2","dheeraj"])
participants


# In[159]:


print("The first participant is " + participants[0] + '.')


# In[160]:


len(participants)


# In[161]:


######### methods ###########
participants[1:3]


# In[162]:


participants[:2]


# In[163]:


participants[4:]


# In[165]:


participants[-2:]


# In[167]:


participants.index("dheeraj")


# In[170]:


newcomers = ["amit","bob"]


# In[174]:


bigger_list = [ participants, newcomers]


# In[177]:


bigger_list.sort()


# In[179]:


bigger_list.sort(reverse=True)


# In[180]:


### Tuples ###########
x = (1,2,3,4)


# In[181]:


y = 25,56,35


# In[184]:


a,b,c = 1,2,3
c


# In[186]:


list1=[x,y]
list1


# In[190]:


(age,years_of_school) = "30,17".split(',')
print(age)
print(years_of_school)


# In[193]:


def square_info(x):
    A=x**2
    P=4*x
    print("area and perimeter")
    return A,P


# In[194]:


square_info(3)


# In[196]:


x = (40,41,42)
x


# In[197]:


y = 35,45,23


# In[198]:


x[0]


# In[200]:


list = [x,y]
list


# In[203]:


(age,years_of_age) = "30,14".split(",")
print(age)
print(years_of_age)


# In[205]:


dict = {"k1":"cat","k2":"dog","k3":"mouse","k4":"fish"}
dict


# In[210]:


dict['k3'] = "parrot"
dict


# In[211]:


team = {}
team["point guard"] = "dirk"
team["shootings guard"] = "AI"
team['small forward'] = "sean"
team


# In[212]:


print(team.get('guard'))


# In[2]:


even = [0,2,4,6,8,10,12,14,16,18]


# In[3]:


for n in even :
    print(n, end = " ")


# In[8]:


x = 0
while x <= 20 :
    print(x, end = " " )
    x +=  2


# In[11]:


######## Range #############################
#range(start,  stop, step)
#range(10)
list(range(10))


# In[16]:


list(range(3,7))
list(range(1,20,2))


# In[21]:


for n in range(10):
    print(2**n, end = " ")


# In[30]:


for x in range(20):
    if x % 2 == 0 :
        print("even number is " , x  , end = " ")
    else :
        print("odd number is ",x , end = " ")
    


# In[45]:


x = [0,1,2]


# In[35]:


for item in range(len(x)) :
    print(x[item], end = " ")


# In[39]:


def count(numbers):
    total = 0 
    for x in numbers :
        if x <20:
            total +=1
    return total       
            


# In[48]:


list_1 = [1,2,3,4,5,6,7,21,22,25]
count(list_1)


# In[73]:


#### iterating over dictionaries #########
prices = {"box_of_strength" : 4,
         "lsagna" : 5,
         "humburger" : 0}
quantity =  {"box_of_strength" : 6,
             "lsagna" : 10,
             "humburger" : 0

    
}

money_spent = 0

for i in prices :
    money_spent = money_spent + (prices[i]*quantity[i])
    
print("money_spent is" , money_spent)    
    
   
    

   
    


# In[74]:



x = 0

for i in prices :
    x = x + (prices[i]*quantity[i])
    
print(x)    
    
   
    


# In[77]:


### OOP ###########
import math


# In[79]:


math.sqrt(16)


# In[81]:


from math import sqrt as s


# In[83]:


s(36)


# In[85]:


import math as m


# In[88]:


help (math)


# In[90]:


help(math.sqrt)


# In[92]:


import numpy as np #### allowing us to work with multidimensional arrays
import pandas as pd ## organise data in tabeluar form 
import matplotlib
import math  #### mathematical functions
import random
import statsmodels
import pandas_datareader


# In[93]:


## all the arrays must be same data type ########


# In[94]:


import numpy as np


# In[99]:


a = np.array([[0,1,2,3],[4,5,6,7]])
a


# In[100]:


a.shape


# In[102]:


a[1,2]


# In[103]:


a[1,2]=8


# In[110]:


b = np.array([3,5])### matrix is a two dimensional of data
b


# In[112]:


import random


# In[114]:


prob = random.random()
print(prob)


# In[118]:


number = random.randint(1,6)
print(number)


# In[119]:


np.random.randint(1,6,(4,6))


# In[ ]:





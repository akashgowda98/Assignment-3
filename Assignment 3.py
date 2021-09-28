#!/usr/bin/env python
# coding: utf-8

# In[8]:


def sum(numbers):
    total=0
    for x in numbers:
        total += x
    return total
print(sum((8,2,3,0,7)))


# In[25]:


def reverse(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1
print(reverse("1234abcd"))


# In[63]:


def upp_low(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in s:
        if i.isupper():
           d["UPPER_CASE"]+=1
        elif i.islower():
           d["LOWER_CASE"]+=1
        else:
            pass
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

upp_low('The quick Brow Fox')


# In[ ]:





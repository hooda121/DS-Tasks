#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Question 1

for i in range(5):
    if i!=0:
        print(i*"ineroun ")


# In[657]:


#Question 2

a = 3

for i in range(a+1):
    for j in range(a,i,-1):
        print(" "*len("ineuron"),end = " ")
    for k in range(i+1):
        if k==0 or k%2==0:
            print("ineuron",end = " ")
        else:
            print(" "*len("ineuron"),end = " ")
    for l in range(i):
        print("ineuron",end = " ")
    print("\n")
    
for i in range(a+1):
    for j in range(i):
        print(" "*len("ineuron"),end = " ")
    for k in range(a,i,-1):
        if k==0 or k%2==0:
            print("ineuron",end = " ")
        else:
            print(" "*len("ineuron"),end = " ")
    for l in range(a,i-1,-1):
        print("ineuron",end = " ")
    print("\n")


# 

# In[636]:


#Dataset

l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"sudh", "k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]


# In[452]:


type(l)


# In[638]:


#Question 3

for i in l:
    if type(i) == list:
        print (i)
        for a in i:
            print ("list entities",a)


# In[639]:


#Question 4

for i in l:
    if type(i) == dict:
        #print (i)
        for a in i.items():
            print (a[0], a[1])


# In[640]:


#Question 5

for i in l:
    if type(i) == tuple:
        #print (i)
        for a in i:
            print(a)


# In[507]:


l


# In[500]:


#Question 6

for i in l:
    #print(i)
    if type(i) == dict:
            for j,k in i.items():
                if type(j)==int or type(k)==int:
                    print(j)
                    print(k)
    else:
        for a in i:
            if type(a)==int:
                print(a)


# In[514]:


#Question 7

l1 = []
for i in l:
    #print(i)
    if type(i) == dict:
            for j,k in i.items():
                if type(j)==int or type(k)==int:
                    #print(j)
                    #print(k)
                    l1.append(j)
                    l1.append(k)
    else:
        for a in i:
            if type(a)==int:
                #print(a)
                l1.append(a)

print(l1)
b=0
for a in l1:
    b=b+a
print("Total sum", b)


# In[538]:


#Question 8
l2 = l
#print(l2)
for i in l2:
    #print(i)
    if type(i) == list:
        for a in i:
            if type(a) == int and a%2!=0:
                print(a)


# In[550]:


l2


# In[554]:


#Question 9

for i in l2:
    #print(i)
    if type(i)==dict:
        for j,k in i.items():
            if j=="ineuron" or k=="ineuron":
                print(i,j,k)
    else:
        for a in i:
                if a=="ineuron":
                    print(i,a)
                


# In[641]:


#Question 10

l3=[]
s={}
for i in l2:
    if type(i) == dict:
            for j,k in i.items():
                    l3.append(j)
                    l3.append(k)
    else:
        for a in i:
                l3.append(a)
#print(l3)
s=set(l3)
for i in s:
    print(i,l3.count(i))


# In[603]:


#Question 11

l4=[]
for i in l:
    #print(i)
    if type(i)==dict:
            for a in i.items():
                l4.append(a[0])

print(len(l4))


# In[582]:


l


# In[605]:


#Question 12

for i in l:
    #print(i)
    if type(i) == dict:
            for j,k in i.items():
                if type(j)==str or type(k)==str:
                    print(j)
                    print(k)
    else:
        for a in i:
            if type(a)==str:
                print(a)


# In[617]:


#Question 13

l5=[]

for i in l:
    #print(i)
    if type(i) == dict:
            for j,k in i.items():
                    l5.append(j)
                    l5.append(k)
    else:
        for a in i:
                l5.append(a)
                
                
for i in l5:
        if type(i)== str:
            if i.isalpha() == True:
                print(i.isalpha(), i,type(i),"yes")


# In[619]:


#Question 14

l1 = []
for i in l:
    #print(i)
    if type(i) == dict:
            for j,k in i.items():
                if type(j)==int or type(k)==int:
                    #print(j)
                    #print(k)
                    l1.append(j)
                    l1.append(k)
    else:
        for a in i:
            if type(a)==int:
                #print(a)
                l1.append(a)

print(l1)
b=1
for a in l1:
    b=b*a
print("Total product", b)


# In[620]:


#Question 15

l6=[]
for i in l:
    if type(i) == dict:
            for j,k in i.items():
                    l6.append(j)
                    l6.append(k)
    else:
        for a in i:
                l6.append(a)
print(l6)


# In[ ]:





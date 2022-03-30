#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

def unreliable_transmission(dataword, prob):
    #initiate data
    pick = prob
    not_pick = 1 - prob
    dataword = list(dataword)
    
    #We assign 1 to be pick if pick then corrupted the bit
    arr = [1, 2]
    #This mean the if pick(input prob = 0.05) not pick will be 0.95 or 5% and 95%. 5% that 1 will be pick
    distribution = [pick, not_pick]
    
    #if flag = 1 mean is bit is corrupted
    flag = 0
    #Loop to corrupted the bit in bit string
   
    for i in range(0,len(dataword)):
        
        random_number = random.choices(arr, distribution)
        #if 1 is pick mean that this bit will be corrupted and alter the bit value
        if(random_number == [1]):
            flag = 1
            if(dataword[i] == '1'):
                dataword[i] = '0'
            elif(dataword[i] == '0'):
                dataword[i] = '1'
            #this else mean spacebar
            else:
                pass
    #print("".join(dataword))
    return flag


# In[5]:


count = 0
for i in range(0,100):

    flag = unreliable_transmission('10001', 0.05)
    if(flag == 1):
        count+=1
        #print('corrupted frame')
    else:
        #print('uncorrupted frame')
        pass
        
print(str(count) + '%')


# In[6]:


count = 0
for i in range(0,100):

    flag = unreliable_transmission('10001', 0.1)
    if(flag == 1):
        count+=1
        #print('corrupted frame')
    else:
        #print('uncorrupted frame')
        pass
        
print(str(count) + '%')


# In[7]:


count = 0
for i in range(0,100):

    flag = unreliable_transmission('10001', 0.2)
    if(flag == 1):
        count+=1
        #print('corrupted frame')
    else:
        #print('uncorrupted frame')
        pass
        
print(str(count) + '%')


# In[ ]:





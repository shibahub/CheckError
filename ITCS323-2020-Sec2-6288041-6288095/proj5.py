#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Hamming_gen(dataword):
    
    #Change to be 7 bits string
    temp = list(dataword.zfill(7))
    
    # 'x' is the position of the checker
    if(len(temp) > 7):
        print('bit string exceed size of 7')
    else:

        arr = ['', '', '', 'x', '', '', '', 'x', '', 'x', 'x']
        #index 0   1   2    3   4   5   6    7   8    9   10
        count = 0
        #out put bit is 11 bits x indicate the prosition of the checker
        for i in range(0,11):
            if(arr[i] !='x'):
                arr[i] = temp[count]
                count+=1
        #checker bit
        r1 = 0
        r2 = 0
        r4 = 0
        r8 = 0
        for i in range(0,len(arr)):
            # for r1
            if((i==8 or i==6 or i==4 or i==2 or i==0) and arr[i] == '1'):
                r1+=1

            # for r2
            if((i==8 or i==5 or i==4 or i==1 or i==0) and arr[i] == '1'):
                r2+=1

            # for r4
            if((i==4 or i==5 or i==6) and arr[i] == '1'):
                r4+=1

            # for r8
            if((i==0 or i==1 or i==2) and arr[i] == '1'):
                r8+=1
        
        
        #checker if each checker bit is odd or even then add to the r1,r2,r4,r8
        if(r1%2 == 0):
            arr[10] = '0'
        else:
            arr[10] = '1'


        if(r2%2 == 0):
            arr[9] = '0'
        else:
            arr[9] = '1'


        if(r4%2 == 0):
            arr[7] = '0'
        else:
            arr[7] = '1'


        if(r8%2 == 0):
            arr[3] = '0'
        else:
            arr[3] = '1'
            
        print('result: ', end='')
        for i in arr:
            print(i, end='')
        print('\n**********************************************')


# In[3]:


Hamming_gen('101001')
Hamming_gen('1001101')
Hamming_gen('10001')
Hamming_gen('0000101')
Hamming_gen('100011')
Hamming_gen('0000101')
Hamming_gen('100111')
Hamming_gen('1001')
Hamming_gen('00101')
Hamming_gen('1110001')


# In[136]:


#arr =['', '', '', 'x', '', '', '', 'x', '', 'x', 'x']
#index 0   1   2    3   4   5   6    7   8    9   10
        
def Hamming_check(codeword):
    
    #need to be 11 bit
    data = list(codeword.zfill(11))

    r1 = 0
    r2 = 0
    r4 = 0
    r8 = 0

    for i in range(0,len(data)):
        # for r1
        if((i==8 or i==6 or i==4 or i==2 or i==0) and data[i] == '1'):
            r1+=1
        # for r2
        if((i==8 or i==5 or i==4 or i==1 or i==0) and data[i] == '1'):
            r2+=1
        # for r4
        if((i==4 or i==5 or i==6) and data[i] == '1'):
            r4+=1
        # for r8
        if((i==0 or i==1 or i==2) and data[i] == '1'):
            r8+=1

    checker = []
    #Check the checker if correct put 0 if not correct put 1
    if(r8%2 == 0 and data[3] == '0'):
        checker.append('0')
    elif(r8%2 == 0 and data[3] == '1'):
        checker.append('1')
    elif(r8%2 != 0 and data[3] == '0'):
        checker.append('1')
    elif(r8%2 != 0 and data[3] == '1'):
        checker.append('0')


    if(r4%2 == 0 and data[7] == '0'):
        checker.append('0')
    elif(r4%2 == 0 and data[7] == '1'):
        checker.append('1')
    elif(r4%2 != 0 and data[7] == '0'):
        checker.append('1')
    elif(r4%2 != 0 and data[7] == '1'):
        checker.append('0')


    if(r2%2 == 0 and data[9] == '0'):
        checker.append('0')
    elif(r2%2 == 0 and data[9] == '1'):
        checker.append('1')
    elif(r2%2 != 0 and data[9] == '0'):
        checker.append('1')
    elif(r2%2 != 0 and data[9] == '1'):
        checker.append('0')


    if(r1%2 == 0 and data[10] == '0'):
        checker.append('0')
    elif(r1%2 == 0 and data[10] == '1'):
        checker.append('1')
    elif(r1%2 != 0 and data[10] == '0'):
        checker.append('1')
    elif(r1%2 != 0 and data[10] == '1'):
        checker.append('0')
    
    #if no error found flag = 0 then return -1
    flag = 0;
    for i in checker:
        if(i == '1'):
            flag=1
    if(flag == 1):
        sum = (8*int(checker[0])) + (4*int(checker[1])) + (2*int(checker[2])) + (1*int(checker[3]))
        print(sum)
    else:
        print(-1)


# In[138]:


Hamming_check('01011001110')
Hamming_check('10011100101')
Hamming_check('00110000110')
Hamming_check('01010011100')
Hamming_check('00001001100')
Hamming_check('00001101100')
Hamming_check('01000101101')
Hamming_check('00010101101')
Hamming_check('01000101101')
Hamming_check('00000101100')


# In[ ]:





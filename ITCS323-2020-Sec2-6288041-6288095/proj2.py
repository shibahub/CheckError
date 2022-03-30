#!/usr/bin/env python
# coding: utf-8

# In[13]:


def parity_gen(word, parity_type):
    
    #Method of transforming a word to binary string
    temp = word
    asci = [ord(c) for c in word]
    array = []
    for i in range(0,len(asci)):
        array.append(asci[i])
        
    dataword = []
    print('The word is: ' + word)
    print('parity type: ' + parity_type)
    for i in range(0,len(array)):
        dataword.append(format(array[i],'b').zfill(7))
    ######## Maximum value of word in ascii = 7 bit ##########################################
    
    
    #Choose the type of the parity to generate
    if(parity_type == 'one-dimensional-even'):
        even_parity_1dim(dataword)
        
    elif(parity_type == 'one-dimensional-odd'):
        odd_parity_1dim(dataword)
        
    elif(parity_type == 'two-dimensional-even'):
        even_parity_2dim(dataword)
        
    elif(parity_type == 'two-dimensional-odd'):
        odd_parity_2dim(dataword)
    
    
def even_parity_1dim(dataword):
    codeword = []
    #Loop through the dataword
    for i in range(0,len(dataword)):
        count = 0
        for j in range(0,len(dataword[i])):
            if(dataword[i][j] == '1'):
                #count to calculate if the count is even or odd number
                count+=1
        #add the parity bit to the last+1 index
        if(count%2 == 0):
            codeword.append(dataword[i] + '0')
        else:
            codeword.append(dataword[i] + '1')
    #print to show the result
    for i in codeword:
        print(i, end=' ')
    print('\n******************************************************************************')

    
def odd_parity_1dim(dataword):
    codeword = []
    #Loop through the dataword
    for i in range(0,len(dataword)):
        count = 0
        for j in range(0,len(dataword[i])):
            if(dataword[i][j] == '1'):
                #count to calculate if the count is even or odd number
                count+=1
        #add the parity bit to the last+1 index
        if(count%2 == 0):
            codeword.append(dataword[i] + '1')
        else:
            codeword.append(dataword[i] + '0')
    #print to show the result
    for i in codeword:
        print(i, end=' ')
    print('\n******************************************************************************')
    
    
def even_parity_2dim(dataword):
    codeword = []
    temp = ""
    #This method is similar to the 1 dimension parity
    for i in range(0,len(dataword)):
        count = 0
        for j in range(0,len(dataword[i])):
            if(dataword[i][j] == '1'):
                count+=1
        if(count%2 == 0):
            temp+='0'
            codeword.append(dataword[i] + '0')
        else:
            temp+='1'
            codeword.append(dataword[i] + '1')

            
    
    m = ''
    #Loop through each column
    for i in range(0,len(dataword[-1])):
        c = 0
        #Method to generate redundant bit from the column
        for j in range(0,len(dataword)):
            if(dataword[j][i] == '1'):
                c+=1
        if(c % 2 == 0):
            m+='0'
        else:
            m+='1'


    hi = 0
    #The redundant bit that we calculate from the column to add to the add the last parity bit
    for i in range(0,len(m)):
        if(m[i] == '1'):
            hi+=1
    if(hi%2 == 0):
        m+='0'
    else:
        m+='1'
    
    #print the codeword
    codeword.append(m)
    for i in codeword:
        print(i, end=' ')
    print('\n******************************************************************************')
    
    
def odd_parity_2dim(dataword):
    codeword = []
    temp = ""
    #This method is similar to the 1 dimension parity
    for i in range(0,len(dataword)):
        count = 0
        for j in range(0,len(dataword[i])):
            if(dataword[i][j] == '1'):
                count+=1
        if(count%2 == 0):
            temp+='1'
            codeword.append(dataword[i] + '1')
        else:
            temp+='0'
            codeword.append(dataword[i] + '0')
            
            

    m = ''
    #Loop through each column
    for i in range(0,len(dataword[-1])):
        c = 0
         #Method to generate redundant bit from the column
        for j in range(0,len(dataword)):
            if(dataword[j][i] == '1'):
                c+=1
        if(c % 2 == 0):
            m+='1'
        else:
            m+='0'

    hi = 0
    #The redundant bit that we calculate from the column to add to the add the last parity bit
    for i in range(0,len(m)):
        if(m[i] == '1'):
            hi+=1
    if(hi%2 == 0):
        m+='1'
    else:
        m+='0'
    
    codeword.append(m)
    #print the codeword
    for i in codeword:
        print(i, end=' ')
    print('\n******************************************************************************')


# In[14]:


parity_gen('g]9)', 'one-dimensional-even')
parity_gen('g]9)', 'one-dimensional-odd')
parity_gen('g]9)', 'two-dimensional-even')
parity_gen('g]9)', 'two-dimensional-odd')
parity_gen('Hello World', 'one-dimensional-even')
parity_gen('Hello world', 'one-dimensional-odd')
parity_gen('Hello wolrd', 'two-dimensional-even')
parity_gen('Hello world', 'two-dimensional-odd')
parity_gen('MUICT NO1 THAILAND', 'two-dimensional-even')
parity_gen('MUICT NO1 THAILAND', 'two-dimensional-odd')


# In[8]:


def parity_check(codeword,parity_type):
    #input as the following '10010 1110010 1111001...........'
    dataword = codeword.split(' ')
    Max = len(dataword[0])
    for i in range(0,len(dataword)):
        count = 0
        for j in range(0, len(dataword[i])):
            count+=1
        if(int(count) > int(Max)):
            Max = count
            
            

    print('parity_type: ' + parity_type)
    for i in dataword:
        print(i, end=' ')
    #To make all bit string equal size accroding to the longest size
    for i in range(0, len(dataword)):
        dataword[i] = dataword[i].zfill(Max)
    

    #choose method if return 0 it mean that its FAIL else PASS
    if(parity_type == 'one-dimensional-even'):
        if(even_parity_1dim_check(dataword) == 0):
            print('\nFAIL')
            print('******************************************************************************')
        else:
            print('\nPASS')
            print('******************************************************************************')
            
    elif(parity_type == 'one-dimensional-odd'):
        if(odd_parity_1dim_check(dataword) == 0):
            print('\nFAIL')
            print('******************************************************************************')
        else:
            print('\nPASS')
            print('******************************************************************************')
    

    elif(parity_type == 'two-dimensional-even'):
        if(even_parity_2dim_check(dataword) == 0):
            print('\nFAIL')
            print('******************************************************************************')
        else:
            print('\nPASS')
            print('******************************************************************************')

    elif(parity_type == 'two-dimensional-odd'):
        if(odd_parity_2dim_check(dataword) == 0):
            print('\nFAIL')
            print('******************************************************************************')
        else:
            print('\nPASS')
            print('******************************************************************************')


        
def even_parity_1dim_check(dataword):
    #Check through each row normally
    for i in range(0, len(dataword)):
        count = 0
        for j in range(0, len(dataword[i])-1):
            
            if(dataword[i][j] == '1'):
                count+=1
                
        if(count%2 == 0 and dataword[i][-1] == '1'):
            return 0
        if(count%2 != 0 and dataword[i][-1] == '0'):
            return 0
    return 1
    #return 1 if correct or return 0 if not correct

def odd_parity_1dim_check(dataword):
    #Check through each row normally
    for i in range(0, len(dataword)):
        count = 0
        for j in range(0, len(dataword[i])-1):
            
            if(dataword[i][j] == '1'):
                count+=1
                
        if(count%2 == 0 and dataword[i][-1] == '0'):
            return 0
        if(count%2 != 0 and dataword[i][-1] == '1'):
            return 0
    return 1
    #return 1 if correct or return 0 if not correct

def even_parity_2dim_check(dataword):
    #checkแนวตั้ง
    for i in range(0,len(dataword[-1])-1):
        t = 0
        for j in range(0,len(dataword)-1):
            if(dataword[j][i] == '1'):
                t+=1
        if(t%2 == 0 and dataword[-1][i] != '0'):
            return 0
            
        if(t%2 != 0 and dataword[-1][i] != '1'):
            return 0
        
    #checkแนวนอน        
    for i in range(0, len(dataword)):
        l = 0
        for j in range(0, len(dataword[i])-1):
            
            if(dataword[i][j] == '1'):
                l+=1
                
        if(l%2 == 0 and dataword[i][-1] != '0'):
            return 0
        if(l%2 != 0 and dataword[i][-1] != '1'):
            return 0
    return 1
    #return 1 if correct or return 0 if not correct


def odd_parity_2dim_check(dataword):
    #checkแนวตั้ง
    for i in range(0,len(dataword[-1])-1):
        t = 0
        for j in range(0,len(dataword)-1):
            
            if(dataword[j][i] == '1'):
                t+=1
        if(t%2 == 0 and dataword[-1][i] != '1'):
            return 0
            print('hello')
        if(t%2 != 0 and dataword[-1][i] != '0'):
            return 0
            print('hello')
        
    #checkแนวนอน        
    for i in range(0, len(dataword)):
        l = 0
        for j in range(0, len(dataword[i])-1):
            
            if(dataword[i][j] == '1'):
                l+=1
        if(l%2 == 0 and dataword[i][-1] != '1'):
            return 0
        if(l%2 != 0 and dataword[i][-1] != '0'):
            return 0
    return 1
    #return 1 if correct or return 0 if not correct


# In[11]:


#USE THE number from the parity generator it should ALL PASS
parity_check('11001110 10111010 01110011 01010010','one-dimensional-odd')
parity_check('11001111 10111011 01110010 01010011','one-dimensional-even')
parity_check('11001111 10111011 01110010 01010011 01010101','two-dimensional-even')
parity_check('11001110 10111010 01110011 01010010 10101011','two-dimensional-odd')
parity_check('10010001 11001011 11011001 11011001 11011111 01000000 11101111 11011111 11100101 11011001 11001000','one-dimensional-odd')
parity_check('10010000 11001010 11011000 11011000 11011110 01000001 10101111 11011110 11100100 11011000 11001001','one-dimensional-even')
parity_check('10010000 11001010 11011000 11011000 11011110 01000001 11101110 11011110 11011000 11100100 11001001 00000000','two-dimensional-even')
parity_check('10010001 11001011 11011001 11011001 11011111 01000000 11101111 11011111 11100101 11011001 11001000 11111110','two-dimensional-odd')
#This is the last 2 bit string that PASS but I will change the bit to check if it FAIL or not ; it should fail
parity_check('10010000 11001010 11011000 11011000 11011110 01000001 11101110 11011110 11011000 11100100 11001001 11100000','two-dimensional-even')
parity_check('10010001 11001011 11011001 11011001 11011111 01000000 11101111 11011111 11100101 11011001 11001000 10111110','two-dimensional-odd')


# In[ ]:





# In[ ]:





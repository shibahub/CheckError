#!/usr/bin/env python
# coding: utf-8

# In[10]:


def exceedbit(code):
    counter=0
    tmp=''
    tmp2=''
    x=""
    y=""
    for i in reversed(code):
        if counter<7:
            #arr2.extend(i)
            x+=i
        else:
            #arr3.extend(i)
            y+=i
        counter+=1;
    for i in reversed(x):
        tmp+= i
    for i in reversed(y):
        tmp2+= i
    print("Tmp1:")
    print(tmp)
    print("Tmp2:")
    print(tmp2)
    print("result")
    ch=int(tmp,2)+int(tmp2,2)
    #print(ch)
    return ch
def comple(code):
    st=''
    st2=''
    print('Before 1 complement:')
    for i in reversed(code):
        st+=i
    print(st)
    for i in st:
        if i=='1':
            st2+='0'
        else:
            st2+='1'
    print('After 1 complement:')
    print(f'Check sum is {st2}')
    return st2
def bincon(code):
    ch=code
    binchecksum=bin(ch)
    word=binchecksum.split('b')
    binchecksum=word[1]
    print("sum")
    print(binchecksum)
    return binchecksum
def sumofbin(code):
    arr=code
    sum=0
    for i in arr:
        sum= sum+i
    code=bin(sum)
    word= code.split('b')
    code=word[0]+word[1]
    print('code')
    print(code)
    return code
def checksum(dataword, word_size): #main function to check sum
    sum=0
    code=[]
    arr=[]
    arr2=[]
    rev=[]
    st=""
    st2=""
    tmp=''
    binofcodeword=[]
    adder=0
    arrofbinary=[]
    #print(word_size)
    codeword=dataword
    for i in codeword:
        arr.extend(ord(num) for num in i)
    print(arr)
    code= sumofbin(arr) #sum of ascii
    ch = exceedbit(code) #Sum of exeed bit that more than 7
    binchecksum = bincon(ch)# split ('b') of the string
    arr2.append(binchecksum)
    while (adder+len(binchecksum)<7): # to check that our bit is 4 or not
        arr2+='0'
        adder+=1
    st2 = comple(arr2)# complement 
    #print(f'st2 is here {st2} {type(st2)}')
    adder=0
    sum=0
    for i in reversed(st2):
        sum+= int(i)*(2**adder)
        adder+=1
    sum
    print('*************************')
    print('Checking method')
    for i in arr:
        sum+=i
    #print(sum)
    st2 = bincon(sum) #split b out
    st2= exceedbit(st2) #sum exeedbit
    st2= bincon(st2)#split b out
    st2= comple(st2) #complement
    count=0
    for i in st2: #check that data correct or not
        if i=='0':
            count+=1
    if(count==7):
        print('Your data is correct')
codeword = str(input('Codeword: '))
checksum(codeword,len(codeword))


# In[ ]:





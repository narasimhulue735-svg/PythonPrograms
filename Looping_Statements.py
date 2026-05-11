'''There are two looping statements are there
1.for loop
2.While loop
for loop:we can aware of no.of iterations
while loop:it is depends on condition
i want to print 1-10 numbers
print(1)
print(2)
print(3)
.
.
print(10)
like this we will print it
use for loop and while loop we can easy to print all numbers
'''
# for i in range(1,11):
#     print(i)
# l1=[]
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     l1.append(i*i)
# print(l1)
# '''print vowels in string'''
# name="narasimhulu naidu"
# vowels="aeiou"
# for i in name:
#     if i in vowels:
#         print(i)
# '''`count the number of letters in a string by using dictionary key,value pairs'''
# d={}
# name1="python automation testing"
# for i in name1:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i] +=1
# print(d)
'''split a string by giving width'''
# def string_spliting_by_width(string,max_width):
#    for i in range(0,len(string),max_width):
#         print(string[i:i+max_width])
# string=input("enter the str:")
# max_width=int(input("enter the max width:"))
# string_spliting_by_width(string,max_width)
'''while loop syntax
while condition:
          code
'''
# while True:
#     print("Hello")
# n=1
# while n<=10:
#     print(f"Hello world: {n}")
#     n+=1

'''
control flow statements:
There are three types of statements
1.break:terminate the entire loop and break is executed no code execute
2.continue:it will skip the current iteration and continue the loop
3.pass:it's placeholder,whenever we need syntax purpose we can use for creating empty class,method,etc
'''
'''1.break'''
# l=[12,23,12,435,546,24,4]
# for i in l:
#     if i==435:
#         break
#     print(i)
'''printing the prime numbers between the range'''
# def prime_or_not(n,m):
#     for i in range(n,m+1):
#         if i>1:
#             for j in range(2,int(i**0.5)+1):
#                 if i%j==0:
#                     break
#             else:
#                 print(i)
# n=int(input("Enter a number:"))
# m=int(input("Enter another number:"))
#prime_or_not(n,m)
'''first non repeating char'''
# n="narasimhulu naidu"
# for i in n:
#     if n.count(i)==1:
#         print(i)
#         break
'''second non repeating char'''
# n="python automation"
# c=0
# for i in n:
#     if n.count(i)==1:
#         c+=1
#         if c==2:
#             print(i)
#             break
'''2.continue'''
# l1=[12,23,12,435,546,24,4]
# for i in l1:
#     if i==12:
#         continue
#     print(i)
'''3.pass'''
# l2=[12,23,12,435,546,24,4]
# for i in l2:
#     if i==12:
#         pass
#     print(i)
'''print count the frequency of each word in a sentence.'''
# def sentence(n):
#     words=n.split()
#     d={}
#     for i in words:
#         if i not in d:
#               d[i]=1
#         else:
#               d[i]+=1
#     return d
# n=input("enter the sentence:")
# print(sentence(n))
'''list of integers, return the two numbers that add up to a target value.'''
# def add_target_value(nums, target):
#     seen = {}
#     for num in nums:#[2,3,4,5,6,7]
#         diff = target - num
#         if diff in seen:
#             print(diff, num)
#         seen[num] = True
# n=list(map(int,input("Enter the list of integers:").split()))
# t=int(input("Enter the target value:"))
# add_target_value(n,t)
# def multiply_with_index(n):
#     a=[]
#     for i in n:
#         a.append(i**i)
#
#     return a
# n=list(map(int,input("enter the nums:").split()))
# print(multiply_with_index(n))

# def reverse_string(n):
#     a=''
#     for i in n:
#         a=i+a
#     return a
# n=input("enter the nums:")
# print(reverse_string(n))
# def maximum_price(n):
#     min_price=n[0]
#     max_price=0
#     for i in n:
#         if i<min_price:
#             min_price=i
#         else:
#             profit=i-min_price
#             max_price=max(max_price,profit)
#     return max_price
# n=list(map(int,input("Enter the list of numbers:").split()))
# print(maximum_price(n))

# def find_missing_and_duplicate(arr):
#     n=len(arr)
#     s=set()
#     duplicate=-1
#     for i in arr:
#         if i in s:
#             duplicate=i
#         s.add(i)
#     total_sum=n*(n+1)//2
#     missing=total_sum-(sum(arr)-duplicate)
#     return duplicate,missing
# arr=list(map(int,input("enter the list of numbers:").split()))
# print(find_missing_and_duplicate(arr))
'''count the numbers in form of key value pair'''
# l=[1,2,3,4,5]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
'''patterns in python'''
# n=int(input("Enter a number"))
# for i in range(n):
#     for j in range(n-i,0,-1):
#             print(chr(94),end=' ')
#     print()
# m=int(input("Enter a number"))
# num=1
# for i in range(1,m):
#     for j in range(i):
#             print(num,end=' ')
#             num+=1
#     print()
'''pattern in form of 
A
AB
ABC
ABCD
ABCDE'''
v=int(input("Enter the num:"))
for i in range(1,v):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

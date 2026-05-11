'''function:function is a block of code that will execute once we called the function with function name
inbuilt functions:functions are that are already defined in python itself
just we call those functions and execute it
example:len(),id(),type(),dir()
user defined functions:we can define by using def keyword
we can reusable code we can write
function can have args and it will return the values as well
by using return we can return values,once return is executed function will terminated.
only one return statement is executed in a function

syntax:
def function_name(): #fuction definatin
    #function body
function_name()  #function calling
'''
# def memory_location(a):
#     return id(a) #id is a function and a is  parameter/arguments
# print(memory_location(a)) #it will return memory location
# def greet(name):
#     print('hello',name)
# greet(name="Naidu")
# greet("Narasimhulu")
# greet("Python Automation")
'''geting the non repeating character from string'''
# print("getting non-repeating char :")
# def get_non_repeating_char(name,n):
#     c=0
#     for i in name:
#         if name.count(i)==1:
#             c+=1
#             if c==n:
#                 return i
# name=input("enter your name:")
# n=int(input("enter your number:"))
# print(get_non_repeating_char(name,n))
'''check the string is a anagram or not'''
# def check_anagram(s1,s2):
#     a=s1.lower()
#     b=s2.lower()
#     if sorted(a)==sorted(b):
#         return True
#     else:
#         return False
# s1=input("enter the first string")
# s2=input("enter the second string")
# print(check_anagram(s1,s2))
'''flatten a nested list'''
# def flatten_list(l):
#     l1=[]
#     for i in l:
#        if isinstance(i,list):
#            l1.extend(i)
#        else:
#            l1.append(i)
#     print(l1)
# l=[1,[2,3,[4,5,[6]]]]
# flatten_list(l)
'''infosys coding question 1:'''
# def solve(n,k,a):
#     a.sort()
#     count=0
#     i=0
#     while i<2*n-1:
#         if abs(a[i]-a[i+1])<=k:
#             count+=1
#             i+=2
#
#         else:
#             i+=1
#     return count
# n=int(input("Enter the num:"))
# k=int(input("Enter the key:"))
# a=list(map(int,input("Enter the list:").split()))
# print(solve(n,k,a))
'''function arguments:
there are 4 types of arguments
1.positional arguments:it will take the values based on the position
2.keyword arguments:while calling the function name,we have provide key-value and it's not follow any order
3.default arguments:while defining the function,we are provide the default values
4.variable length arguments(*args) and keyword length arguments(**kwargs)'''
def adds(a,b,c=20):
    print(a+b+c)
adds(10,20)#positional args
adds(b=30,a=10)#keyword args
adds(10,20)#defalut args
def demo(name,course,place="hyderabad"): # parameters
    print(f"My name is {name} iam from {place}")

demo("Narasimhulu",place="bangalore",course="python") # arguments

demo("Naidu","java","Jharkhand")

# if non default argument follows default argument it will return error
# def check_prime_or_not(num):
#     if num>1:
#         return "not prime"
#     for i in range(2,num):
#         if num%i==0:
#                 return "not prime"
#         else:
#                 return "prime"
# num=int(input("enter the number"))
# print(check_prime_or_not(num))
def sum_of_nums(num1):
    n=0
    while num1>0:
        n+=num1%10
        num1//=10
    return n
print(sum_of_nums(12345))

print("IAM UPDATING INTO GIT")
print("chandrashekar")
print("C:\Program Files\Git\cmd")
print("python Automation")
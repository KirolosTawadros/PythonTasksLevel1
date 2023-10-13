Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha","kirolos","jimmy","reem","tamer","tommy","hamada"]

'''
Task Number 1
'''
# Normal Case
# new = []
# for x in Names:
#     new.append(x.upper())
# print(new)    
# -------------------------
# List Comprehension
# print([x.upper() for x in Names])
#------------------------------------
# Functional Programming
# print(list(map(lambda x: x.upper(),Names)))
# def myupper(n):
#     return n.upper()
# result = map(myupper,Names)
# print(list(result))
'''
Task Number 2
'''
## Normal Case:
# new = []
# for x in Names:
#     if "a" in x:
#         new.append(x)
# print (new)
## List Comperhension
# print(list(x for x in Names if "a" in x))
## Functional Programming:
# def char(n):
#     if "a" in n:
#         return n
# result = map(char,Names)
# print(list(result))
# result2 = filter(char,Names)
# print(list(result2))
'''
Task Number 3
'''
## Normal Case
# new = []
# for x in Names:
#     if x.startswith("t"):
#         new.append(x)
# print(new)
## List Comprehension
# print(list(x for x in Names if x.startswith("t")))
## Functional Programming
# def start(x):
#     if x.startswith("t"):
#         return x
# result = filter(start,Names)
# print(list(result))
'''
Task Number 4
'''  
## Normal Case 
# for x in Names:
#     if x.count("a") >= 2:
#         print(x)
## List Comprehension
# print(list(x for x in Names if x.count("a")>= 2))
## Fuctional Programming
# def letters(x):
#     if x.count("a")>=2:
#         return x
# result = filter(letters,Names)
# print(list(result))
'''
Task Number 5
'''
## Normal Case
# for x in Names:
#     length = len(x)
#     print(length)
## List Comprehension
# print(list(len(x) for x in Names))
## Functional Programming
# def length(x):
#     return len(x)
# result = map(length,Names)
# print (list(result))
'''
Task Number 7
'''
# a,*b = Names
# print(a)
# print(b)
'''
Task Number 8
'''
# a ,*_,b = Names
# print(a)
# print(b)
'''
Task Number 9
'''
# a,b,*_ = Names
# print(a)
# print(b)
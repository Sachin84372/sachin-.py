                                     # day12 # # string slicing #
a=("sachin,karan,himanshu,sonu,suraj,sumit,neeraj,satish")
print(a[0:4])
print(len(a))

b=("sachin kuamr")
length=len(b)
print("the name is",b,)
print("sachin kumar",length,"has words")# simple write the length of string

abc=("leaddy finger")  #string data type
vegitable=(len(abc))  #let vegitable =length of the abc
print(vegitable)  #give the output of vegitable=abc 

                                #basic of string slicing from index#
print(abc[0:6]) 
#it will print the first 6 letters of the abc

print(abc[:6])  
#it will print the first 6 letters of the abc

print(abc[:])   
#it will print the first 6 letters of the abc

print(abc[0:-4]) 
#it will print the first 8 letters  beause 12-4=8 of the abc

print(abc[-1:-6])
#it will print notihng letters of the abc

print(abc[-5:-1])  
#it will print the 8,9,10,11 letters of the abc

name=("sachin")    # quick quiz
sac=(len(name))
print(name[-4:-2])
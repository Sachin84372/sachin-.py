                                                                          #DAY 22#
                                         #today we learn about {LIST} in the python and how we can use it or apply the list                                        

#simple list program {known that how to use it }  and what is the why


nmuber=[1,4,3,6,78,45,5,56,45,45,34,5,34,5,23]
print(type(nmuber))      #type help to find that the data is which type {it is list type}

nmuber=(1,4,3,6,78,45,5,56,45,45,34,5,34,5,23)
print(type(nmuber))      #type help to find that the data is which type  {it is tuple type}   


nmuber={1,4,3,6,78,45,5,56,45,45,34,5,34,5,23}
print(type(nmuber))      #type help to find that the data is which type  {it is set type}   



                    ##using some list for batter understanding##
list=[1,3,5,6,87,65,43,45,67,97,94,32,1,34,56,45]   
print(list[0]) 
print(list[1])                    
print(list[2])    
print(list[3])    
print(list[4])    
print(list[5])    #for finidng the value need to khow the index #
print(list[6])        #same for all the list #
print(list[7])    
print(list[8])    
print(list[9])    
 

 #if any number is nagtive than how we can maqke it postive #

num=[1,3,5,6,87,65,43,]
print(num[-6])   #for understand it works how

print(num[len (num)-6]) #just we use the length of{} list to make the number postive } 


#by checking the number is that present in the list or not #
num1=[1,4,6,7,98,423,556,756,6]
if 556 in num1:
   print("yes")
else :
   print("no")
print(num1)


num1=[1,4,6,7,98,423,556,756,6]
if 55 in num1:
   print("yes")
else :
   print("no")
print(num1)


#using the slicing and jumping in the python on the list 

list2=[1,4,3,6,78,45,5,56,45,45,34,5,34,5,23]
print(list2[0:4])
print(list2[:])
print(list2[:4])  #all are counting from the zero  index #
print(list2[3:6])


#now writing some 2 level code for batter undersataning #

list3=[i for i in range(20)]
print (list3)  #this is we use range in the list #


list4=[i*i for i in range(40) if (i*i%2==0)] # it just add the number which is divisbal by the {2 becuse we give the conditon}
print (list4)

                                                                ### DAY 22 ### {END} ###
                                                                  ##TIME= 12:40 ##






                                                    # Day 31 and 32 { learning set and set method on the saem day } #
                                                                              #DAY 31#
# if you want to print the empty set than you can do like this  with {se()}
set={}
print(set)
print(type (set) ) # it was dic type 

# the set is not able to  print the same type of veriable and the set  give the output unordered meanes if you give input {1,2,3,4,5,6,7,} the  output come may be {7,4,5,3,6,1,2}
# example :-
set ={13,4,5,6,4,3,2,4,32}
print(set)

# the set do not contain the duplicate items [or the set are unorderedas you can see on upper side]

#we can store the diffrent type of variable in the sets
set={"sachin" ,2 ,3.5, "true"} 
print(set)

                                                        ##work of Day 32## #topic the methods of set in the python
                                                                               #DAY 32#
#UNINON [U]           SIGN (AUB)     
# the combination of the set is know as the know as the union where all the none repetable value comes in output in unordered 
set1={1,3,5,7,4,2}                                                            
set2={22,4,67,54,87,12}  # {4 is prestent on the set 1 or set2  but print only once becouse it do not cntain dublicate items}
print(set1.union(set2)) 

set1={1,3,5,7,4,2}                                                            
set2={22,4,67,54,87,12}  
print(set1,set2)  # if you want to print both of set seprate than it use {, coma}

set1={1,3,5,7,4,2}                                                            
set2={22,4,67,54,87,12}  
set1.update(set2)
print(set1,set2)  # if you want to update the set it use {.update}

#INTERSACTION [Q]           SIGN (AQB)      #########Q=INTERSACTION SIGN##########
# the combination of the set is know as the know as the union where all the none repetable value comes in output in unordered 

set1={1,3,5,7,4,2}                                                            
set2={22,4,67,54,87,12}  # 4 is prestent on the set 1 or set2  SO print only 
print(set1.intersection(set2)) 

set1={1,3,5,7,4,12}                                                            
set2={22,4,67,54,87,12}   
set1.intersection_update(set2) # it update when the value is match in the both of th set
print(set1)

#symmetric  method in the set :-
set1={1,3,5,7,4,12}                                                            
set2={22,4,67,54,87,12}   
set1.symmetric_difference(set2)  #[it print the diffren number do not print the same number]
print(set1)

 #diffrent and diffrent update :-

set1={1,3,5,7,4,12}                                                            
set2={22,4,67,54,87,12}   
set1.difference(set2)  #[it macth the number which is prsent is alos prsent in the other set so print ]
print(set1)


#there are some in build methods in the python for thwe set 

#1st method for set in the python  ##isdisjoint()##
num1={1,3,4,5,2}
num2={1,3,4,5,2}
print(num1.isdisjoint(num2)) #output comes false becouse num1 dose not match num2 all the number are being  not present in the set #


#2nd method for set in the python ##issuperset##
num1={1,3,4,5,2}
num2={1,3,4,5,2,}
print(num1.issuperset(num2))  #output comes true becouse num1 =num2 all the number are being present in the set #


#3rd method for set in the python ##issubset##
num1={1,3,4,5,2,43,56}
num2={1,3,4,5,2,43,56}
print(num1.issubset(num2))  #output comes true becouse num1 =num2 all the number are being present in the set.  in both it say false when no if any of the  number is same in the set #


#4th method for set in the python ##add##
number={1,3,4,5,2,43,56}
number.add(345)
print(number)  # the add() is use to add one variable in the sets 


#5th method for set in the python ##update##
number1={1,3,4,5,2,43,56}
number1.update({34,55,78,89})
print(number1)  # the update() is use to add one or more variable in the sets in one time


#6th method for set in the python ##remove##
number1={1,3,4,5,2,43,56}
number1.remove(56)
print(number1)  # the remove() tkae only one[1] input it help to remove the element from the set if the number is not present in the set it provide the error..


#7th method for set in the python ##discard##
number1={1,3,4,5,2,43,56}
number1.discard(43)
print(number1)  # the remove() tkae only one[1] input it help to remove the element from the set if the number is not present in the set it { DO NOT provide the error.. }


#8th method for set in the python ##pop##
number1={1,3,4,5,2,43,56}
number1.pop()
print(number1)  # the pop() help to . remove() the last variable of the set just by wrtting the pop()


#9th method for set in the python ##clear##
number1={1,3,4,5,2,43,56}
number1.clear()
print(number1)   # the clear(). delete all the variable which is provided in the number1 set  the output is empty


# #10th method for set in the python ##del##  ###NEED TO COMMNET OUT OTHER WIE THROW THIS ERROR
# number1={1,3,4,5,2,43,56}
# del number1
# print(number1)   # if we use the del than provide the the location  of deleting the set  {it wae deleted so throw the ERRORS DONT ne nervese}

### now using the if else condition in theset for the batter understanding 

sachin ={98,99,97,56,96,100}
if 100 in sachin  :
    print ("sachin is the good learner")
elif 98 in sachin :
    print ("sachin is okk okk learner ")
elif 56 in sachin :
    print("sachin is slow learner")
else:
    print("sachin is not good learner")  # the if else condition is use to in the sets on the python
 
                                                                            ###DAY 31,32 DONE DONE###
                                                                                ###TIMING=23:45###
                                                                    #DAY 21#
                                                ## larning the function arrgument in the python ## 
#### this is the just  basic code to write thwe function in the python####                                                
def adddivide (a,b,c):
    print("mean is ",(a+b)/c)

adddivide(4,50,6)

#there are four type of the arguments in function #
# default argument
# keywords argument
# variable length argument
# required argument

#1st argument {default argument}
# the default argument is the argument that is assigned a default value when it is not passed to the
def value1 (a=3,b=5):
    print("the multiple of the a and b",(a*b))
value1() # if we does not give any  value  on the section than it give the default output
    

def value1 (a=3,b=5):
    print("the multiple of the a and b",(a*b))
value1(5,6) # if we does give any  value  on the section than it give the  which we give the last input 


#it is a basic example for adding yor name or ser name#
def name (fname="sachin " ,mname="... ",lname ="kumar"):
    print("hii my dear ",fname ,mname ,lname)
name ("sachin"  , "coder " , "sahab")

# 2nd  is {keyword  argument }
value(b=3,c=45,a=4)# are can be write randomly{is know  as keyword arguments}

#3rd  is {required argument}
# in this we a requring to feel the value if you use it #
def number (a,b,c=65 ):
    print ("the sum is ",(a+b+c))
number(44,23)

#4th is variable argument
#this is code for just find the average number#
def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    print ("the average is: ",sum/len(number))
average(3,5,7,4,2,87,98,65,4,6,7,5,4,56,7864,5,64,87,654,5)


def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    return sum/len(number)  #the meaning of  return is jsut print the value and {move out from the loop}
c=average(2,3,4,5)
print(c) #in this it basiclly store the data in c#

                                        
                                        
                                                    ## DAY 21 DONE ## {TIME is 12:30AM}
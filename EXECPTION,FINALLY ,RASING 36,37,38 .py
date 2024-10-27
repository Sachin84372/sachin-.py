                                                #  [EXECPTION ERROR HENDLING  FINALLY KEYWORD ,RASING ERROR]  ##

                          ##DAY 36 ,37 ,38  OF LEARNING PYTHON TODAY TOPIC IS;-[EXECPTION ERROR HENDLING  FINALLY KEYWORD ,RASING ERROR] ###


###DAY 36   OF LEARNING PYTHON TODAY TOPIC IS;-[EXECPTION ERROR HENDLING ]
# Exception Handling in Python simple code 
    ### THIS IS THE 1ST CODE ###                
try:
    
    a=int(input("enter the number "))
    for i in range (11):
     
     print(f"the multipale of {int(a)} x {i}={int(a)*(i)}")
     ##this is basically print the table  of which number you want 


except:  # it work when we enter the wrong the value like [we provide the string input]
    print("you dont enter a number ")


   ### THIS IS THE 2ND CODE ###

### we can use so many expect case in the code the exmple are
try:

    a=int(input("enter the num. "))
    sachin=[2,4,5,6,7,4,3,2]
    print(sachin[a])
except IndexError :
   print("invalid index")

except ValueError  :
   print("pls put (or enter)the number ")

                                                    ### THIS IS ALL ABOUT THE EXCEPTION ERROR IN THE PYTHON ###
                                                                        ## DAY 36 DONE ###
                                                                        #TIMING=22:59##




                                                  ##DAY 37  OF LEARNING PYTHON TODAY TOPIC IS;- [ FINALLY KEYWORD ]
#SOME ABOUT THE FINALLY KEYWORD


     ##FINALLY KEYWORD IN PYTHON THE CODE HOW IT USE {The finally block will be executed no matter if the try block raises an error or not.}
try:
 a=int(input("enter the number "))
 
 for i in range (11):   
        print(f"the multipale of {int(a)} x {i}={int(a)*(i)}")
        ##this is basically print the table  of which number you want 

except:  # it work when we enter the wrong the value like [we provide the string input]
        print("you dont enter a number ")

finally:
    print("i am exicuted always in any conditon does not matter error come or not")

    #{most of the pepole think this is also can do with just by write print  }
    #the finally is mostlly used in the funtion where the print does not work  the finally works always 

    #example of code using the function  to batter understading hoe the finally works  
    #  
## this is how we can use finally 
def fun():
    try:
        l = [1, 2, 3, 4, 54, 5, 5,4,67,88,9,4,3,5,45]
        i = int(input("Enter an index : ")) 
        return 1
    
    except IndexError:
        print("Index out of range. Please enter a value between 0 and 6.")
        return 0

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return 0

    finally:
        print("I am executed always in any condition, does not matter if an error occurs or not.")

# Call the function
x = fun()
print(x)
                                                  #### THIS IS ALL ABOUT THE FINALLY IN THE PYTHON ###
                                                                 ### DAY 37 DONE ###
                                                                    ##TIMING=23:45##


                                        ###DAY 38   OF LEARNING PYTHON TODAY TOPIC IS;-[RAISNG ERROR HENDLING
 # WHAT IS RAISING A ERROR :-{Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program.
 #  It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack.}

 # RASING ERROR  in Python simple code 
num=int(input("enter the value b/w 5 to 20 : "))

print(f"the squre of the number {num**2}")

if (num<5 or num>20):
 raise ValueError ("the enter number should be between 5 to 20 ")


                                                #### THIS IS ALL ABOUT THE RASINIG ERROR IN THE PYTHON ###            
                                                                 ### DAY 38 DONE ###
                                                                    ##TIMING=00:04##
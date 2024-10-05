                                        ### DAY 29 in python today i learn about the recursion  and use it ###
                                          # write a simple code for batter understand abohut the recursion :-
# ####{the recursion is basically help to call call the function but by using the diffrent arrguments }####

# the code using recursion in the funtion on python
def power(n): #This was the simple code for finding the any power using the condtion if else 
    print(n**5)
if (power==0):
    print(0)
elif (power==1):
    print(1)
else:
    print(power)
power(2)
print(power)


#How factorial work if if want to find the factorial of 5 the it whould be find like this 
# 5*4*3*2*1 =120 is Answer

                          #[ TASK OF DAY 29 ]# ##USING THE RECURSION IN  THE FUNCTION##
## Here we call the function again by giving the diffrent argument as we can see
def factorial(n):   # FIRST FUNCTION {SIMPLE}
    if n==0 or n==1:
        return 1
    else :
        return n*factorial(n-1) #RECALL THE FUNCTION WITH ANOTHER ARGUMNENT
print(factorial(6))


#THE QUESTION FOR RECURSION:-write a program fibonacci sequence 
# f(0)=0
# f(1)=1
# f(2)=f(1)+f(0)
# f(n)=f(n-1)+f(n-2)

                                                               ###DAY 29 IN PYTHON DONE ###
                                                                      ##TIMING :11:47##             
                                    #day14#
                        #if  elif else conditon in python
#have some conditional oprater
#<,>,!=,==,,<=,>=

#if else using
a=int(input("enter your agr :"))
if a>18:
 print("you are able to drive")      
else :
 print("you cannot drive")        

mango=20
budget=200
if mango<=budget:
    print("yes you can buy it ")                 
else:
    print("yuo can not buy it")

#using elif condition {for many condition}
coder=int(input("enter you number"))
if coder<0:
  print("the number is nagttive")
elif coder==0:
 print("number is zero")
elif coder==999:
 print("lucy man you are ")
elif coder>0:
 print("the number is psitive")

#nesated if else is using in it 
c=int(input("enter your number"))
if c<0:
      print("number is nagtive")     
elif (c>0):
   if c>=10:
      print("the number lies between 1 to 10")     
   elif c>=20:
      print("the nmuber lies betwwen the 11 to 20")
   else:
      print("the number is grater than 20")

else:
 print("the number is postive")
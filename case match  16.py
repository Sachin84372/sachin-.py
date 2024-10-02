                                           #day 16#
                                 #match case case  in python #
             #the case match is a newly in the python3.10 update {it not int the in python 3.08#}
a=int(input("enter you numnber "))
match a:
    case 0:

        print(''' case zreo  is match  "hii''')
    case 1:
        print(''' case one is match "its me"''')

    case 2:
        print('''case two is match "day 16"''')
    

    #we can use the if ,elif,else on the case match for more optin 
    
    case _ if a==50:
        print("congratulaion value is 50")
    case _ if a==66:
        print("congratulaion value is 66")
    case _ if a==99:
        print("congratulaion value is 99")
    case _ :
        print("case dont match")
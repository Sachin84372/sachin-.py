                                                            ### THE DAY 27 IN PTTHON 3.6###
                                        #The using of the format in python which was an older step #
   # code using the format in the string method    
About =("Hii i am {} i blong from {} an i am leving in the {} and my hobby is  to {}")

name=("sachin kumar")
country=("india")
city=("punjab")
hobby=("play fotboll")
  ### it just use format if we write any wrong format it print un useful line
print(About.format(name,country,city,hobby))


   # code using the format in the string method    
About =("Hii i am {1} i blong from {2} an i am leving in the {0} and my hobby is  to {3}") #Here we write the index number

name=("sachin kumar")
country=("india")
city=("punjab")
hobby=("play fotboll")
  ### it just use format if we write any wrong format it print un useful line { we can correct it by just using index number}
print(About.format(city,name,country,hobby)) #we see the index from there

### now we use F.string which is new in the method in the python  #

   # code using the f string  in the string method    


name=("sachin kumar")   
country=("india")            ## we can write it just by {print f}
city=("punjab")
hobby=("play fotboll")
print(f"Hii i am {name} i blong from {country} an i am leving in the {city} and my hobby is  to {hobby}")

# some  help full trick using {[f string ]}
print(f"{23*34}")
print(type(f"{23*34}"))  #the output is in the sting

price =23.4365256334
print(f"{price:.2f}")  # the 2f is help to provide the {[2number in decimal]}


                                                    ###THE END OF THE DAY 27 IN PTTHON 3.6###
                                                            ### TIMING 12:03 AM ###


#trying the simple why for why we use this [understood]
about =("Hii i am {SACHIN} i blong from {HEHEH}")
print(about)

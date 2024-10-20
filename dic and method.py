                                                      #DAY 33 IN THE PYTHON TASK =LEARINING THE DICTIONARY #

#A dictionary is a built-in data type that allows you to store data in key-value pairs. Here are some key features of dictionaries in Python: 
# the basic code of the dic in the python:-
dic={
    "weeks":"in one week have a seven days",
    "mounths":"In one year having a 12 mounth ",
    "year":"a time period of 365 days"
}

print(dic)


#here we store the data of the sachin in dic we use all the basic or main methods in it
info={"name":"sachin kumar","class":"B-tech","age":18 ,"city":"utter pardesh"}

print(info)  # it just provide the simple output if the info 

print(info["name"])  # if we use the just dic define name than we just got an error for the batter  expirence and fix the bug in that time 

print(info.get("name")) # if we use the (.get) than it does not throw the error  some time it good but some of the time it not goood ..

print(info.keys())  #it  provide the key of the dic like id of the details

print(info.values())  #it provide the value of the dic like the details are being in the provided in the id                

print(info.items())

#now we are using the the for of f string inn the dic  on the info 2
info2={"name":"satishkumar","class":"BCA","age":24 ,"city":"bihar"}
for key in info2.keys():
    print(f"the value of the key {key} is {info2[key]}") # the output is come by using the f string it is noW easy to understanding what is the output


info2={"name":"satishkumar","class":"BCA","age":24 ,"city":"bihar"}
print(info.items())
for key,values in info2.items():
    print(f"the value of the {key} is {values}") # the output is come by using the f string it is noW easy to understanding what is the output WE USE ITEMS method in it 

                                                                          ### DAY 33 IS DONE ###
                                                                          ### TIMING= 12:30 ###
   
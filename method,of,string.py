                                      #day 13#
                                #string method in python

#for finding the length of the string 
a=("hii my name is sachin kumar")
namelen= len(a)
print("the length of name is ",namelen,) #first why
print( len(a)) #second why

#the string are immutable  {we can not change the string} 
#for upper case
a=("HIi My namE is SachIn Kumar")
print(a.upper())
#for lowr case
b=("HIi My namE is SachIn Kumar")
print(b.lower())


# use of the rstrip 
c=("heloo!!!!!!!")
print(c.rstrip("!"))


# use of the replace{_help to replace the string}}
d=("sumit kumar")
print(d.replace("sumit kumar", "sachin kumar"))


# use of the split{_help to split the string into the list}
e=("sumit,sachin,suraj,karan,satish,himanshu,ujjwal,neeraj")
print(e.split(" "))


# use of the capitalize{_help to capitalize the first letter of the string}
f=("hii my name is sacHiN Kumar")
print(f.capitalize())


# use of the center{_help to center the string}
g=("hii i am btech cse student")
print(g.center(60))
print(len(g))
print(len(g.center(60)))


# use of the count{_help to count the string}
h=("sachin ,sumit,sachin ,sachin ,sumit,sachin ,sachin ,sumit,sachin ,sachin ,sumit,sachin")
print(h.count("sachin"))


# use of the endswith{_help to check the string is end with the given value}
i=("how are you my friends")
print(i.endswith("friends"))
print(i.endswith("you",5,7))


# use of the find{_help to find the first occurence of the given value}
j=("hey my name is sachin kumar")
print(j.find("is"))
print(j.find("isname"))


# use of the index{_help to find the first occurence of the given value}
k=("hey my name is sachin kumar")
print(k.index("my"))
#print(k.index("myname"))


# use of the isalnum{_help to check the string is alpha numeric}
L=("hey my name is sachin 24 kumar") #it containts A-Z,a-z,0-9
print(L.isalnum())


# use of the isalpha{_help to check the string is alpha}
m=("hey my name is sachin kumar") #it only contains A-Z,a-z
print(m.isalpha())


#use of the islower{_help to check the string is lower}
n=("hey my name is sachin kumar") #it only contains lower case
print(n.islower())


# use of the isprintable{_help to check the string is printable}
o=("hey my name is sachin kumar/n") #it only contains printable character
print(o.isprintable())


# use of the isspace{_help to check the string is space}
p=("hey my name is sachin kumar") #it only contains space
p=('hello') #it only contains space
print(p.isspace())


# use of the istitle{_help to check the string is title}
q=("hey my name is sachin kumar") #it only contains title
print(q.istitle())


# use of the isupper{_help to check the string is upper}
r=("HEY MY NAME IS SACHIN KUMAR") #it only contains upper case
print(r.isupper())


# use of the startswith{_help to check the string is start with the given value}
s=("hey my name is sachin kumar") #is string start with given with
print(s.startswith("hey"))
print(p.isspace())


# use of the swapcase{_help to convert the upper case to lower case and lower case to upper case
t="hello my firends"
print(t.swapcase())
ts=("HII MY NAME S SACHIN KUMAR")
print(ts.swapcase())


# use of the title{_help to convert the first letter of the word to upper case}
u="hello my firends" #it change all the first world into  capital letter
print(u.title())


# use of the istitle{_help to check the string is title}
v=("hey my name is sachin kumar") #it only contains title
print(v.istitle())

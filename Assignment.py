# Write a python code that displays all popular dataypes to the user.
# Each datatype will be explained and an example will be attached

# Question 2
# Write a java code that will take a proof and then solve it by proof of induction

datatypes = ["strings", "integers", "boolean","float"]
print ("These are the basic datatypes in computing" , datatypes)
assign = input ( "Type in what datatype you would like to know about"
)
if assign == datatypes[0]:
    print("Strings are collective characters.... basically any data you put in quotes when programming"  )
    print(assign = input ( "Type in what datatype you would like to know about"
))
elif assign == datatypes[1]:
    print ("Integers are non-decimal numbers")
    print(assign = input ( "Type in what datatype you would like to know about"
))
elif assign == datatypes[2]:
    print ("Boolean values deal with situstions where you can only have two answers; like in the case of True and False")
    print(assign = input ( "Type in what datatype you would like to know about"
))
elif assign == datatypes [3]:
    print ("Floats are decimal numbers. As a matter of fact, integers can be found here as well since all integers are in the form x.0 where x belongs to a set of integers")
    print(assign = input ( "Type in what datatype you would like to know about"
))
else: 
    print("You are not choosing from th list choose an option from the list given")
    


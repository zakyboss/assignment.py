# Slice the string below to get as follows
# a= "The Dog Breed Is German Shepherd", only display "Breed Is German"
sent1="The Dog Breed Is German Shepherd"
#k=sent1[2:24]

print(sent1[4:23])
print(" ")
print(" ")

# b=sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sent2="Defeats for the Clinton forces, this was her moment of triumph"
print(sent2[15:30])
#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
sent3="The lazy dog; ran so fast; it hit the wall"
sent4=(sent3.split(";"))
print(len(sent4))
#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="Joh.n"
first_name1=first_name.replace("Joh.n",'John')

last_name="Do,e"
last_name1=last_name.replace("Do,e","Doe")
print(first_name1 + " "+last_name1)

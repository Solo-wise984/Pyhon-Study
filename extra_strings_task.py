#Creating first_name and last_name and concanating them to form full_name
first_name="Solomon"
last_name="Macharia"
full_name=first_name+" "+last_name
print(full_name)

#Character indexing
text="PYTHON"
print(text[0] )
print(text[5])

#Character indexing
phrase="learning Python is fun!"
print(phrase[9:15])

#Rversing a string



#Character Replacement
greetings="Hello World"
greetings2=greetings .replace('World','Python')
print(greetings2)

#Changing to uppercase
msg="Python Programming"
msg2=msg.upper()
print(msg2) 

#changing to lowercase
msg="Python Programming"
msg3=msg.lower() 
print(msg3)

##Count occurrence
sentence="This is a simple sentence"
sentence2=sentence.count("s")
print(sentence)

#Checking Substring presence
quote="The best way to predict the future is to create it"
quote2=quote.count('future')
print(quote2)
#using "in" in this 
print("future" in quote  )


#String length
description="Data Science"
description2=len(description)
print(description2)

#Removing Spaces
name="    John Doe   "
name2=name.strip()
print(name2)
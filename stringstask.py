#clean the word JOHn to "john"
name="JOHn"
print(name .capitalize)

#cleaning the word "John Doe"
fname="Joh.n"
lname="Do,e"
#Replacing ","with a space"
cleaned_fname= fname .replace('.','')
cleaned_lname=lname.replace(',','')
full_name=cleaned_fname+" "+cleaned_lname
print(full_name)

#initial sentence
sentence="The lazy dog; ran so fast; it hit the wall"
#split the sentence with;
parts=sentence.split(';w')
sentence1=(parts)
print(sentence1)

#Slice the sentence below from "The Dog Breed is German Sherpherd" to "Breed is German"
text="The Dog Breed is German Sherpherd"
print(text[8:24])

#manupulating "["E","W","C"]" to EWC
r=["E","W","C"]
r2=r.replace('[','').replace('"','').replace(',','').replace(']','')
print(r2)






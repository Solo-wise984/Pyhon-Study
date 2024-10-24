person={
    'name':"Kelvin",
    'age':25,
    'gender':'male',
    'location':{'kiambu',518},
    'address':{
        'street':'muthaiga',
        'city':'nairobi',
        'county':'kenya'
    }
    
}

print(type(person))
print(person['name'])
#age
print(person['age'])
#gender
print(person['gender'])
#location

#city


#Adding a key
person['ocupation']='Doctor'
print(person)

print(person.keys())



person.pop('name')

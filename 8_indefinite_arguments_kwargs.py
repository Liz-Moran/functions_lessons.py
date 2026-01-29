
# Indefinite Arguments (**kwargs) Practice #1
# # Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.
def number_attributes(**kwargs):
    return len(kwargs)
print(number_attributes())




# # Indefinite Arguments (**kwargs) Practice #2
# # Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.
# def list_attributes(**kwargs)
def list_attributes(**kwargs):
    return list(kwargs.values())
result1 = list_attributes(name="Alice", age=30, city="Chicago")
print(result1)  # Output: ['Alice', 30, 'Chicago']




# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:
def describe_person(person_name, **kwargs):
    print(person_name,  )
    for key, value in kwargs.items():
        print("  ", key, ":", value)
print(describe_person("Alice", eye_color="blue", hair_color="black"))

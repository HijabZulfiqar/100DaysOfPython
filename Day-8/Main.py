# Review Functions
def Greet():
    print("Hello")
    print("How are you?")
    print("What is your favorite color?")
Greet()
# funtion with inputs
# def Greet_with_name(name):
#     print(f"Hello {name}" )
# Greet_with_name("Hijab")
# functions with more than 1 input
def greet_with_inputs(name,age):
         print(f"Hello {name}")
         print(f"How are you?")
         print(f"What is your favorite color?")
         print(f"Your age is {age}")
         print("Or")
         print(f"Hello {name} you are {age} years old")
greet_with_inputs("Hijab",23)
# Keyords Arguements
greet_with_inputs(name="Hijab",age=23)
# Function with output
def my_function():
    return 2*3
output = my_function()
print(output)
def my_function2(a,b):
    return a+b
print(my_function2(2,3))
print(my_function2("Hijab","Zulfiqar"))
# DocString
def my_function3(a,b):
    """ add two  parameters """
    return a.title()+b.title()

print(my_function3("Hijab","ZULFiQAR"))
def my_function4(a,b):
    if a=="" or b=="":
        return


    format_a=a.title()
    format_b=b.title()
    return f"Result: {format_a} {format_b}"
print(my_function4(input("Enter first"),input("Enter second")))


import math

print('Welcome to PaintArea')
height = int(input('Enter your height : '))
weight = int(input('Enter your weight  :'))
coverage=5

def paint_area(height,weight,coverage):
    number_of_cans = math.ceil((height * weight) / coverage)
    print(number_of_cans)
paint_area(height,weight,coverage)
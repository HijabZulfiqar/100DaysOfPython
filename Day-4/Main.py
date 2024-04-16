
import  random
import  my_module
# Randomisation
random_num=random.randint(1,10)
print(random_num)
# Random Float numbers
random_float=random.random()
print(random_float*5)
# Modules in python

print(my_module.name,my_module.Age)
# Python List

states_of_America=["Washington","New York","Delaware","Florida","Pennsylvania","Denver","Rhode Island","South Dakota","Georgia","Hawaii","Utah","Illinois"]
print(states_of_America[0])
states_of_America.append("AngelaLand")
print(states_of_America)
states_of_America.reverse()

print(states_of_America)
# Nested List
fruits=["apple","banana","grape","orange"]
vegetables=["Potato","Tomato","Cabage","Spinach"]
nested_list=[fruits,vegetables]
print(nested_list)
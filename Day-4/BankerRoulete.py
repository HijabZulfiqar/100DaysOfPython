import random

name_String=input("Give me everybody's name? Separated by a comma!\n ")
name_List=name_String.split(",")
# print(name_List)
print(name_List)
random_name=random.randint(0,len(name_List)-1)
print(random_name)
print(name_List[random_name])

# Python Dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
# Adding to dictionar
programming_dictionary["Loop"] = "A action of doing something again and again."
print(programming_dictionary["Loop"])
print(programming_dictionary)
# Edit a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting Dictionary and Lists
travel_log={
    "France":{
        "city_visited":["Paris","Lille"],
        "total_visits":12
    },
    "Germany":{
        "city_visited":["Berlin","Hamburg"],
        "total_visits":0

    }
}





# Wipe out a dictionary

programming_dictionary = {}
print(programming_dictionary)


# Exercise 9.2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,times,city):
    new_country ={}
    new_country["country"] = country
    new_country["visits"] = times
    new_country["cities"] = city
    travel_log.append(new_country)






#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)




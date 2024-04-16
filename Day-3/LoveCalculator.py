print("Welcome to the Love Calculator!")
name1 = input("What is your name?")
name2 = input("What is their name?")
combined_name = name1 + name2
lowest = combined_name.lower()
t = lowest.count("t")
r = lowest.count("r")
u = lowest.count("u")
e1 = lowest.count("e")
true = t + r + u + e1
# now love
l = lowest.count("l")
o = lowest.count("o")
v = lowest.count("v")
e2 = lowest.count("e")
love = l + o + v + e2
total_score = int(str(true) + str(love))
# print(f"Your Love score is {total_score}")
if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score}  and you come together like coke and mentos")
elif (total_score >= 40) and (total_score <= 50):
    print(f"Your score is {total_score} and you are alright together")
else:
    print(f"Your score is {total_score} ")
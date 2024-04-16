sum_of_even_numbers = 0
for number in range(1,101):
    if number % 2 == 0:
        sum_of_even_numbers += number
print(sum_of_even_numbers)
#OR
sum_of_even_numbers2 = 0
for number in range(2,101,2):
    sum_of_even_numbers2 += number
print(sum_of_even_numbers2)

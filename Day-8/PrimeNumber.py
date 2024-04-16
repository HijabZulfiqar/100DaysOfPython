print("Welcome to the prime numbers checker")
number_p = int(input("Enter a number:"))


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
        else:
            print("Prime")


is_prime(number=number_p)

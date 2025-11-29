# Write a program to display prime numbers up to 100.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for number in range(101):
    if is_prime(number):
        print(number)

# Alternatively, using list comprehension to generate and print prime numbers up to 100
prime_numbers = [num for num in range(101) if is_prime(num)]
print("Prime numbers up to 100 are:", prime_numbers)

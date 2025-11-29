# Write a program using list comprehension to find sum of only even numbers.

def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

numbers = []
n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

result = sum_of_even_numbers(numbers)

print(f"Sum of even numbers: {result}")

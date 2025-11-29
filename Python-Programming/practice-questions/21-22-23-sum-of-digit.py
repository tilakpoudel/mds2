# Write a program to find sum and average of 10 numbers stored in a list.

def sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0

    return total_sum, average

# Find smallest and largest number among 10 numbers stored in a list.
def find_smallest_largest(numbers):
    if not numbers:
        return None, None

    smallest = min(numbers)
    largest = max(numbers)

    return smallest, largest

# count even numbers and odd numbers stored in a list.
def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count

    return even_count, odd_count

numbers = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total, avg = sum_and_average(numbers)
smallest, largest = find_smallest_largest(numbers)
even_count, odd_count = count_even_odd(numbers)

print("Sum of the numbers:", total)
print("Average of the numbers:", avg)
print("Smallest number:", smallest)
print("Largest number:", largest)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

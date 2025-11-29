# Write a program to display “MDS” 10 times.

# Using a for loop with variable name
for i in range(10):
    print("MDS")

# Using a for loop with underscore as the variable name
for _ in range(10):
    print("MDS")

# Using while loop
count = 0
while count < 10:
    print("MDS")
    count += 1

# Using a list comprehension (not recommended for just printing)
[print("MDS") for _ in range(10)]

# Using a function with recursion
def print_mds(n):
    if n > 0:
        print("MDS2")
        print_mds(n - 1)
print_mds(10)

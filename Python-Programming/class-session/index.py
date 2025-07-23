import sys
a = 8
print(sys.getsizeof(a))


# | Component                  | Purpose                               | Approx. Size |
# | -------------------------- | ------------------------------------- | ------------ |
# | Reference count            | Tracks how many variables refer to it | 8 bytes      |
# | Type pointer               | Says what type this object is (`int`) | 8 bytes      |
# | Actual integer value       | The number itself (e.g. `8`)          | 4–8 bytes    |
# | Padding, internal overhead | For alignment and structure           | varies       |
# 👉 Total = around 28 bytes for a simple integer on a 64-bit system.


# Bitwise operators

# Bitwise AND (&)
# Bitwise OR (|)
# Bitwise XOR (^)
# Bitwise NOT (~)
# Left Shift (<<)
# Right Shift (>>)

a = 5
b = 4

print("a = {}, b = {}".format(a, b))
print("a & b = {}".format(a & b))
print("a | b = {}".format(a | b))
print("a ^ b = {}".format(a ^ b))
print("~a = {}".format(~a))
print("a << 2 = {}".format(a << 2))
print("a >> 2 = {}".format(a >> 2))

a = b = c = 10

print(2**5**3)
print((2**5) ** 3)

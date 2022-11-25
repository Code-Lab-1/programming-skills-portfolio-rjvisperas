a = ['Dubai', 'Japan', 'Morocco', 'North Korea', 'USA']

print("Original order:")
print(a)

print("\nAlphabetical:")
print(sorted(a))

print("\nOriginal order:")
print(a)

print("\nReverse alphabetical:")
print(sorted(a, reverse=True))

print("\nOriginal order:")
print(a)

print("\nReversed:")
a.reverse()
print(a)

print("\nOriginal order:")
a.reverse()
print(a)

print("\nAlphabetical")
a.sort()
print(a)

print("\nReverse alphabetical")
a.sort(reverse=True)
print(a)
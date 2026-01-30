# Problem 10: Remove duplicates from a list
# Find and fix the error

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
seen = set()
for num in numbers:
    if num not in unique:
        unique.append(num)
        seen.add(num)
print(f"Unique numbers: {unique}")

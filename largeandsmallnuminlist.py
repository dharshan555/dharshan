numbers = [28, 56, 42, 10, 95, 73]
smallest = numbers[0]
largest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
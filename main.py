# This is a simple Python program

# A variable stores a value
name = "Ola"

# A list stores multiple values
numbers = []

# A function groups reusable logic
def calculate_average(num_list):
    total = sum(num_list)
    count = len(num_list)
    average = total / count
    return average

# A loop repeats actions
for number in numbers:
    print("Number:", number)

avg = calculate_average(numbers)

print("Average:", avg)
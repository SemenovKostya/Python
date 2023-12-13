a = int(input("Digital from 1 to 20 : "))
b = int(input("Digital from 1 to 10 : "))
if a > 1 and a < 20:
    if b > 1 and b < 10:
        sum1 = a + b;
        min1 = a - b;
        mul1 = a * b;
        div1 = a // b;
        print(sum1,min1,mul1,div1)
    else:
        print("Nothing")
else:
    print("Nothing")


hour = int(input('Count of hours: ')) #17
mins = int(input('Count of mins: ')) # 35
dura = int(input('Count of duration (minutes): ')) # 40

mins = mins + dura
mins = mins % 60

hour = round((hour * 60 + dura)/ 60)
if hour>24:
    hour = hour - 24
else:
    hour = hour
print(hour,mins,dura)

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)




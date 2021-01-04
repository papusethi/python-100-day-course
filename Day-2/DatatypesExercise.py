'''
Exercise Instruction

write a program that adds the digits in a 2 digit number 
e.g if the input was 35, then the output should be 3 + 5 = 8
'''

# ask for input a number
two_digit_number = input("Type a two digit number: ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

result = int(first_digit) + int(second_digit)
print(result)
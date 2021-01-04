'''
wap that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m).

WARN: you should round the result to the nearest whole number.
'''

height = input('enter you height in m: ')
weight = input('enter your weight in kg: ')

actual_bmi = float(weight) / (float(height) ** 2)

bmi_as_int = int(actual_bmi)
print('Your BMI value is ' + str(bmi_as_int))

# end

'''
Create aprogram using maths and f-strings that tells us how many days, weeks, mnths we have left if we live untill 90 years.

It will take your current afe as the input and output a message with our time left in this format.

'You have x days, y weeks, and z months left.'

where x, y and z are replaced with the actual calculated numbers.
'''

age = input("what is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
# type error and type check

print(len("Hello"))
# print(len(1234)) # type error

num_of_char = len( input("what is your name? "))

print("type of variable num_of_char ", type(num_of_char))

# type conversion / type casting
new_num_of_char = str(num_of_char)

print("type of variable new_num_of_char ", type(new_num_of_char))
print("Your name has " + new_num_of_char + " characters.")

# conversion 
a = 123456
print( type( str(a) ) )

b = "123.345"
print( type( float(b) ) )

print( int("320") + float("320.123") ) # 640.123

print( str(100) + str(723) )    # 100723

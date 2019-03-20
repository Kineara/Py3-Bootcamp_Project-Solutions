# Reverse a String - Enter a string and the program will reverse it and print it out.

print("String Reverser")

while True:
	user_string = input("Enter the string you would like to reverse:")

	print(user_string[::-1])

	repeat = input("Would you like to reverse another string? y/n").lower()

	if repeat != 'y':
		break

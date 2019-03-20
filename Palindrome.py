# Check if Palindrome (word reads same backwards as forwards)

print("Palindrome Checker")

while True:
	user_string = input("Please enter a word to check:")
	if ' ' in user_string:
		print("Error! Please enter only a single word.")
		continue
	else:
		if user_string == user_string[::-1]:
			print(f"{user_string} is a palindrome!")
		else:
			print(f"{user_string} is not a palindrome!")

	repeat = input("Would you like to check another word? y/n").lower()

	if repeat == 'n':
		break

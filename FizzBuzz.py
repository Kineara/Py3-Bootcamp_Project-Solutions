# Fizz Buzz - Write a program that prints the numbers from 1 to 100.
# For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz".
# For numbers which are multiples of both three and five print “FizzBuzz”.

print("FizzBuzz")

for i in range(1,101):
	if i%5==0:
		if i%3==0:
			print("FizzBuzz")
		else:
			print("Buzz")
	elif i%3==0:
		print("Fizz")
	else:
		print(i)
		
# create a function called is_prime with an argument, x
def is_prime(x):
	# check if it is prime only for numbers larger than 2
	if x < 2:
		return False
	# All numbers are prime until proved the contrary
	prime_flag = True
	# loop for every integer i between 2 and x
	for i in range(2, x):
    	# If x is exactly divisible by i
		if x % i == 0:
			# x is not prime, so we set prime_flag to False
			prime_flag = False
			# Exit the loop, we already found it is not prime
			break
	# Return whichever state the number it is
	# If we did not find any divisor it should still be True
	return prime_flag
# check if 24 is prime and print the result
print is_prime(24)

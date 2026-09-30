def powerСheck():
	"""Contains assert statements to verify the correctness of the power function."""
	assert power(2,3) == 8, "Must be 2^3 = 8"
	assert power(5,1) == 5, "Any number in power by 1 return self"
	assert power(6,0) == 1, "Any number in power by zero return 1"
	assert power(-2,3) == -8, "Not work with  negative number"

	print("All tests passed successfully! You can work with program")

def power(number, n):
	""" Function for calculate the nth power  of  a number 
	Arguments:
		number (int)  - the base number to power
		n (int) - power (must be non-negative number)
	"""
	assert not (number == 0 and n ==0), "Impossible to power 0 by 0"
	assert n >= 0, "Incorrect input power less than 0"

	res = 1

	if n == 0:
		return 1
	
	for i in range(0,n):
		res *= number
	return res 

powerСheck()

num = int(input("Enter number: "))
n = int(input("Enter power: "))

print(f"{num}^{n} = {power(num, n)}")	
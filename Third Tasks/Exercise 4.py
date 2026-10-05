def sumOfDivision(num):
	""" Calculate the sum of all divisors of a number

	Arguments:
	num (int)  - number to check
	"""
	if num < 2:
		return 0

	totalSum = 1
	for i in range(2, (num // 2) + 1):
		if num % i == 0:
			totalSum+= i
	return totalSum
	
def perfectNumber(max):
	""" Finds and displays all perfect numbers from 2 to given max number
	
	Arguments:
	max (int)  - max limit to check number
	"""
	assert max >=0, "Max value is less than zero"
	print("\nPerfect numbers: ", end = " ")
	for i in range(2, max + 1):
		 if sumOfDivision(i) == i:
		 	print(f" {i} ", end = "")
		 	
def friendNumbers(max):
	""" Finds and displays all friendly numbers up to max
    
    Arguments:
    max (int)  - max limit to check number
    """
	assert max >=0, "Max value is less than zero"

	for n in range(2, max + 1):
		m = sumOfDivision(n)

		if n < m <= max and sumOfDivision(m) == n:
			print(f"{n} and {m} are friend numbers")

maxLimit = int(input("Enter the limit: "))
friendNumbers(maxLimit)				
perfectNumber(maxLimit)	
num = int(input("Hello, please enter a positive integer and I will say if it is a prime number or not: "))
isPrime = False
if num >1:
	isPrime = True
	for i in range(2, int(num/2) +1):
		if(num%i ==0):
			isPrime = False
			break
if(isPrime):
	print("It is prime")
else:
	print("It is not prime")

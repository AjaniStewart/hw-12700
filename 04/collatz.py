def collatz():
	n = int(input("Enter number: "))
	print(n)
	while not(n == 1):
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3 * n + 1
		print(n)
collatz()
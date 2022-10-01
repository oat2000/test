def FizzBuzz(num):
	if num % 3 == 0 and num % 9 != 0 and num % 5 != 0 and num % 25 != 0:
		return('Fizz')
	elif num % 5 == 0 and num % 25 != 0 and num % 3 != 0 and num % 9 != 0:
		return('Buzz')
	elif num % 3 == 0 and num % 5 == 0 and num % 25 != 0 and num % 9 != 0:					
		return('FizzBuzz')
	elif num % 9 == 0 and num % 25 != 0:
		return('FizzFizz') 
	elif num % 25 == 0 and num % 9 != 0:
		return('BuzzBuzz')
	elif num % 9 == 0 and num % 25 == 0:
		return('FizzFizzBuzzBuzz')
	elif num > 10000:
		return('NoFizzBuzz')	
	else:
		return('NoFizzBuzz')
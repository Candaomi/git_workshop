# print 'Hello World!'
# name = raw_input("What's your name? ")
# print "Your name is " + name


# x= raw_input("What is your number? ")
# if x < 0:
# 	print "x is negative"
# elif x > 0:
# 	print "x is positive"
# else:
# 	print "x is 0"


# print "It's your birthday!"
# answer = raw_input("How old are you? ")
# age = int(answer)
# if age < 21:
# 	print "You may not have a beer, but here's some juice!"
# else:
# 	beers = raw_input("How many beers do you want?")
# 	beers = int(beers)
# 	if beers > 3:
# 		print "Oops, you're drunk!"
# 	elif beers > 1:
# 		print "You got a little tipsy"
# 	else:
# 		print "Looks like you're the designated driver"
# print "Happy birthday!"



# x=5
# while x > 0:
# 	print x
# 	x= x-1

# shipping_cost = 2.5
# prices = [3, 4, 5.25]
# costs = []

# for z in prices:
# 	costs.append(z + shipping_cost)

# print costs

# print range(5)
	
# my_list = [1, 'hello', 12.33, 'data', [1,2]]
# for x in my_list:
# 	print type(x)


# magicno = 26
# guess = raw_input("Guess a number between 1 and 100. ")
# noomber = int(guess)
# print noomber
# if noomber == magicno:
# 	print ("Congratulations! Would you like to play again?")
# elif noomber >=10 and noomber<20:
# 	print ("You are warm!")
# elif noomber>=5 and noomber<10:
# 	print ("You are hot!")
# elif noomber >=0 and noomber<5:
# 	print ("You are scalding!")
# elif noomber >=20 and noomber<50:
# 	print ("You are cool!")
# else:
# 	print ("You are cold!")

# my_list = [1, 'hello', 12.33, 'data', [1,2]]
# for item in my_list:
# 	print type(item)


# Functions

# a = 3
# print type(a)



#CREATING A FUNCTION

# def print_plus_5(x):
# 	print x + 5
# print_plus_5(2)
# print_plus_5(9)

# def hello_world():
# 	return "Hello World!"
# print "Kim" + hello_world() 

# answer = raw_input("What is your age? " ) 
# age = int(answer)
# def isOfDrinkingAge(age):
# 	print age
# 	if age < 21:
# 		print "Go home!"
# 	else:
# 		print "Come on in!"
# isOfDrinkingAge(age)

answer = raw_input("What is today? ")
dayOfWeek = str(answer) 

seasonanswer = raw_input("What is the season? ")
season = str(seasonanswer)

tempanswer = raw_input("What is the temperature? ")
currentTemperature = int(tempanswer)

def willKermitPlantFlowers(dayOfWeek, season, currentTemperature):
	if dayOfWeek == "Saturday" and seasonanswer == "Spring" and currentTemperature > 65:
	
		print "Kermit plants flowers today"
	else:
		print "Kermit does not plant flowers today"
willKermitPlantFlowers(dayOfWeek, season, currentTemperature)


# tempo = raw_input ("What is the temperature in your basement? ")
# humy = raw_input("What is the humidity in your basement? ")

# temperature = int(tempo)
# humidity = int(humy)

# def basementIsOk(temperature, humidity):
# 	if temperature < 50 or humidity > 70:
# 		print "Zach, you have a problem! "
# 	else:
# 		print "Zach, relax!"

# basementIsOk(temperature, humidity)


# {"talk": "to speak out loud"}
# KeyboardInterrupt
# people_ages = {"Amy":26, "Tim":15, "Sally": 45}
# my_list[0]
# people_ages["Amy"]

# menu = {'pizza': 9, 'burger': 12, 'dessert': 5}
# print menu['burger']

# my_list = [1, 'hello', 'goodbye', 2, 14]
# if 3 in my_list:
# 	print "You are number 1"
# else:
# 	print "Boo"


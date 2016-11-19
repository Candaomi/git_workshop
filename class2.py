




# def basementIsOk():
# 	tempo = raw_input ("What is the temperature in your basement? ")
# 	temperature = int(tempo)
# 	if temperature < 50 :
# 		print "Zach, you have a problem with your temperature! "
# 	else: 
# 		humy = raw_input("The temperature is fine, what's the humidity? ")
# 		humidity = int(humy)
# 		if humidity > 70:
# 			print "Zach, you have a problem with your humidity! "
# 		else:
# 			print "Zach, relax!"

# basementIsOk()





 



def willKermitPlantFlowers():
	answer = raw_input("What is today? ")
	dayOfWeek = str(answer)
	if dayOfWeek == "Saturday": 
		print "Let's see what the season is!"
	
		seasonanswer = raw_input("What is the season? ")
		season = str(seasonanswer)
		if seasonanswer == "Spring": 
			print "Nice! What's the temperature? "
		 
		 	tempanswer = raw_input("What is the temperature? ")
		 	currentTemperature = int(tempanswer)	
		 	if currentTemperature > 65:
		 		print "Kermit plants flowers today"
		 	else:
		 		print "Kermit does not plant flowers today"
		else: 
		 	print "Kermit does not plant flowers today"
	else:
		 print "Kermit does not plant flowers today"
			
willKermitPlantFlowers()


# How to write any statement
# 1. Ask question
# 2. Define function
# 3. List out parameter check
# 4. Call function
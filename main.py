''' Random Password Generator will generate password for you having the following cahracteristics
              1. At least 8 characters
			  2. No words, instead randomly chosen characters
			  3. Characters - numbers, 
				 uppercase/lowercase letters, punctuation's
This will protect password against all kinds of attacks '''


import random, string, sys,time

# List of characters, alphabets, numbers to choose from

data_set = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

# generates a very strong random password due to randomness 

def generate_random_password(n):
	if n < 8:
		return("\nNo password generated :( , password should be at least 8 characters long!")
	
	# Chooses a random character from data_set
	# after password of given length is created
	# returns it to user
	password = ""
	for x in range(n):
		password += random.choice(data_set)
	
	return password 

# Test
print("\nWelcome to RANDOM PASSWORD GENERATOR\n\n")
time.sleep(1)
while True:
	usr = input("Desired length of your password (or press 'e' to exit) :-  ").lower()
	if usr == "e":
		sys.exit()
	
	print("Generated password: " + generate_random_password(int(usr)) + "\n")
	time.sleep(1)
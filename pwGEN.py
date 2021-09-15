import string, random

exocombo = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def exoticfuckedme():
	pwlen = int(input('> Password length: '))

	random.shuffle(exocombo)

	pw = []
	for i in range(pwlen):
		pw.append(random.choice(exocombo))

	random.shuffle(pw)
	print("".join(pw))

exoticfuckedme()
input("\nPress any key to exit...")

#made by exotic cuz ye idk i felt like it

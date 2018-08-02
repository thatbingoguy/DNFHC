# THIS IS NOT AN ACTUAL INJECTOR.
# THIS WILL NOT GIVE YOU AN ADVANTAGE IN ANY COMBAT.
import os
from random import *
from time import sleep
def dprint(message):
	print('\r',message,end='')
print("  _____    _   _   ______   _    _    _____ ")
print(" |  __ \  | \ | | |  ____| | |  | |  / ____|")
print(" | |  | | |  \| | | |__    | |__| | | |     ")
print(" | |  | | | . ` | |  __|   |  __  | | |     ")
print(" | |__| | | |\  | | |      | |  | | | |____ ")
print(" |_____/  |_| \_| |_|      |_|  |_|  \_____|")
sleep(0.3)
print()
print()
print("Attempting to connect to servers...")
sleep(randint(0,1))
print("Connection succeeded.")
print("Downloading new client files...")
print("Download progress: 0")
sleep(1)
print("Download progress: ", randint(10,25))
sleep(1)
print("Download progress: ", randint(50,80))
sleep(1)
print("Download progress: 100")
print("Download Complete.")
#print()
#dprint("Downloading, Progress:   0% [          ]")
#sleep(0.2)
#dprint("Downloading, Progress:  10% [=         ]")
#sleep(0.2)
#dprint("Downloading, Progress:  20% [==        ]")
#sleep(0.2)
#dprint("Downloading, Progress:  30% [===       ]")
#sleep(0.2)
#dprint("Downloading, Progress:  40% [====      ]")
#sleep(0.2)
#dprint("Downloading, Progress:  50% [=====     ]")
#sleep(0.2)
#dprint("Downloading, Progress:  60% [======    ]")
#sleep(0.2)
#dprint("Downloading, Progress:  70% [=======   ]")
#sleep(0.2)
#dprint("Downloading, Progress:  80% [========  ]")
#sleep(0.2)
#dprint("Downloading, Progress:  90% [========= ]")
#sleep(0.2)
#dprint("Downloading, Progress: 100% [==========]")
#sleep(0.2)
#print()
#print("Download complete.")
# failed progress bar ^
sleep(1)
print("Attemping to find javaw.exe...")
def getTasks(name):
	r = os.popen('tasklist').read().strip().split('\n')
	for i in range(len(r)):
		s = r[i]
		if name in r[i]:
			return r[i]
	return []

if __name__ == '__main__':

	imgName = 'javaw.exe'

	notResponding = 'Not Responding'

	r = getTasks(imgName)

	if not r:
		print('Minecraft not detected - Please open Minecraft and try again.') 
		sleep(5)
		print("  at line 37")
		print("    if __name__ == '__main': ")
		print("  at line 130")
		print("    injectCheat(\"javaw.exe -F -T\")")
		exit()

	elif 'Not Responding' in r:
		print('Minecraft detected. Attemping to inject...')
		sleep(randint(1,3))
		print('Could not inject. Is the window responding?')
		sleep(5)
		exit()

	else:
		pass
print('Minecraft detected, attemping to inject...')
sleep(randint(1,3))
injectSuccessChance = randint(0,99)
if injectSuccessChance < 1:
	print("Injection failed!")
	sleep(randint(1,2))
	exit()
else:
	pass
print("Injection successful.")
sleep(1)
def clearscreen():
	os.system("cls")
	print("  _____    _   _   ______   _    _    _____ ")
	print(" |  __ \  | \ | | |  ____| | |  | |  / ____|")
	print(" | |  | | |  \| | | |__    | |__| | | |     ")
	print(" | |  | | | . ` | |  __|   |  __  | | |     ")
	print(" | |__| | | |\  | | |      | |  | | | |____ ")
	print(" |_____/  |_| \_| |_|      |_|  |_|  \_____|")
	print()
	print()
	print("DNFHC Injection Client. Type \'help\' for help.")
clearscreen()
# this is where it gets messy, copypasted from required.py
reachcmd = "reach"
autoclckcmd = "autoclick"
kbcmd = "kb"
helpcmd = "help"
listcmd = "listset"
sdcmd = "sd"
mpcmd = "misplace"
clscmd = "clearscreen"
reachvar = 0
acvar = 0
kbvar = 100
antikb = False
misplace = False
while True:
	dcmd = input("$>> ")
	# if i want to make dcmd back into one command instead of adding another variable with it,
	# i should add .split(' ') to the end of it. than at the if part i should replace "dcmd" with "dcmd[0]" and use "dcmd[1]" for the second part.
	if dcmd == reachcmd:
		reachvar = int(input("Reach amount (0-2): "))
		if reachvar == 0:
			print("Reach module disabled.")
		elif reachvar < 0:
			print("Invalid reach amount. Range from 0-2.")
		elif reachvar > 2:
			print("Invalid reach amount. Range from 0-2.")
			reachvar = 0
		else:
			print("Reach module set to add ", reachvar, " block reach to the default Minecraft range.")

	elif dcmd == autoclckcmd:
		acvar = int(input("Randomize CPS around which number? (0-20) "))
		if acvar == 0:
			print("Autoclick module disabled.")
		elif acvar < 0:
			print("Invalid CPS amount. Range from 0-20.")
			acvar = 0
		elif acvar > 20:
			print("Invalid CPS amount. Range from 0-20.")
			acvar = 0
		else:
			print("Autoclicker module set to randomize around ", acvar, " CPS.")
	elif dcmd == kbcmd:
		kbvar = int(input("Set velocity percent (0-100): "))
		if kbvar == 0:
			print("AntiKnockback enabled.")
		elif kbvar < 0:
			print("Invalid velocity amount. Range from 0-100.")
			kbvar = 100
			antikb = True
		elif kbvar == 100:
			print("Velocity module disabled.")
			if antikb == True:
				print("AntiKnockback module disabled.")
				antikb = False
			else:
				pass
		elif kbvar > 100:
			print("Invalid velocity amount. Range from 0-100.")
			kbvar = 100
		else:
			print("Velocity persent set to ", kbvar, " percent.")
			if antikb == True:
				print("AntiKnockback module disabled.")
				antikb = False
			else:
				pass
# program no longer crashes from below code
	elif dcmd == listcmd:
		if reachvar < 1:
			print("Reach module is disabled.")
		else:
			print("Reach module set to add", reachvar, "blocks to the default Minecraft reach. (Default reach value is 3 in Minecraft)")
		print() # Printing blank line to actually make the code work, and to not confuse people.
		if acvar < 1:
			print("Autoclicker module is disabled.")
		else:
			print("Autoclicker module is set to randomize around", acvar, "CPS.")
		print() # another blank line lmao
		if kbvar == 100:
			print("Velocity module is disabled.")
		elif kbvar == 0:
			if antikb == True:
				print("AntiKnockback enabled.")
			else:
				pass
		else:
			print("Velocity module set to", kbvar, "% velocity.")
	elif dcmd == helpcmd:
		print("reach - Sets the amount of reach added to Minecraft. 0 would set the client side reach to 3, while 2 would set to 5.")
		print()
		print("autoclick - Randomizes around set CPS. Undetectable by server-side anticheats, utilizing white noise to determine when to click. Range from 0-20, 0 will disable, while 20 will hover around 20, but not go over due to the tick system.")
		print()
		print("kb - Sets percent of velocity. 0 will enable AntiKnockback, while anything from 1-99 will set the amount of velocity knockback will deal. 100 disables this module.")
		print()
		print("listset - Shows you your current settings in the client.")
		print()
		print("sd - Self destruct; Uninjects from the Minecraft client and closes the injector for you to delete it in a hurry. (Screenshare friendly)")
		print()
		print("clearscreen - Clears screen.")
		print()
		print("Don't do something like \"kb 42\", just type in \"kb\", and wait for it to ask you for a number.")
	elif dcmd == sdcmd:
		print("Unhooking from javaw.exe")
		sleep(0.1)
		print("Deleting temporary log files...")
		sleep(0.2)
		print("Goodbye!")
		sleep(0.1)
		exit()
	elif dcmd == mpcmd:
		if misplace == False:
			print("Misplace enabled.")
			misplace = True
		else:
			print("Misplace disabled.")
			misplace = False
	elif dcmd == clscmd:
		clearscreen()
	else:
		print("Unknown command. Type \'help\' for help.")
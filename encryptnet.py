"""
Sir Syarif's codes.
Written at python 3.6 :)
"""

import os
import time
import webbrowser

os.system('cls')
os.system('color a')
time.sleep(3)
print('\n')
print("                ====================================")
print("                ======= S`I`R `` S`Y`A`R`I`F =======")
print("                ====================================")
print()
time.sleep(5)
print(" THIS IS AN ENCRYPTED NETWORK. ONLY ANONYMOUS THAT ALLOWED TO RUN IT.")
time.sleep(3)
print('\n')
os.system('pause')
os.system('cls')
os.system('color e')
def sir():
	print('\n')
	print("                ====================================")
	print("                ======= S`I`R `` S`Y`A`R`I`F =======")
	print("                ====================================")
sir()
print()
time.sleep(1.2)
print(" What are you going to do..??")
def  sirsyarif():
	time.sleep(1)
	print()
	print(" 1. Go To DuckDuckGo Search Engine")
	time.sleep(1)
	print(" 2. Go To Youtube")
	time.sleep(1)
	print(" 3. Go To Dropbox")
	time.sleep(1)
	print(" 4. Go To Yahoo")
	time.sleep(1)
	print(" 5. Go To Facebook")
	time.sleep(1.5)
	print()
	choice = input(" ==>> Pick-up a choice (1/2/3/4/5): ")
	if choice == "1":
		webbrowser.open("www.duckduckgo.com")
	elif choice == "2":
		webbrowser.open("www.youtube.com")
	elif choice == "3":
		webbrowser.open("www.dropbox.com")
	elif choice == "4":
		webbrowser.open("www.yahoo.com")
	elif choice == "5":
		webbrowser.open("www.facebook.com")
	else:
		print()
	back_again = input(" Only Accept 1-5. Press 0 to try again : ")
	if back_again == "0":
		os.system('cls')
		os.system('color cf')
		sir()
		print()
		time.sleep(1.5)
		print(" Select one of these options below!")
		sirsyarif()
	else:
		print(" Press y to back to the options")
sirsyarif()
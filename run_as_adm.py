import os
notAdministrator = True
try  :
	if os.getuid()!= 0:
		print("Please run as Admnistrator")
except:
	pass
print("Hello You")
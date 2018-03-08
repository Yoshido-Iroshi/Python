from socket import *
from datetime import datetime
import sys, time, os

os.system("cls")
host = ''
max_port = 100
min_port = 20

def scan_host(host, port, r_code = 1):
  try:
    s = socket(AF_INET, SOCK_STREAM)
    code = s.connect_ex((host, port))
    if code == 0:
      r_code = code
    s.close()
  except Exception:
    pass
  return r_code
  
try:
  host = input("\nHello, Sir. Please place the hostname : ")
except KeyboardInterrupt:
  print("'Ctrl+C' detected")
  print("Process is stopped\n")
  sys.exit(1)
  
hostip = gethostbyname(host)
print()
print("[*] Host : %s" % (host))
print("[*] IP   : %s \n" % (hostip))
print("[*] Scanning started at %s" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
  try:
    response = scan_host(host, port)

    if response == 0:
      print("[*] Port %d : open" % (port))
  except Exception:
    pass
  
stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("[*] Scanning finished at %s" % (time.strftime("%H:%M:%S")))
print("[*] Scanning duration : %s" % (total_time_duration))
print("\n  Powered by Sir Syarif")

#Getting Firewall Status
a = input("\n//Do you want to know the host firewall status..?? (y/n) : ")
if a == "y":
  print(os.system("netsh advfirewall show currentprofile"))
elif a == "n":
  pass
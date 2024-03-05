import os
from random import randint
import time

def alea():
    balle=int(input("Insère ton numéro de 1 à 6:"))
    if randint(1,1)==balle:
        print("Tu est foutu :()")
        time.sleep(2)
        print("ARRET SYSTEM!!!!")
        #os.system("shutdown 0")
    else:
        print("Ta eu de la chance")
        
        
        
def start(n):
    for k in range(n):
        alea()

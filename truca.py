import os
from random import randint

def alea(balle):
    if randint(1,6)==balle:
        os.system("shutdown 0")
    else:
        print("Ta eu de la chance")
        

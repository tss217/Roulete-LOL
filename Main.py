#ts217

import subprocess
import random
import os
import shutil


def roulette():
    rouletteNumber = random.randint(0,9)
    luckyNumber = random.randint(0,9)

    if rouletteNumber == luckyNumber:
        return True
    

    
#funcao para remover o legue of legends do computador   
def lucky():
    path = r"C:\Riot Games\League of Legends\uninstall.exe"

    if os.path.exists(path): 
        try:
            subprocess.run([path, "--uninstall"], check=True)
            print("ok")
        except FileNotFoundError:
            print("File not Found, sorry")
        except Exception as e:
            print(f"erro:{e}")
        finally:
            shutil.rmtree(r"C:\Riot Games\League of Legends")

def Main():

    print("""
                     _      _   _                            
                    | |    | | | |                           
     _ __ ___  _   _| | ___| |_| |_ ___   _ __ _   _ ___ ___ 
    | '__/ _ \| | | | |/ _ \ __| __/ _ \ | '__| | | / __/ __|
    | | | (_) | |_| | |  __/ |_| ||  __/ | |  | |_| \__ \__ \
    |_|  \___/ \__,_|_|\___|\__|\__\___| |_|   \__,_|___/___/
                                                            
                    Legue of Legends                                  
    """)

    print("""
                    Game of roulette russ with LOL
                            good lucky
    """)


    if roulette == True:
        lucky()

        print("You are lucky guy. allowed to unistall legue of legends")

    print("sorry body, notr this time")

Main()
""" Bataille entre 2 bots
Code écrit entièrement par DRU®"""

from colorama import Fore, Back, Style
import time
import random

class Battle:
    def __init__(self, life1, life2, combo1, combo2):
        self.combo1 = combo1
        self.combo2 = combo2
        self.life1 = life1
        time.sleep(random.uniform(1, 2))
        print(20*"\n"+'\033[1m'+"|"+Fore.LIGHTGREEN_EX+self.life1*"O"+Fore.WHITE+'\033[1m'+"|"+"\n")
        self.life2 = life2
        print('\033[1m'+"|"+Fore.LIGHTGREEN_EX+self.life2*"O"+Fore.WHITE+'\033[1m'+"|"+"\n")
        if self.life1 <= 0 or self.life2 <= 0:
            self.__str__()
        else:
            self.random = random.randint(1, 2)
            if self.random == 1:
                self.bot1()
            self.bot2()
        ou = str(input(30*"\n"+"Voulez-vous recommencer un combat ? OUI/NON \n -->  "))
        if ou.lower() == "oui":
            Battle(100, 100, 0, 0)
        elif ou.lower() == "non":
            exit()
        else:
            print("Coisissez oui ou non !")
            exit()

    def bot1(self):
        self.combo2 = 0
        if random.randint(1, 100)%2 == 0:
            self.combo1+=1
            self.attack()
            if self.combo1 == 3:
                self.life2 -= 3*self.damage
                print("Le BOT 1 a fait une combo attaque de "+str(3*self.damage)+" dégâts !\n")
                self.combo1 = 0
            else:    
                self.life2 -= self.damage
                print("Le BOT 1 a attaqué le BOT 2 et lui a mis "+ str(self.damage) + " dégâts !\n")
        else:
            #self.combo1 = 0
            print("Le BOT 1 a bloqué l'attaque du BOT 2 !\n")
            if random.randint(1, 3) == 2:
                self.combo1+=1
                self.attack()
                self.life2-=self.damage
                time.sleep(random.randint(1, 2))
                print("Le BOT 1 a contre-attaqué le BOT 2 et lui a mis "+ str(self.damage) + " dégâts !\n")
        return Battle(self.life1, self.life2, self.combo1, self.combo2)
    
    def bot2(self):
        self.combo1 = 0
        if random.randint(1, 100)%2 == 0:
            self.combo2+=1
            self.attack()
            if self.combo2 == 3:
                self.life1 -= 3*self.damage
                print("Le BOT 2 a fait une combo attaque de "+str(3*self.damage)+" dégâts !\n")
                self.combo2 = 0
            else:    
                self.life1 -= self.damage
                print("Le BOT 2 a attaqué le BOT 1 et lui a mis "+ str(self.damage) + " dégâts !\n")
        else:
            #self.combo2 = 0
            print("Le BOT 2 a bloqué l'attaque du BOT 1 !\n")
            if random.randint(1, 3) == 2:
                self.combo2+=1
                self.attack()
                self.life1-=self.damage
                time.sleep(random.randint(1, 2))
                print("Le BOT 2 a contre-attaqué le BOT 1 et lui a mis "+ str(self.damage) + " dégâts !\n")
        return Battle(self.life1, self.life2, self.combo1, self.combo2)

    def attack(self):
        self.damage = random.randint(8, 12)
    
    def __str__(self):
        if self.life1 > self.life2:
            print(Fore.LIGHTRED_EX+'\033[1m'+"Le BOT 1 a gagné !"+Fore.WHITE)
        else:
            print(Fore.LIGHTRED_EX+'\033[1m'+"Le BOT 2 a gagné !"+Fore.WHITE)
        time.sleep(3)
    
Battle(100, 100, 0, 0)
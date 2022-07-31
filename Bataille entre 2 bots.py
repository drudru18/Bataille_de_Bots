""" Bataille entre 2 bots
Code écrit entièrement par DRU"""

from colorama import Fore, Back, Style
import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        if len(self.name) > 20:
            self.name = self.name[:19]
        Battle(100, 100, 0, 0, 0, 0, 0, 0, self.name)
        

class Battle(Player):
    def __init__(self, life1, life2, combo1, combo2, win1, win2, lose1, lose2, name):
        self.start = time.time()
        self.lose1 = lose1
        self.lose2 = lose2
        self.win1 = win1
        self.win2 = win2
        self.name = name
        self.combo1 = combo1
        self.combo2 = combo2
        self.life1 = life1
        time.sleep(random.uniform(1, 2))
        print(20*"\n"+'\033[1m'+"|"+Fore.LIGHTGREEN_EX+self.life1*"O"+Fore.WHITE+'\033[1m'+"|\t •BOT 1•"+"\n")
        self.life2 = life2
        print('\033[1m'+"|"+Fore.LIGHTGREEN_EX+self.life2*"O"+Fore.WHITE+'\033[1m'+"|\t •BOT 2•"+"\n")
        if self.life1 <= 0 or self.life2 <= 0:
            self.__str__()
        else:
            self.random = random.randint(1, 2)
            if self.random == 1:
                self.bot1()
            self.bot2()
        self.ou = str(input(30*"\n"+'\033[0m'+"Voulez-vous recommencer un combat sous le pseudo "+'\033[1m'+self.name.upper()+'\033[0m'+" ? OUI/NON \n -->  "+'\033[1m'))
        if self.ou.lower() == "oui":
            Battle(100, 100, 0, 0, self.win1, self.win2, self.lose1, self.lose2, self.name)
        elif self.ou.lower() == "non":
            print("\nCe programme se ferme")
            time.sleep(0.5)
            exit()
        else:
            print("Coisissez oui ou non ! (ce programme se ferme)")
            time.sleep(0.5)
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
        return Battle(self.life1, self.life2, self.combo1, self.combo2, self.win1, self.win2, self.lose1, self.lose2, self.name)
    
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
        return Battle(self.life1, self.life2, self.combo1, self.combo2, self.win1, self.win2, self.lose1, self.lose2, self.name)

    def attack(self):
        self.damage = random.randint(8, 12)
    
    def leaderboard(self):
        with open("log.txt", "a") as file:
            file.write("Username:\t"+self.name.upper()+"\t\tTemps passé: "+str(round(self.total_time, 2))+" sec.\n\nBot_1\t\tCombats Gagnés:\t"+str(self.win1)+"\t\tCombats Perdus:\t"+str(self.lose1)+"\nBot_2\t\tCombats Gagnés:\t"+str(self.win2)+"\t\tCombats Perdus:\t"+str(self.lose2)+"\n\n----------------------------------------------------------------------\n\n")
        
    def __str__(self):
        if self.life1 > self.life2:
            print(Fore.LIGHTRED_EX+'\033[1m'+"Le BOT 1 a gagné !"+Fore.WHITE)
            self.win1+=1
            self.lose2+=1
        else:
            print(Fore.LIGHTRED_EX+'\033[1m'+"Le BOT 2 a gagné !"+Fore.WHITE)
            self.win2+=1
            self.lose1+=1
        self.end = time.time()
        self.total_time = self.end - self.start
        self.leaderboard()
        time.sleep(3)
    
Player(str(input("Veuillez entrer votre nom d'utilisateur: ")))
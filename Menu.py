from Logs.logs import Logs
import time
class Menu:
    def __init__(self):
        self.file = Logs().file
        self.lis = []
        self.load = Logs().load_log_content()
    
    def menu(self):
        self.value = str(input("\n\n\n\n\n\nWelcome !\n\nType 1 to play a match\nType 2 to delete one or more Usernames from the database\nType 3 to show the leaderboard (Coming Soon :) )\nType 4 to close the program\n\n  -> "))
        if self.value == "1":
            imp = __import__("Bataille entre 2 bots")
            return imp.Player(str(input("Veuillez entrer votre nom d'utilisateur: ")), time.time())
        elif self.value == "2":
            return self.choose_name()
        elif self.value == "3":
            #self.leaderboard()
            print("Leaderboard coming soon !")
            time.sleep(3)
            return self.menu()
        elif self.value == "4":
            exit()
        else:
            print("No Good, type 1, 2, 3 or 4")
            time.sleep(3)
            return self.menu()

    def choose_name(self):
        if self.load == {}:
            print("Database is empty ! Play a match to fill it :)")
            time.sleep(3)
            return self.menu()
        else:
            self.name_choice = str(input("Type an Username you would like to delete from the database or tap Enter if you have done\n-> "))
            while self.name_choice != "":
                self.lis.append(self.name_choice.lower())
                self.choose_name()
            self.delete_elem()

    def delete_elem(self):
        for i in range(len(self.lis)):
            if self.lis[i] in self.load:
                self.load.pop(self.lis[i])
                Logs().write_log_content(self.load)
                print(self.lis[i]+" removed")
                time.sleep(1)
            else:
                print(self.lis[i]+" hasn't played a game yet")
                time.sleep(1)
        print("DONE")
        time.sleep(1)
        return self.menu()

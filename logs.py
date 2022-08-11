import json

class Logs:
    def __init__(self):
        self.__file = "logs.json"

    def load_log_content(self):
        with open(self.__file, 'r') as f:
            return json.load(f)

    def write_log_content(self, log_dic):
        with open(self.__file, "w") as f:
            json.dump(log_dic, f, indent=4)

    def write_log(self, name, total_time, win1, lose1, win2, lose2):
        content = self.load_log_content()
        if name in content:
            content[name]["Total_time"].append(total_time)
            content[name]["Bot 1 Win"] += win1
            content[name]["Bot 1 Lose"] += lose1
            content[name]["Bot 2 Win"] += win2
            content[name]["Bot 2 Lose"] += lose2
        else:
            data = {
            "Total_time": [total_time],
            "Bot 1 Win": win1,
            "Bot 1 Lose": lose1,
            "Bot 2 Win": win2,
            "Bot 2 Lose": lose2
                }
            content[name] = data
        
        self.write_log_content(content)


    def __str__(self):
        content = self.load_log_content()
        stri = ""
        for players, data in content.items():
            stri += "Username:\t"+players.upper()+"\t\tTemps passé: "+str(round(sum(data["Total_time"]), 2))+" sec.\n\nBot_1\t\tCombats Gagnés:\t"+str(data["Bot 1 Win"])+"\t\tCombats Perdus:\t"+str(data["Bot 1 Lose"])+"\nBot_2\t\tCombats Gagnés:\t"+str(data["Bot 2 Win"])+"\t\tCombats Perdus:\t"+str(data["Bot 2 Lose"])+"\n\n----------------------------------------------------------------------\n\n"
        return stri

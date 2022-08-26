import json

class Logs:
    def __init__(self):
        self.file = "Logs/logs.json"

    def load_log_content(self):
        with open(self.file, 'r') as f:
            return json.load(f)

    def write_log_content(self, log_dic):
        with open(self.file, "w") as f:
            json.dump(log_dic, f, indent=4)
    
    def write_log(self, name, total_time, win1, lose1, win2, lose2):
        content = self.load_log_content()
        if name in content:
            content[name]["Total_time"].append(total_time)
            content[name]["Bot 1 Win"] += win1
            content[name]["Bot 1 Lose"] += lose1
            content[name]["Bot 2 Win"] += win2
            content[name]["Bot 2 Lose"] += lose2
            if content[name]["Bot 1 Lose"] == 0:
                content[name]["Ratio Bot 1"] = 100
            else:
                content[name]["Ratio Bot 1"] = round((content[name]["Bot 1 Win"]/(content[name]["Bot 1 Win"]+content[name]["Bot 1 Lose"]))*100, 2)
            if content[name]["Bot 2 Lose"] == 0:
                content[name]["Ratio Bot 2"] = 100
            else:
                content[name]["Ratio Bot 2"] = round((content[name]["Bot 2 Win"]/(content[name]["Bot 2 Win"]+content[name]["Bot 2 Lose"]))*100, 2)
        else:
            data = {
            "Total_time": [total_time],
            "Bot 1 Win": win1,
            "Bot 1 Lose": lose1,
            "Bot 2 Win": win2,
            "Bot 2 Lose": lose2,
            "Ratio Bot 1": win1*100,
            "Ratio Bot 2": win2*100,
                }
            content[name] = data
        
        self.write_log_content(content)


    def __str__(self):
        content = self.load_log_content()
        stri = ""
        for players, data in content.items():
            stri += "Username:\t"+players.upper()+"\t\tTemps passé: "+str(round(sum(data["Total_time"]), 2))+" sec.\n\nBot_1\t\tCombats Gagnés:\t"+str(data["Bot 1 Win"])+"\t\tCombats Perdus:\t"+str(data["Bot 1 Lose"])+"\t\tRatio: "+str(data["Ratio Bot 1"])+"%\nBot_2\t\tCombats Gagnés:\t"+str(data["Bot 2 Win"])+"\t\tCombats Perdus:\t"+str(data["Bot 2 Lose"])+"\t\tRatio: "+str(data["Ratio Bot 2"])+"%\n\nRatio calculé en fonction des matchs gagnés sur le total de ceux-ci\n\n----------------------------------------------------------------------\n\n"
        return stri

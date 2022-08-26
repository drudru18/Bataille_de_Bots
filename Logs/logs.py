import json

class Logs:
    def __init__(self):
        self.file = "Logs/logs.json"

    def load_log_content(self) -> dict:
        with open(self.file, 'r') as f:
            return json.load(f)

    def write_log_content(self, log_dic) -> None:
        with open(self.file, "w") as f:
            json.dump(log_dic, f, indent=4)
    
    def write_log(self, name, total_time, win1, lose1, win2, lose2) -> None:
        content = self.load_log_content()
        if name in content:
            data = content[name] # var to imporve code visibility
            data["Total_time"].append(total_time)
            data["Bot 1 Win"] += win1
            data["Bot 1 Lose"] += lose1
            data["Bot 2 Win"] += win2
            data["Bot 2 Lose"] += lose2
            if data["Bot 1 Lose"] == 0:
                data["Ratio Bot 1"] = 100
            else:
                data["Ratio Bot 1"] = round((data["Bot 1 Win"]/(data["Bot 1 Win"]+data["Bot 1 Lose"]))*100, 2)
            if data["Bot 2 Lose"] == 0:
                data["Ratio Bot 2"] = 100
            else:
                data["Ratio Bot 2"] = round((data["Bot 2 Win"]/(data["Bot 2 Win"]+data["Bot 2 Lose"]))*100, 2)
        else:
            new_data = {
            "Total_time": [total_time],
            "Bot 1 Win": win1,
            "Bot 1 Lose": lose1,
            "Bot 2 Win": win2,
            "Bot 2 Lose": lose2,
            "Ratio Bot 1": win1*100,
            "Ratio Bot 2": win2*100,
                }
            data = new_data
        content[name] = data
        
        self.write_log_content(content)

    def leaderboard(self) -> str:
        """
        This is a test function, to validate and improve by @Drudru18
        """
        leaderboard = "LeaderBoard: 🚀"
        content = self.load_log_content()
        best_ratio = [] # shows the best ratio (between Bot 1 - Bot 2) per player and sort it
        worst_ratio = [] # shows the worst ratio (between Bot 1 - Bot 2) per player and sort it
        most_win = [] # shows the bot which has the most win (between Bot 1 - Bot 2) per player and sort it
        most_time_spent = [] # shows wich player has played the most
        best_overall_bot = {"Bot 1": 0, "Bot 2": 0} # shows the bot who has the best overall ratio using all players data
        # could add more info to show on leaderboard, some of the above may not be fully relevant...

        for player, data in content.items():
            game_played = len(data["Total_time"])

            # === Adding best ratio per player ===
            if data["Ratio Bot 1"] >= data["Ratio Bot 2"]:
                biggest_ratio = data["Ration Bot 1"]
            else:
                biggest_ratio = data["Ratio Bot 2"]
            best_ratio.append([player, biggest_ratio])

            # === Adding worst ratio per player ===
            if data["Ratio Bot 1"] <= data["Ratio Bot 2"]:
                smallest_ratio = data["Ratio Bot 1"]
            else:
                smallest_ratio = data["Ratio Bot 2"]
            worst_ratio.append([player, smallest_ratio])

            # === Adding most win per player ===
            if data["Bot 1 Win"] >= data["Bot 2 Win"]:
                best_win = data["Bot 1 Win"]
            else:
                best_win = data["Bot 2 Win"]
            most_win.append([player, best_win])

            # === Adding time Spent
            most_time_spent.append([player, sum(data["Total_time"])])

            # == Adding wins / lose for overall 
            best_overall_bot["Bot 1"] += data["Bot 1 Win"]
            best_overall_bot["Bot 2"] += data["Bot 2 Win"]

            # still has to sort all of the lists and create the string containing the leaderboard itself :)

                           


        
        

    def __str__(self) -> str:
        content = self.load_log_content()
        stri = ""
        for players, data in content.items():
            stri += "Username:\t"+players.upper()+"\t\tTemps passé: "+str(round(sum(data["Total_time"]), 2))+" sec.\n\nBot_1\t\tCombats Gagnés:\t"+str(data["Bot 1 Win"])+"\t\tCombats Perdus:\t"+str(data["Bot 1 Lose"])+"\t\tRatio: "+str(data["Ratio Bot 1"])+"%\nBot_2\t\tCombats Gagnés:\t"+str(data["Bot 2 Win"])+"\t\tCombats Perdus:\t"+str(data["Bot 2 Lose"])+"\t\tRatio: "+str(data["Ratio Bot 2"])+"%\n\nRatio calculé en fonction des matchs gagnés sur le total de ceux-ci\n\n----------------------------------------------------------------------\n\n"
        return stri

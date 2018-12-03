import pandas as pd
stats = pd.read_csv("Players_stats.csv", sep = ",")
pd.set_option("display.max_columns", 35)
pd.set_option("display.max_rows", 492)
def PPG(navn):
    for i in navn:
        points = stats.loc[lambda stats: stats['Name'] == i, "PTS"]
        games = stats.loc[lambda stats: stats['Name'] == i, "Games Played"]
        PPG = points / games
        print(i, " hadde en PPG average på", PPG.values, " i sesongen 2014-15")
        
def PPM(players):
    for i in players:
        points = stats.loc[lambda stats: stats['Name'] == i, "PTS"]
        Min = stats.loc[lambda stats: stats['Name'] == i, "MIN"]
        PPM = points / Min
        print(i, " hadde en PPM average på", PPM.values, " i sesongen 2014-15")
        
def show(players):
    for i in players:
        s = stats.loc[lambda stats: stats['Name'] == i]
        print(s)

def stat(player, stat):
    for i in player:
        s = stats.loc[lambda stats: stats['Name'] == i, stat]
        print("I sesongen 2014-15 så hadde ", i, " en ", stat, " på ", s.values)

def Team(lagg):
    for lag in lagg:
        print("---------", lag, "---------")
        players = []
        PTS = []
        REB = []
        STL = []
        TO = []
        PER = []
        AST = []
        for i in range(490):
            d = stats.loc[lambda stats: i, "Team"]
            if d == lag:
                print(stats.loc[lambda stats: i, "Name"])
                players.append(stats.loc[lambda stats: i, "Name"])
        for f in players:
            points = stats.loc[lambda stats: stats["Name"] == f, "PTS"]
            PTS.append(points.values)
            reb = stats.loc[lambda stats: stats["Name"] == f, "REB"]
            REB.append(reb.values)
            steals = stats.loc[lambda stats: stats["Name"] == f, "STL"]
            STL.append(steals.values)
            turn = stats.loc[lambda stats: stats["Name"] == f, "TOV"]
            TO.append(turn.values)
            percent = stats.loc[lambda stats: stats["Name"] == f, "FG%"]
            PER.append(percent.values)
            assist = stats.loc[lambda stats: stats["Name"] == f, "AST"]
            AST.append(assist.values)
        PPG = sum(PTS) / 82
        RPG = sum(REB) / 82
        SPG = sum(STL) / 82
        TPG = sum(TO) / 82
        PG = sum(PER) / 82
        APG = sum(AST) / 82
        print(lag, " sin PPG er: ", PPG, ", rebounds per game er: ", RPG, ", steals per game er: ", SPG, ", ")
        print("turnovers per game er: ", TPG, ", average percentage er:", PG, ", assists per game er: ", APG)
        print("")

def Top(stat):
    s = stats.nlargest(10, stat)
    print(s)

def EFF(players):
    for i in players:
        pts = stats.loc[lambda stats: stats["Name"] == i, "PTS"]
        reb = stats.loc[lambda stats: stats["Name"] == i, "REB"]
        ast = stats.loc[lambda stats: stats["Name"] == i, "AST"]
        stl = stats.loc[lambda stats: stats["Name"] == i, "STL"]
        blk = stats.loc[lambda stats: stats["Name"] == i, "BLK"]
        fga = stats.loc[lambda stats: stats["Name"] == i, "FGA"]
        fgm = stats.loc[lambda stats: stats["Name"] == i, "FGM"]
        fta = stats.loc[lambda stats: stats["Name"] == i, "FTA"]
        ftm = stats.loc[lambda stats: stats["Name"] == i, "FTM"]
        to = stats.loc[lambda stats: stats["Name"] == i, "TOV"]
        gp = stats.loc[lambda stats: stats["Name"] == i, "Games Played"]
        missFG = fga.values - fgm.values
        missFT = fta.values - ftm.values
        eff = (pts.values + reb.values + ast.values + stl.values + blk.values - missFG - missFT - to) / gp.values
        print(i, " hadde en efficiency på ", eff.values)
        




op = input("Hva vil du se?\n")
spillere = []
if op == "Vis stats":
    sant = True
    while sant:
        spiller = input("Hvilke spillere sine stats vil du se?\n")
        if spiller != "":
            spillere.append(spiller)
        elif spiller == "":
            sant = False
    show(spillere)
elif op == "PPG":
    sant = True
    while sant:
        spiller = input("Hvilke spillere sine stats vil du se?\n")
        if spiller != "":
            spillere.append(spiller)
        elif spiller == "":
            sant = False
    PPG(spillere)
elif op == "Single Stat":
    for i in range(1):
        spiller = input("Hvilken spiller sine stats vil du se?\n")
        spillere.append(spiller)
        statss = input("Hvilken stat vil du se?\n")
    stat(spillere, statss)
elif op == "Team":
    lag = input("Hvilket lag vil du se spillerne til?\n")
    Team(lag)
elif op == "EFF":
    sant = True
    while sant:
        spiller = input("Hvilke spillere sine stats vil du se?\n")
        if spiller != "":
            spillere.append(spiller)
        elif spiller == "":
            sant = False
    EFF(spillere)
elif op == "PPM":
    sant = True
    while sant:
        spiller = input("Hvilke spillere sine stats vil du se?\n")
        if spiller != "":
            spillere.append(spiller)
        elif spiller == "":
            sant = False
    PPM(spillere)
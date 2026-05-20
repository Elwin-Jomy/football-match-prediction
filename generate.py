import pandas as pd
import random
from itertools import permutations

teams = [
    "Arsenal", "Aston Villa", "Bournemouth",
    "Brentford", "Brighton", "Burnley",
    "Chelsea", "Crystal Palace", "Everton",
    "Fulham", "Leeds", "Liverpool",
    "Man City", "Man United", "Newcastle",
    "Nottingham Forest", "Sunderland",
    "Tottenham", "West Ham", "Wolves"
]

matches = []

matchweek = 1

for home, away in permutations(teams, 2):

    home_goals = random.randint(0, 5)
    away_goals = random.randint(0, 4)

    # Match Result
    if home_goals > away_goals:
        result = "H"
    elif away_goals > home_goals:
        result = "A"
    else:
        result = "D"

    # Random Form
    forms = ['W', 'D', 'L']

    hm = [random.choice(forms) for _ in range(5)]
    am = [random.choice(forms) for _ in range(5)]

    # Form points
    def calc_points(form):
        points = 0
        for f in form:
            if f == 'W':
                points += 3
            elif f == 'D':
                points += 1
        return points

    ht_form_pts = calc_points(hm)
    at_form_pts = calc_points(am)

    row = {
        "Date": "16/08/25",
        "HomeTeam": home,
        "AwayTeam": away,

        "FTHG": home_goals,
        "FTAG": away_goals,
        "FTR": result,

        "HTGS": random.randint(10, 80),
        "ATGS": random.randint(10, 80),

        "HTGC": random.randint(10, 70),
        "ATGC": random.randint(10, 70),

        "HTP": random.randint(0, 90),
        "ATP": random.randint(0, 90),

        "HM1": hm[0],
        "HM2": hm[1],
        "HM3": hm[2],
        "HM4": hm[3],
        "HM5": hm[4],

        "AM1": am[0],
        "AM2": am[1],
        "AM3": am[2],
        "AM4": am[3],
        "AM5": am[4],

        "MW": matchweek,

        "HTFormPtsStr": ''.join(hm),
        "ATFormPtsStr": ''.join(am),

        "HTFormPts": ht_form_pts,
        "ATFormPts": at_form_pts,

        "HTWinStreak3": int(hm[:3] == ['W','W','W']),
        "HTWinStreak5": int(hm == ['W']*5),

        "HTLossStreak3": int(hm[:3] == ['L','L','L']),
        "HTLossStreak5": int(hm == ['L']*5),

        "ATWinStreak3": int(am[:3] == ['W','W','W']),
        "ATWinStreak5": int(am == ['W']*5),

        "ATLossStreak3": int(am[:3] == ['L','L','L']),
        "ATLossStreak5": int(am == ['L']*5),

        "HTGD": random.randint(-30, 50),
        "ATGD": random.randint(-30, 50),

        "DiffPts": random.randint(-20, 20),
        "DiffFormPts": ht_form_pts - at_form_pts
    }

    matches.append(row)

    matchweek += 1

df = pd.DataFrame(matches)

df.to_csv("premier_league_2025.csv", index=False)

print("2025 season dataset generated successfully!")
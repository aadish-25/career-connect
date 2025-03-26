import pandas as pd
import json

df = pd.read_excel("updated_leaderboard.xlsx")

leaderboard_data = df[["Name", "Final Score"]].to_dict(orient="records")

with open("leaderboard.json", "w") as json_file:
    json.dump(leaderboard_data, json_file, indent=4)

print("Leaderboard JSON file generated successfully!")
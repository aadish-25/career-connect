import pandas as pd
import json
import os

# Get the base directory (career-connect)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Moves up one level

# Load the Excel file (assuming it's in Back-end)
excel_path = os.path.join(base_dir, "Back-end", "updated_leaderboard.xlsx")
df = pd.read_excel(excel_path)

# Convert to JSON format
leaderboard_data = df[["Name", "CGPA",  "LeetCode Score", "Final Score"]].to_dict(orient="records")

# Save JSON file in the existing Front-end directory
frontend_dir = os.path.join(base_dir, "Front-end")
json_path = os.path.join(frontend_dir, "leaderboard.json")

with open(json_path, "w") as json_file:
    json.dump(leaderboard_data, json_file, indent=4)

print(f"Leaderboard JSON file saved at: {json_path}")

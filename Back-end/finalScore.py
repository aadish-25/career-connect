import pandas as pd

df = pd.read_excel("dummy_student_data.xlsx") 

print("Columns in Excel file:", df.columns)

def calculate_score(row):
    cgpa_weight = 50
    leetcode_weight = 30
    internship_weight = 20

#Not final algo will change its for dummy data only
    final_score = (
        row["CGPA"] * cgpa_weight +
        row["LeetCode Score"] * leetcode_weight +
        row["Internships"] * internship_weight
    )
    return final_score #will change the formula later for trial only 

df["Final Score"] = df.apply(calculate_score, axis=1)

#To arrange the final score 
df = df.sort_values(by="Final Score", ascending=False)

df.to_excel("updated_leaderboard.xlsx", index=False)

print("Leaderboard updated successfully!")

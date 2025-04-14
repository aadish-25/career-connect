import pandas as pd
import os

# Define file paths
file_path = r"Back-end/dummy_student_data.xlsx"
output_file = r"Back-end/updated_leaderboard.xlsx"

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# Read the Excel file
df = pd.read_excel(file_path)

# Print column names to verify correct loading
print("Columns in Excel file:", df.columns)

# Function to calculate the final score
def calculate_score(row):
    cgpa_weight = 50
    leetcode_weight = 30
    internship_weight = 20

    # Temporary formula for testing
    final_score = (
        row["CGPA"] * cgpa_weight +
        row["LeetCode Score"] * leetcode_weight +
        row["Internships"] * internship_weight
    )
    return final_score/100  

# Apply score calculation to each row
df["Final Score"] = df.apply(calculate_score, axis=1)

# Sort by Final Score in descending order
df = df.sort_values(by="Final Score", ascending=False)

# Save updated data to a new Excel file
df.to_excel(output_file, index=False)

print(f"Leaderboard updated successfully! Saved as: {output_file}")

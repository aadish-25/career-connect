# 📌 README: Leaderboard System

This project automates the ranking of students based on **CGPA, LeetCode Score, and Internship/Open-Source Experience**. The process involves calculating a **Final Score**, sorting the students in descending order, and updating the leaderboard on the website.

---

## **🚀 Workflow**

1️⃣ **Run the `finalScore.py` script**

- This script reads data from `dummy_student_data.xlsx`.
- It calculates the **Final Score** using weighted values.
- The students are sorted in **descending order** based on their score.
- The updated data is saved in `updated_leaderboard.xlsx`.

2️⃣ **Run the `excel_to_json.py` script**

- Converts the sorted `updated_leaderboard.xlsx` file to a **JSON file** (`leaderboard.json`).
- This JSON file will be used to update the leaderboard dynamically on the website.

3️⃣ **Integrate with the Frontend**

- The `leaderboard.json` file is used in the HTML file to display the updated leaderboard.
- A JavaScript script reads `leaderboard.json` and updates the leaderboard **automatically**.

---

## **📌 Requirements**

Make sure you have Python installed along with the required libraries:

```bash
pip install pandas openpyxl json
```

## **⚡ Running the Scripts**

```bash
python finalScore.py      # Step 1: Calculate Scores and Sort
python excel_to_json.py   # Step 2: Convert Excel to JSON
```

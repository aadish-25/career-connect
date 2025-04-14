// Function to fetch and populate leaderboard
async function populateLeaderboard() {
    try {
        const response = await fetch("leaderboard.json");
        const students = await response.json();

        console.log("response");

        const tbody = document.getElementById("leaderboard-details");
        tbody.innerHTML = ""; // Clear existing rows

        students.forEach((student, index) => {
            const row = document.createElement("tr");
            row.classList.add("text-center");

            row.innerHTML = `
                <td class="border p-2">${index + 1}</td>
                <td class="border p-2">${student.Name}</td>
                <td class="border p-2">${student.CGPA}</td>
                <td class="border p-2">${student["LeetCode Score"]}</td>
                <td class="border p-2">${student["Final Score"]}</td>
            `;

            tbody.appendChild(row);
        });
    } catch (error) {
        console.error("Error fetching leaderboard data:", error);
    }
}

// Call function after page loads
document.addEventListener("DOMContentLoaded", populateLeaderboard);

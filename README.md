# Campus Shuttle Routing & Capacity Scheduling

**Course:** Design and Analysis of Algorithms (DAA)  
**Programming Language:** Python

---

## 📌 Project Overview
In large university campuses, shuttle services are used to transport students and staff
between different locations. Inefficient routing and poor capacity planning can increase
travel time and reduce shuttle utilization.

This project focuses on:
- Finding the shortest routes between campus stops
- Efficiently assigning shuttle capacity based on passenger demand

---

## 🎯 Objectives
- To compute the shortest path between campus locations
- To apply greedy techniques for shuttle capacity scheduling
- To demonstrate practical usage of DAA algorithms

---

## 🧠 Algorithms Used

### 1. Dijkstra’s Algorithm
- Used to calculate the shortest distance from a source stop to all other stops
- Greedy-based shortest path algorithm
- **Time Complexity:** O((V + E) log V)

### 2. Greedy Scheduling Algorithm
- Used to assign shuttle routes based on passenger demand
- Routes with higher demand are prioritized
- **Time Complexity:** O(n log n)

---

## 🛠️ Tools & Technologies
- Python 3
- VS Code
- Standard Python Library (`heapq`)

---

## ▶️ How to Run the Project
1. Open the project folder in terminal
2. Run the command:
```bash
python shuttle_routing.py

# Comparative Analysis of Prim's and Kruskal's Algorithms for Minimum Spanning Tree

## Overview

This project implements and compares two popular Minimum Spanning Tree (MST) algorithms:

- Prim's Algorithm
- Kruskal's Algorithm

The application allows users to input a weighted undirected graph and generates the Minimum Spanning Tree using both algorithms.

---

## Features

✅ User-friendly Streamlit interface  
✅ Implementation of Prim's Algorithm using Min Heap  
✅ Implementation of Kruskal's Algorithm using Union-Find  
✅ Displays MST edges and total cost  
✅ Easy deployment on Streamlit Cloud

---

## Algorithms Used

### Prim's Algorithm

- Starts from a chosen vertex.
- Grows the MST by selecting the minimum-weight edge connecting the tree to a new vertex.

**Time Complexity:** O(E log V)

**Space Complexity:** O(V)

---

### Kruskal's Algorithm

- Sorts all edges by weight.
- Adds edges one by one while avoiding cycles using Union-Find.

**Time Complexity:** O(E log E)

**Space Complexity:** O(V)

---

## Project Structure

```text
MST-Algorithms/
│
├── app.py
├── program.py
├── requirements.txt
└── README.md
```

---

## Sample Input

Number of Vertices:

```text
4
```

Edges:

```text
0 1 4
0 2 3
1 2 1
1 3 2
2 3 5
```

Starting Vertex:

```text
0
```

---

## Sample Output

### Kruskal's MST

```text
(1 - 2) Weight = 1
(1 - 3) Weight = 2
(0 - 2) Weight = 3

Total Cost = 6
```

### Prim's MST

```text
(0 - 2) Weight = 3
(2 - 1) Weight = 1
(1 - 3) Weight = 2

Total Cost = 6
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/MST-Algorithms.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Deployment on Streamlit Cloud

1. Push the project to GitHub.
2. Go to https://streamlit.io/cloud
3. Click **New App**.
4. Select your GitHub repository.
5. Set:

```text
Main file path: app.py
```

6. Click **Deploy**.

---

## Applications of MST

- Computer Networks
- Road Construction
- Electrical Grid Design
- Network Routing
- Clustering in Machine Learning

---

## Author

ELAMATHI S
B.Tech AI&DS 
Chennai Institute of Technology

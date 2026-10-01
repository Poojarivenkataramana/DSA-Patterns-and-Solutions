# ⚡ Data Structures & Algorithms (DSA) Patterns & Solutions in Python

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![DSA Patterns](https://img.shields.io/badge/DSA-Patterns%20%26%20Techniques-orange.svg)](https://github.com/Poojarivenkataramana)
[![Problems Solved](https://img.shields.io/badge/Solved-19%20Problems-success.svg)](#-problem-index)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Profile](https://img.shields.io/badge/GitHub-Poojarivenkataramana-black?logo=github)](https://github.com/Poojarivenkataramana)

A curated collection of **Data Structures and Algorithms (DSA)** problems solved in Python, organized by fundamental algorithmic patterns. Each solution includes real-world scenarios, clean modular code, step-by-step intuition, brute-force vs. optimized comparisons, and rigorous **Time & Space Complexity** analysis.

---

## 📌 Table of Contents
- [🧠 Algorithmic Patterns Covered](#-algorithmic-patterns-covered)
  - [1. Sliding Window Pattern](#1-sliding-window-pattern)
  - [2. Two Pointers Pattern](#2-two-pointers-pattern)
- [📂 Repository Structure](#-repository-structure)
- [📋 Problem Index](#-problem-index)
  - [🪟 Sliding Window Solutions (7 Problems)](#-sliding-window-solutions)
  - [👉 Two Pointers Solutions (12 Problems)](#-two-pointers-solutions)
- [🚀 Quick Start & How to Run](#-quick-start--how-to-run)
- [🗺️ Learning Roadmap](#-learning-roadmap)
- [👤 Author](#-author)

---

## 🧠 Algorithmic Patterns Covered

### 1. Sliding Window Pattern
The **Sliding Window** technique avoids redundant re-computation over contiguous subarrays or subsegments of size $k$. Instead of recalculating the window properties from scratch ($O(n \cdot k)$), we slide the window by subtracting the leaving left element and adding the entering right element in $O(1)$ per step ($O(n)$ overall).

```text
[ 12,   8,  15,  20,   7,  18,  10 ]  k = 3
  └─────────────┘                      -> Window 1 (sum = 35)
        └─────────────┘                -> Window 2 (sum = 35 - 12 + 20 = 43)
              └─────────────┘          -> Window 3 (sum = 43 - 8 + 7 = 42)
                    └─────────────┘    -> Window 4 (sum = 42 - 15 + 18 = 45) [MAX]
```

**Key Sub-Patterns:**
* **Fixed-size Window Sum / Min / Max**: Maintain running aggregate during sliding.
* **Window Condition Counting**: Track whether running window metrics meet given business thresholds.
* **State Tracking (Positive / Even Count)**: Dynamically increment/decrement counts based on elements entering and leaving.

---

### 2. Two Pointers Pattern
The **Two Pointers** technique uses two index pointers to traverse data structures in tandem, significantly reducing time complexity (often from $O(n^2)$ to $O(n)$) and achieving $O(1)$ auxiliary space.

```text
Opposite Direction (Converging):
[ 2,   4,   5,   7,   9,   11,   15 ]  Target = 16
  ↑                               ↑
 Left                           Right  -> (2 + 15 = 17 > 16) => Move Right Leftward
       ↑                  ↑
      Left              Right          -> (5 + 11 = 16 == 16) => Found Pair!

Same Direction (Fast & Slow):
[ 150,   0,   200,   350,   0,   500 ]
  ↑      ↑
 Slow   Fast   -> Slow tracks insertion position, Fast scans valid elements.
```

**Key Sub-Patterns:**
* **Opposite Direction (Converging)**: Search pairs in sorted arrays, container capacity, palindrome verification.
* **Fast & Slow Pointers (Same Direction)**: In-place array modification (e.g., removing duplicates, moving zeroes).
* **Parallel Traversal Across Arrays**: Finding common elements or merging sorted sequences in $O(n + m)$.
* **Fixed Pointer + Two Pointers**: Solving triplet problems like 3Sum in $O(n^2)$ with duplicate handling.

---

## 📂 Repository Structure

```tree
DSA/
├── README.md
├── .gitignore
├── sliding_window/
│   ├── 01_max_sum_subarray_k.py
│   ├── 02_min_sum_subarray_k.py
│   ├── 03_count_high_activity_periods.py
│   ├── 04_max_spending_k_days.py
│   ├── 05_max_positive_days_in_window.py
│   ├── 06_max_even_ids_in_window.py
│   └── 07_daily_sales_max_window.py
│
└── two_pointers/
    ├── 01_two_sum_sorted.py
    ├── 02_remove_duplicates_inplace.py
    ├── 03_move_zeroes_to_end.py
    ├── 04_container_with_most_water.py
    ├── 05_customer_purchase_pair.py
    ├── 06_delivery_package_pair.py
    ├── 07_reverse_array_inplace.py
    ├── 08_intersection_two_sorted_arrays.py
    ├── 09_valid_palindrome_basic.py
    ├── 10_valid_palindrome_alphanumeric.py
    ├── 11_sorted_squares.py
    └── 12_three_sum.py
```

---

## 📋 Problem Index

### 🪟 Sliding Window Solutions

| # | Problem File | Scenario / Problem Description | LeetCode Equivalent | Time | Space |
|---|---|---|---|:---:|:---:|
| 1 | [`01_max_sum_subarray_k.py`](sliding_window/01_max_sum_subarray_k.py) | Max Total Sales in any $k$ consecutive days | LC 643 (Variant) | $O(n)$ | $O(1)$ |
| 2 | [`02_min_sum_subarray_k.py`](sliding_window/02_min_sum_subarray_k.py) | Min Temperature Sum in $k$ consecutive days | Min Subarray Sum | $O(n)$ | $O(1)$ |
| 3 | [`03_count_high_activity_periods.py`](sliding_window/03_count_high_activity_periods.py) | Count $k$-day windows with total activity $\ge$ threshold | Window Counter | $O(n)$ | $O(1)$ |
| 4 | [`04_max_spending_k_days.py`](sliding_window/04_max_spending_k_days.py) | Best Customer Spending over 4 consecutive days | Max Subarray Sum | $O(n)$ | $O(1)$ |
| 5 | [`05_max_positive_days_in_window.py`](sliding_window/05_max_positive_days_in_window.py) | Max positive profit days in any $k$-day window (BF & Opt) | State Tracking | $O(n)$ | $O(1)$ |
| 6 | [`06_max_even_ids_in_window.py`](sliding_window/06_max_even_ids_in_window.py) | Max even transaction IDs in any $k$-day window (BF & Opt) | State Tracking | $O(n)$ | $O(1)$ |
| 7 | [`07_daily_sales_max_window.py`](sliding_window/07_daily_sales_max_window.py) | Max daily sales window sum introduction | LC 643 | $O(n)$ | $O(1)$ |

---

### 👉 Two Pointers Solutions

| # | Problem File | Scenario / Problem Description | LeetCode Equivalent | Time | Space |
|---|---|---|---|:---:|:---:|
| 1 | [`01_two_sum_sorted.py`](two_pointers/01_two_sum_sorted.py) | Two Sum in a sorted array | LC 167 | $O(n)$ | $O(1)$ |
| 2 | [`02_remove_duplicates_inplace.py`](two_pointers/02_remove_duplicates_inplace.py) | Remove duplicate customer IDs in-place | LC 26 | $O(n)$ | $O(1)$ |
| 3 | [`03_move_zeroes_to_end.py`](two_pointers/03_move_zeroes_to_end.py) | Move failed (0) transactions to end in-place | LC 283 | $O(n)$ | $O(1)$ |
| 4 | [`04_container_with_most_water.py`](two_pointers/04_container_with_most_water.py) | Warehouse Container Max Material Capacity | LC 11 | $O(n)$ | $O(1)$ |
| 5 | [`05_customer_purchase_pair.py`](two_pointers/05_customer_purchase_pair.py) | Find two purchase amounts summing to target | LC 167 (Variant) | $O(n)$ | $O(1)$ |
| 6 | [`06_delivery_package_pair.py`](two_pointers/06_delivery_package_pair.py) | Find two delivery package weights summing to target | LC 167 (Variant) | $O(n)$ | $O(1)$ |
| 7 | [`07_reverse_array_inplace.py`](two_pointers/07_reverse_array_inplace.py) | Reverse customer ID list in-place | LC 344 | $O(n)$ | $O(1)$ |
| 8 | [`08_intersection_two_sorted_arrays.py`](two_pointers/08_intersection_two_sorted_arrays.py) | Common product IDs across two sorted warehouses | LC 349 / 350 | $O(n+m)$ | $O(\min(n,m))$ |
| 9 | [`09_valid_palindrome_basic.py`](two_pointers/09_valid_palindrome_basic.py) | Transaction code exact palindrome verification | LC 125 (Basic) | $O(n)$ | $O(1)$ |
| 10 | [`10_valid_palindrome_alphanumeric.py`](two_pointers/10_valid_palindrome_alphanumeric.py) | Valid Palindrome with punctuation & case ignoring | LC 125 | $O(n)$ | $O(1)$ |
| 11 | [`11_sorted_squares.py`](two_pointers/11_sorted_squares.py) | Sensor sorted squared values without $O(n \log n)$ sort | LC 977 | $O(n)$ | $O(n)$ |
| 12 | [`12_three_sum.py`](two_pointers/12_three_sum.py) | 3Sum: Budget Match & Unique Triplet Extraction | LC 15 | $O(n^2)$ | $O(1)$ |

---

## 🚀 Quick Start & How to Run

### Prerequisites
- Python 3.10+ installed on your machine.
- Git.

### Clone the Repository
```bash
git clone https://github.com/Poojarivenkataramana/DSA-Patterns-and-Solutions.git
cd DSA-Patterns-and-Solutions
```

### Run Any Specific Solution
```bash
# Run a Sliding Window solution
python3 sliding_window/01_max_sum_subarray_k.py

# Run a Two Pointers solution
python3 two_pointers/12_three_sum.py
```

### Run All Solutions
```bash
for file in sliding_window/*.py two_pointers/*.py; do
    echo "▶ Running $file..."
    python3 "$file"
    echo ""
done
```

---

## 🗺️ Learning Roadmap

- [x] **Sliding Window (Fixed Size)**
- [ ] **Sliding Window (Dynamic / Variable Size)**
- [x] **Two Pointers (Opposite Direction)**
- [x] **Two Pointers (Fast & Slow Pointers)**
- [x] **Two Pointers (Multi-Array & 3Sum)**
- [ ] **Prefix Sum & Difference Arrays**
- [ ] **Binary Search & Variants**
- [ ] **Monotonic Stack & Queue**
- [ ] **Linked Lists & Floyd's Cycle Detection**
- [ ] **Trees, BST & Tree Traversals**
- [ ] **Graph Algorithms (BFS, DFS, Dijkstra)**
- [ ] **Dynamic Programming (1D & 2D)**

---

## 👤 Author

**Poojari Venkataramana**
- GitHub: [@Poojarivenkataramana](https://github.com/Poojarivenkataramana)

---

⭐ *If you find this repository helpful for your DSA preparation, feel free to star the repo!*

# 🌧️ Trapping Rain Water — LeetCode 42

**Problem Link:** [trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/)

---

## Practice Count

`1 / 5`

---

## Approach

**Monotonic Stack (Index-based)**

* Store **indices** in the stack (not heights) to calculate width
* When a **higher bar appears**, compute trapped water using:

  | Term     | Meaning                     |
  | -------- | --------------------------- |
  | `bottom` | popped index (valley floor) |
  | `left`   | new stack top (left wall)   |
  | `right`  | current index (right wall)  |

---

## Core Rules

* Water can **only** be trapped when there are **walls on both sides**
* Water height is limited by the **shorter wall**
* Each trapped block is calculated as:

```
(min(left_wall, right_wall) - floor_height) × width
```

---

## ⏱ Complexity

```
Time  : O(n)
```


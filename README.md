![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)

![OR-Tools](https://img.shields.io/badge/Google-OR--Tools-green?style=for-the-badge)

![Optimization](https://img.shields.io/badge/Operations-Research-orange?style=for-the-badge)
# Nurse Scheduling using OR-Tools

## Problem

This project solves a nurse scheduling problem using Google OR-Tools CP-SAT.

The model assigns nurses to shifts while satisfying scheduling constraints and balancing workloads.

---

##  Features

- Exactly one nurse per shift
- At most one shift per nurse per day
- Rest constraints after night shifts
- Balanced workload distribution
- Fair scheduling

---

##  Tools Used

- Python
- Google OR-Tools
- CP-SAT Solver

---

##  Optimization Constraints

- No consecutive night shifts
- No morning shift after night shift
- Nurse 0 and Nurse 1 cannot work night shifts
- Minimized workload deviations

---

##  Run the Code

```bash
python main.py
```

---

##  Concepts Used

- Constraint Programming
- Scheduling Optimization
- Operations Research
- Workforce Planning

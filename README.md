# first-python-repo

A small Python script that reads `expenses.csv` and prints a summary:
total, total per category, the most expensive item, and the number of expenses.

## How to run
```
python -m venv .venv
.venv\Scripts\activate
python summarize.py
```

## Result
```
Total: 49.75 JOD
food: 25.75 JOD
transport: 9.00 JOD
internet: 15.00 JOD
Most expensive: groceries (23.50 JOD)
Number of expenses: 5
```

## Limitation
The file name `expenses.csv` is fixed in the code, so the script only works when run from this folder.
import csv
count = 0
total = 0.0
totals_by_category = {}
most_expensive = None

with open("expenses.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row["amount_jod"])
        category = row["category"]
        total += amount
        count += 1
        totals_by_category[category] = totals_by_category.get(category, 0) + amount
        if most_expensive is None or amount > float(most_expensive["amount_jod"]):
            most_expensive = row

print(f"Total: {total:.2f} JOD")
for category, value in totals_by_category.items():
    print(f"{category}: {value:.2f} JOD")
print(f"Most expensive: {most_expensive['item']} ({most_expensive['amount_jod']} JOD)")
print(f"Number of expenses: {count}")
average = total / count
print(f"Average expense: {average:.2f} JOD")
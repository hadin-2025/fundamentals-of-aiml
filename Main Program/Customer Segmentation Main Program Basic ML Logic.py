customers = [
    ["Amit", 30000, 40],
    ["Riya", 60000, 80],
    ["John", 25000, 20],
    ["Sara", 58000, 75],
    ["Raj", 90000, 30]
]

# Calculate averages
total_income = 0
total_spending = 0

for c in customers:
    total_income += c[1]
    total_spending += c[2]

avg_income = total_income / len(customers)
avg_spending = total_spending / len(customers)

print("Avg Income:", avg_income)
print("Avg Spending:", avg_spending)

# Classification based on learned thresholds
for c in customers:
    name, income, spending = c

    if income > avg_income and spending > avg_spending:
        segment = "High Value"
    elif income > avg_income:
        segment = "Wealthy"
    elif spending > avg_spending:
        segment = "Big Spender"
    else:
        segment = "Low Value"

    print(name, "->", segment)

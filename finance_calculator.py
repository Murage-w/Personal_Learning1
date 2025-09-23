## Operation to calculate and provide feedback on a user's monthly and potential future savings.

# User Input for Financial Details.

monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculations for Monthly Savings.

monthly_savings = monthly_income - total_monthly_expenses
projected_annual_savings = monthly_savings * 12 * (monthly_savings * 12 * 0.05)

# Results

print(f"Your monthly savings are ${monthly_savings:,}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:,.0f}.")

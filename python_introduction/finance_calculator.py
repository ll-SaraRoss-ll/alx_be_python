monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
one_year = 12

projected_savings = monthly_savings * one_year + (monthly_savings * one_year * interest_rate)

print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)

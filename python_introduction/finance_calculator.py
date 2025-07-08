monthlyIncome = int(input("Enter your monthly income: "))
monthlyExprenses = int(input("Enter your total monthly expenses: "))
monthlySavings = monthlyIncome - monthlyExprenses
interestRate = 0.05
oneYear = 12
ProjectedSavings = monthlySavings * oneYear + (monthlySavings * oneYear * interestRate)
print("Your monthly savings are $",monthlySavings)
print("Projected savings after one year, with interest, is: $",ProjectedSavings)
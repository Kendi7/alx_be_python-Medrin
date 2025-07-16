income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
#Hello have added this one check this out and compare with yours
"""
monthly_income= int(input("Enter your monthly income:  "))
monthly_expenses=int(input( "Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

projected_Savings =(monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_Savings} .")
"""

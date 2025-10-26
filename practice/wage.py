departments = 4
employees = 5
days = 6
wages = 500

company_total = 0

for i in range(departments):
    dep_total = 0
    for j in range(employees):
        weekly = wages * days      # calculate weekly salary (don’t change wages)
        dep_total += weekly
    company_total += dep_total

print("Company total payroll: ₹", company_total)

salary = float(input("Enter your monthly salary: ") )
annual_salary = salary * 12
tax_slab ="No Tax" if annual_salary <= 500000 else "5% Tax" if annual_salary <= 500000 else "20% Tax" if annual_salary <= 1000000 else "30% Tax"
print(f"Monthly Salary: ₹{salary:,.0f}")
print(f"Annual Salary: ₹{annual_salary:,.0f}")
print(f"Applicable Tax Slab: {tax_slab}")
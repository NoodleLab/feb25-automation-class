import openpyxl

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Employee Salaries"

# Add headers
sheet.append(["Employee Name", "Salary (GHS)"])

# Sample employee data
employees = [
    ("John Doe", 5000),
    ("Jane Smith", 6200),
    ("David Johnson", 4500),
    ("Sarah Brown", 7000),
    ("Michael Lee", 5200),
]

# Add data to the sheet
for emp in employees:
    sheet.append(emp)

# Save the Excel file
wb.save("Employee_Salaries.xlsx")

print("Excel file 'Employee_Salaries.xlsx' created successfully!")

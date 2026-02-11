import numpy as np

salaries = np.array(
    [[4500, 4700, 4900, 5000],  # Employee 1
    [5500, 5600, 5800, 5900],   # Employee 2
    [4700, 4800, 4900, 5100],   # Employee 3
    [4000, 4200, 4300, 4500],   # Employee 4
    [6000, 6200, 6300, 6500],   # Employee 5
    [5200, 5300, 5400, 5600]])  # Employee 6

print(salaries)

total_salaries = np.sum(salaries, axis=1) # Sum across rows (employees)
print(f"Total salary earned by each employee: {total_salaries}")

average_salaries_per_month = np.mean(salaries, axis=0) # Average across column(employees)
print(f"Average salary for each month : {average_salaries_per_month}")

highest_salary_in_jan = np.argmax(salaries[:, 0]) # Find max salary in January(column 0)
highest_salary_in_feb = np.argmax(salaries[:, 1]) # Find max salary in February(column 1)
highest_salary_in_mar = np.argmax(salaries[:, 2]) # Find max salary in March(column 2)
highest_salary_in_apr = np.argmax(salaries[:, 3]) # Find max salary in April (column 3)

print(f"Employee with highest salary in January: Employee {highest_salary_in_jan }")
print(f"Employee with highest salary in February: Employee {highest_salary_in_feb}")
print(f"Employee with highest salary in March: Employee {highest_salary_in_mar}")
print(f"Employee with highest salary in April: Employee {highest_salary_in_apr}")

employees_above_5000 = np.all(salaries >= 5000, axis=1) # Check if all salary values for an employee are &gt; 5000
num_employees_above_5000 = np.sum(employees_above_5000) # Count the number of True values
print(f"Number of employees who earned above 5000 in all months:{num_employees_above_5000}")

month_with_highest_avg_salary = np.argmax(average_salaries_per_month) # Find the month with max avg salary
#print(&quot;Month with highest average salary across all employees:&quot;, month_with_highest_avg_salary)
months = ["January", "February", "March", "April"]

print(f"The month with the highest average salary is: {months[month_with_highest_avg_salary]}")
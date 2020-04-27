--New Companies
--https://www.hackerrank.com/challenges/the-company/problem

SELECT company.company_code, company.founder, count(distinct(lead_manager_code)), count(distinct(senior_manager_code)), count(distinct(manager_code)), count(distinct(employee_code))
FROM employee
LEFT JOIN company
ON company.company_code = employee.company_code
GROUP BY company.company_code, company.founder
ORDER BY company.company_code;

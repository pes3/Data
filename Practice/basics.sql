---nested queries ---
/*select * 
from employees
where state = 'CA'
and base_salary < (
--- here is said nested query, ie a query within a query to get the lowest base salary in Fl
select min(base_salary)
from employees
where state ='FL' 
);
*/


------- filtering basics-----
/*select first_name,last_name, phone, base_salary from employees
where base_salary > 5000*/

/*select first_name,last_name, phone, base_salary from employees
where base_salary between 1000 and 2000;*/

---select first_name, last_name, phone, base_salary
/*from employees
where base_salary in(1600, 2700, 4200)
giving results that just have the three listed base salaries*/



----working with dates basic

/*select *
from employees
where hire_date < '2005-1-1'
;*/

---basic carestian join for a reference of !***bad perofrmance***! ---
/*select first_name, last_name, name as departments_name
from employees, departments
where employees.department_id = departments.id
;*/
---alias, make more readable---
/*select e.id as employee_id, e.first_name, e.last_name, d.name as departments_name
from employees as e, departments as d
where e.department_id = d.id
and d.name = 'IT';*/

---Inner Join, standard. better performance---
/*select first_name, last_name, department_id, name as departments_name
from employees 
inner join departments 
on employees.department_id = departments.id
where name = 'Marketing';*/




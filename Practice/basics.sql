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


--- find table related to employees---
/*SELECT * FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE 'empl%'*/
---nested query & joins---
/*select e.first_name, e.last_name, d.name
from
(select *
from employees 
where state = 'FL') as e
inner join departments as d
on e.department_id = d.id;
--- right outer join returns unmatched emplyee records (shows null in emloyee column) and shows the department name ---
select e.first_name, e.last_name, d.name
from
(select *
from employees 
where state = 'FL') as e
right outer join departments as d
on e.department_id = d.id;
--- left outer join, shows all emlpoyees that match with departments as well as employees who are not assigned a department so department name shows null here---
select e.first_name, e.last_name, d.name
from
(select *
from employees 
where state = 'FL') as e
left outer join departments as d
on e.department_id = d.id;


--- full outer join  you see that rows that did not get matched on both tables reflect null values(its like your running left and right join)_---
select e.first_name, e.last_name, d.name
from
(select *
from employees 
where state = 'FL') as e
full outer join departments as d
on e.department_id = d.id;*/

---
---create new row, if you do not defineand line up the column names, then it just populates left to right--

/*insert into employees(id, first_name, last_name, state, department_id, job_title, base_salary)
values (394, 'Pete', 'Kline', 'GA', 1, 'Technician', 1800) */

/*insert into employees(id, first_name, last_name, state, department_id, job_title, base_salary)
values (394, 'Pete', 'Kline', 'GA', 1, 'Technician', 1800)

select * 
from employees 
where id  = 394*/


--- here we do not define column names because our we input enough values and in the right oorder

/*insert into employees
values(395, 'Pete', 'Kine', null, 'GA', null, null, null, null, 1, 'Technician', 1800, 0);*/

/*select * 
from employees
where id = 395*/

---  you need to specify record to aply update to!!!!------
/*update employees 
set address = '2826  Clemence St,, Atlanta', 
    zip_code = 30303,
    phone = '404-550-1015'
where id = 394;*/



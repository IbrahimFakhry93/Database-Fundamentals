

select * from employees where salary > all (select salary from employees where dno = 10)

-- aggregation

select count(salary) as salary_count, count(ssn) as employee from employees

select avg(salary) from employee group by dno having max(salary) > 1800
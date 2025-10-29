
--! Update Command:

--^ update alone is column level
--^ update + where condition = record level

select e."Fname" ,e."SSN" ,e."Salary"  from employee e ;

--* if there's no where condition, the DBM will update all the records (all employees of column salary to be 1200 
--* where condition specify a certain record or row



update employee e set "Salary" = 1200 where e."SSN" =102661;

select e."Fname" ,e."SSN" ,e."Salary" from employee e;

select e."Fname" ,e."SSN" ,e."Salary", e."Dno"  from employee e;

update employee e set "Salary" = 1800 , "Dno" = 30 where e."SSN" =102674;

select e."Fname" ,e."SSN" ,e."Salary", e."Dno"  from employee e;

--*====================================================================================

--! Delete Command:

--* Delete 

select e."Fname" ,e."SSN"  from employee e;

delete from employee e where e."SSN" = 102674;

select e."Fname" ,e."SSN"  from employee e;


--*====================================================================================

--! Select Command
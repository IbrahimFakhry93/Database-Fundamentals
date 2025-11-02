
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

--! Select Command:

--*====================================================================================

--! Comparison and Logical Operator

select e."Fname" ,e."Salary"  from employee e ;

select e."Fname" ,e."Salary"  from employee e where e."Salary" >1500;

select e."Fname",e."Salary" from employee e where e."Salary" >=1500 and e."Salary" <=2500;

--^ note: = , > , < are single row operator

--^ other syntax: using between + and
select e."Fname", e."Salary" from employee e where e."Salary" between 1500 and 2500; 

select * from employee e ;

select e."SSN" ,e."Fname" ,e."Superssn"  from employee e where e."Superssn" =321654 or e."Superssn" =223344 ;

--^ other syntax: using (in) multi row operator since we compare relative to same attribute (superssn)
select e."SSN" ,e."Fname" ,e."Superssn"  from employee e where e."Superssn" in (321654,223344);

--*====================================================================================

--! Like:
select e."Fname"  from employee e ;
select e."Fname" from employee e where e."Fname" like '_o%';

--^ LIKE in PostgreSQL is case‑sensitive → 'Ahm_d' matches Ahmad but not ahmad.
select e."Fname" from employee e where e."Fname" like 'Ahm_d'

--! ILike
--^ ILIKE is the case‑insensitive version → it ignores case, 
--^ so it matches both uppercase and lowercase.
select e."Fname" from employee e where e."Fname" ILike 'Ahm_d'

--*====================================================================================

--! Alias

select e."Fname" , e."Salary" * 0.1 as "Bonus" from employee e ;


select e."Fname" || ' ' || e."Lname" as "Full name", e."Salary" *12 as "Annual Salary" from employee e where e."Salary" * 12 > 10000;


--*====================================================================================

--! Order

select e."Fname" , e."SSN" from employee e order by e."Fname" desc;

--^ we can apply multi level of order
select e."Fname" , e."Dno" ,e."Salary" from employee e order by e."Dno" , e."Salary" desc; 

--*====================================================================================


--! Distinct

select distinct e."Dno"  from employee e;


select distinct e."Superssn" ,e."Dno"  from employee e;

--*=======================================================================================================================

--! inner join:

--^ Equ Join: , + where 
select e."Fname" ,d."Dname"  from employee e , department d where e."SSN" =d."MGRSSN" ;

--^ Inner Join: inner join + on
select e."Fname" ,d."Dname"  from  employee e inner join department d on e."SSN" =d."MGRSSN" ;

select e."Fname" ,d."Dname"  from employee e , department d where d."Dno" =e."Dno";

select e."Fname" ,d."Dname" from employee e , department d ;

--^ joining multiple tables
select e."Fname" ,p."Pname" , w."Hours"  from employee e ,projects p ,workon w 
where e."SSN" =w."ESSN" and p."Pnumber" =w."Pno" 
--*=======================================================================================================================

-- ! outer join:

select e."Fname" ,d."Dname"  from  employee e left outer join department d on e."SSN" =d."MGRSSN" ;
--*=======================================================================================================================

-- ! self join:

select e."Fname" as "Employee" ,s."Fname" as "Supervisor"  from employee e ,employee s where e."Superssn" = s."SSN" 

--*=======================================================================================================================
-- ! Sub_Queries:

select e."Fname", e."Salary"  from employee e where e."Salary" > (select e."Salary" from employee e where e."Fname" = 'Ahmed' and e."Lname" ='Ali' )


select e."Fname" from employee e where e."Salary"  > all (select e."Salary" from employee e where e."Dno" =10)

select e."Fname" from employee e where e."Salary"  > any (select e."Salary" from employee e where e."Dno" =10)

--^ ask chatgpt the difference between all and any

--& Comparison of ALL and ANY Operators in SQL

--? General Idea
--* Both ALL and ANY are used with comparison operators (>, <, =, etc.).
--* They compare a value against a set (often a subquery result).
--* The difference lies in how the comparison is evaluated across the set.

--? ALL
--* Condition must be TRUE for **every value** in the set.
--* Think: "value satisfies condition for all rows."
--* Example: salary > ALL (SELECT salary FROM interns)
   → TRUE only if salary is greater than the highest intern salary.

--? ANY (or SOME)
--* Condition must be TRUE for **at least one value** in the set.
--* Think: "value satisfies condition for at least one row."
--* Example: salary > ANY (SELECT salary FROM interns)
   → TRUE if salary is greater than the lowest intern salary.

--? Key Differences
--* ALL = stricter, requires condition to hold for every element.
--* ANY = looser, requires condition to hold for at least one element.
--* With equality (=):
   - col = ALL(subquery) → TRUE only if all values are equal to col.
   - col = ANY(subquery) → TRUE if col matches at least one value.

--? Key Learning Points
--* Use ALL when you want to compare against the maximum or minimum implicitly.
--* Use ANY when you want to check if a condition holds for at least one match.
--* Often paired with >, <, =, <> to express flexible conditions.

--*=======================================================================================================================

-- ! Aggregate function:

select max(e."Salary") as "max sal", min(e."Salary" ) as "min sal" from employee e;


select count(e."SSN") as "emp", count(e."Salary") from employee e;

--*=======================================================================================================================

--! Group by, having

select avg(e."Salary" ) as "Avg Sal", e."Dno" from employee e group by e."Dno" ;


select avg(e."Salary" ) as "Avg Sal", e."Dno" from employee e group by e."Dno"  having max(e."Salary" ) > 1800


--*=======================================================================================================================

--! SQL Conclusion:


select d."Dname" , max(e."Salary" ) as "max_sal" from employee e ,department d where e."Dno" = d."Dno" group by d."Dno" having avg(e."Salary" ) > 1200 order by "Dname"  ;




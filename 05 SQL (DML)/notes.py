#

#! Chapter 05: Data Manipulation Language (DML)

#! Lec 01: INSERT Command

# & SQL – Data Manipulation Language (DML)

# ? Definition
# * DML = Data Manipulation Language
# * Commands used to manipulate data inside tables
# ^ Main commands:
# *   - INSERT → add new records
# *   - UPDATE → modify existing records
# *   - DELETE → remove records
# *   - SELECT → retrieve/display data (show data)

# ? Example Schema (simplified)
# * Employees table
# * Departments table
# * Projects table
# * Dependents table
# * WorksFor table (M:N relationship between Employee & Project)
# * Employee1 (virtual copy for recursive relationship → SupervisorSSN as FK)

# ? INSERT Command
# ! Purpose: Add new data into a table
# ~ Syntax variations (3 ways):

# ^ 1. Insert with explicit column names (recommended)
# *   INSERT INTO Employees (SSN, Name, Salary, DOB)
# *   VALUES (123, 'Ahmed', 5000, '1990-05-10');
# * → Must match order of listed columns

# ^ 2. Insert without column names (requires knowing all columns & order)
# *   INSERT INTO Employees
# *   VALUES (123, 'Ahmed', 5000, '1990-05-10');
# * → Values must match table’s column order exactly

# ^ 3. Insert into selected columns only
# *   INSERT INTO Employees (SSN, Name)
# *   VALUES (124, 'Mona');
# * → Other columns remain NULL (if allowed)

# ? Key Notes
# * Character and date values must be enclosed in single quotes
# * Order of values must match order of columns
# * If inserting partial data, unspecified columns must allow NULL or have defaults
# * INSERT only creates structure of a new record; no updates to existing data

# *=========================================================================

#! Lec 02: UPDATE Command

# & SQL – UPDATE Statement

# ? Definition
# * UPDATE = command used to modify existing data in a table
# * Works on the column level (changes values of specific attributes)

# ? Syntax
# * UPDATE TableName
# * SET ColumnName = NewValue [, ColumnName2 = NewValue2, ...]
# * WHERE condition;

# ? Key Notes
# * WHERE clause specifies which record(s) to update
# * Without WHERE → all rows in the table will be updated (dangerous!)
# * Can update one or multiple columns in the same statement

# ? Example 1 – Update one column
# ^ Requirement: Update salary of employee with SSN = 101 to 1200
# *   UPDATE Employees
# *   SET Salary = 1200
# *   WHERE SSN = 101;

# ? Example 2 – Update multiple columns
# ^ Requirement: Update salary and department number of employee with SSN = 102
# *   UPDATE Employees
# *   SET Salary = 1500,
# *       DeptNo = 20
# *   WHERE SSN = 102;

# ? Comparison with INSERT
# * INSERT → adds a new record (row-level operation)
# * UPDATE → modifies existing record(s) (column-level operation)

# *=========================================================================

#! Lec 03: DELETE Command , TRUNCATE

# & SQL – DELETE vs TRUNCATE

# ? DELETE Command
# * Works on the record (row) level
# ^ Syntax:
# *   DELETE FROM TableName WHERE condition;
# * Without WHERE → deletes ALL rows in the table
# * With WHERE → deletes only specific records
# ~ Example:
# *   DELETE FROM Employees WHERE SSN = 101;

# ? TRUNCATE Command
# * Deletes ALL data from a table (no conditions allowed)
# ^ Syntax:
# *   TRUNCATE TABLE TableName;
# ~ Example:
# *   TRUNCATE TABLE Customers;
# * Removes all rows but keeps the table structure

# ? Key Differences
# ^ DELETE:
# *   - DML command
# *   - Can use WHERE to delete specific rows
# *   - Can be rolled back (before COMMIT)
# *   - Does not auto-commit
# *   - Physical memory freed only after COMMIT
# ^ TRUNCATE:
# *   - DDL command
# *   - Always deletes all rows (no WHERE allowed)
# *   - Auto-commits (cannot be rolled back)
# *   - Immediately frees physical memory

# ? COMMIT and ROLLBACK
# * COMMIT → permanently saves changes to physical memory
# * ROLLBACK → undo changes since last COMMIT
# * DELETE → changes can be rolled back until COMMIT
# * TRUNCATE → auto-committed, cannot be rolled back

# ? Summary
# * Use DELETE when you need selective row removal or rollback option
# * Use TRUNCATE when you want to quickly clear all data from a table

# *=============================================================================
#! Lec 04: SELECT Statement

# & SQL – SELECT Statement

# ? Definition
# * SELECT = command used to display/retrieve data from database tables
# * Most flexible DML command with many options (columns, conditions, joins, etc.)

# ? Basic Syntax
# * SELECT Column1, Column2, ...
# * FROM TableName
# * [WHERE condition];

# ? Example 1 – Select all columns
# ^ Requirement: Display all data of Department table
# *   SELECT *
# *   FROM Departments;
# * → Returns all rows and all columns

# ? Example 2 – Select specific columns
# ^ Requirement: Display SSN, FirstName, DeptNo of employees
# *   SELECT SSN, FirstName, DeptNo
# *   FROM Employees;
# * → Returns only the listed columns

# ? Example 3 – Select with condition (WHERE)
# ^ Requirement: Display data of department with a specific manager
# *   SELECT *
# *   FROM Departments
# *   WHERE ManagerSSN = 101;
# * → Returns only the department(s) managed by SSN = 101

# ? Notes
# * Column names with spaces must be enclosed in square brackets [Column Name]
# * SELECT * → shorthand for all columns
# * WHERE clause filters rows based on conditions
# * Without WHERE → all rows are returned
# * SELECT works on the result set level (retrieves data, does not modify it)


# *=============================================================================

#! Lec 05: Comparison & Logical operators

# & SQL – SELECT with Conditions and Operators

# ? Definition
# * SELECT can filter rows using conditions in the WHERE clause
# * Operators allow comparisons and logical combinations of conditions

# ? Example 1 – Simple condition
# TODO Requirement: Show all employees with salary > 1500
# *   SELECT *
# *   FROM Employees
# *   WHERE Salary > 1500;

# ? Example 2 – Multiple conditions with AND
# TODO Requirement: Show first name of employees with salary between 1500 and 2500
# *   SELECT FName
# *   FROM Employees
# *   WHERE Salary >= 1500 AND Salary <= 2500;
# ^ → AND = both conditions must be true

# ? Example 3 – Using BETWEEN
# TODO : Same requirement as Example 2, but shorter syntax
# *   SELECT FName
# *   FROM Employees
# *   WHERE Salary BETWEEN 1500 AND 2500;
# ^ → BETWEEN includes the boundary values (both 1500 and 2500 are inclusive)

# ? Example 4 – Multiple conditions with OR
# TODO Requirement: Show SSN and FName of employees supervised by supervisor 101 or 102
# *   SELECT SSN, FName
# *   FROM Employees
# *   WHERE SuperSSN = 101 OR SuperSSN = 102;
# ^ → OR = at least one condition must be true

# ? Example 5 – Using IN (multirow operator)
# TODO, Same requirement as Example 4, but shorter syntax
# *   SELECT SSN, FName
# *   FROM Employees
# *   WHERE SuperSSN IN (101, 102);
# ^ → IN replaces multiple OR conditions on the same column

# ? Operator Types
# * Single-row operators → =, >, <, >=, <= (compare with one value)
# * Multi-row operator → IN (compare with multiple values in a list)

# ? Key Notes
# * WHERE filters rows based on conditions
# * AND → all conditions must be true
# * OR → at least one condition must be true
# * BETWEEN → range check (inclusive)
# * IN → check against multiple values (simplifies OR)
# *=============================================================================

#! Lec 06: "like" operator


# & SQL – LIKE Operator and Pattern Matching

# ? Equal (=) Operator
# * Used for comparing exact values
# ^ Example:
# *   SELECT *
# *   FROM Employees
# *   WHERE FName = 'Ahmed';
# * → Works only when the exact spelling/value is known

# ? LIKE Operator
# * Used when the exact value is not known
# * Allows pattern matching in string comparisons
# ^ Syntax:
# *   SELECT *
# *   FROM TableName
# *   WHERE ColumnName LIKE 'pattern';

# ? Pattern Symbols
# * % (percent) → replaces zero or more characters
# * _ (underscore) → replaces exactly one character
# * (Some DBMSs may use * and ? instead, but standard SQL uses % and _)

# ? Example 1 – Second letter is 'O'
# TODO Requirement: Show employees whose second letter of first name = 'O'
# *   SELECT *
# *   FROM Employees
# *   WHERE FName LIKE '_o%';
# * → _ = first character (any), o = second character, % = rest of name

# ? Example 2 – Handling spelling variations
# TODO Requirement: Show employees named Ahmed/Ahmad (E or A in 4th position)
# *   SELECT *
# *   FROM Employees
# *   WHERE FName LIKE 'Ahm_d';
# * → _ replaces one character (matches both 'e' and 'a')

# ? Example 3 – Exact match vs LIKE
# *   WHERE FName = 'Ahmed'   → matches only exact spelling
# *   WHERE FName LIKE 'Ahm_d' → matches both Ahmed and Ahmad

# ? Key Notes
# * LIKE is used when exact value is unknown or flexible
# * % → wildcard for multiple characters
# * _ → wildcard for a single character
# * Useful for partial matches, patterns, or handling spelling variations

# *==================================================================================

#! Lec 07: Alias

# & SQL – Calculated Columns, Alias, and Concatenation

# ? Calculated Columns
# * SELECT can display values, doesn't edit directly in the database
# * Achieved by performing arithmetic operations on existing columns
# ^ Example: Bonus = 10% of Salary
# *   SELECT FName, Salary * 0.1 AS Bonus
# *   FROM Employees;
# * → Displays employee first name and calculated bonus

# ? Alias (AS Operator)
# * Used to rename a column or expression in the result set
# * Provides a readable header for calculated or concatenated columns
# * Syntax:
# *   Expression AS AliasName
# ^ Example:
# *   Salary * 0.1 AS Bonus
# * → Displays calculated column under the name "Bonus"
# * If alias contains spaces → enclose in square brackets [Alias Name]

# ? Arithmetic Operations in SELECT
# * Supported operations: +, -, *, /
# ^ Example: Annual Salary = Monthly Salary * 12
# *   SELECT FName, LName, Salary * 12 AS AnnualSalary
# *   FROM Employees
# *   WHERE Salary * 12 > 10000;

# ? Concatenation Operator
# * Used to combine values from multiple columns into one
# ^ Example: Full Name = First Name + ' ' + Last Name
# *   SELECT FName + ' ' + LName AS [Full Name]
# *   FROM Employees
# *   WHERE Salary * 12 > 10000;
# * → Displays full name in one column for employees with annual salary > 10000

# ? Key Notes
# * SELECT does not modify data; it only displays results
# * Alias improves readability of calculated/concatenated columns
# * Arithmetic operations allow dynamic calculations (bonus, annual salary, etc.)
# * Concatenation merges multiple columns into a single display column

# *=============================================================================================

#! Lec 08: Order By

# & SQL – ORDER BY Clause

# ? Purpose
# * Data in tables is not inherently organized.
# * ORDER BY is used to sort the result set in a specific order.
# * Sorting can be done on one or multiple columns.

# ? Basic Usage
# ^ Syntax:
# *   SELECT Column1, Column2, ...
# *   FROM TableName
# *   ORDER BY ColumnName [ASC|DESC];
# * Default order = ASC (ascending).

# ? Example 1 – Sort by one column
# ^ Requirement: Display FirstName and SSN of employees sorted by FirstName (ascending).
# *   SELECT FName, SSN
# *   FROM Employees
# *   ORDER BY FName ASC;
# * → ASC is optional since it’s the default.

# ? Example 2 – Sort in descending order
# ^ Requirement: Display FirstName and SSN sorted by FirstName descending.
# *   SELECT FName, SSN
# *   FROM Employees
# *   ORDER BY FName DESC;

# ? Example 3 – Multi-level sorting
# ^ Requirement: Display all employee data sorted by DeptNo ascending, then Salary descending.
# *   SELECT *
# *   FROM Employees
# *   ORDER BY DeptNo ASC, Salary DESC;
# * → First sorts by DeptNo (10, 20, 30…)
# * → Within each DeptNo, sorts salaries from highest to lowest.

# ? Key Notes
# * ORDER BY can handle multiple levels of sorting using commas.
# * Each column can have its own sort order (ASC or DESC).
# * Default = ASC if not specified.
# * Sorting affects only the result set, not the stored data.


# *=============================================================================================

#! Lec 09: DISTINCT

# & SQL – DISTINCT Clause

# ? Purpose
# * DISTINCT is used to remove duplicate rows from the result set.
# * It ensures that only unique combinations of values are displayed.
# * Works on the entire row returned, not just one column.

# ? Example 1 – Distinct Department Numbers
# ^ Requirement: Show department numbers of employees (avoid repetition).
# *   SELECT DISTINCT DeptNo
# *   FROM Employees;
# * → Returns each department number only once, even if multiple employees belong to it.

# ? Example 2 – Distinct Departments and Supervisors
# ^ Requirement: Show unique combinations of DeptNo and SupervisorSSN.
# *   SELECT DISTINCT DeptNo, SuperSSN
# *   FROM Employees;
# * → Returns each supervisor once per department (no duplicates).

# ? Key Notes
# * DISTINCT applies to the entire SELECT list (all columns chosen).
# * If multiple columns are listed, DISTINCT ensures uniqueness across the combination.

# * So, "Distinct" filters the repetition in the received result set,
#! not on one column level, but on the level of the whole combination received.

# * Without DISTINCT → duplicates appear in the result set.
# * DISTINCT is applied after WHERE filtering but before ORDER BY sorting.


# *=============================================================================================

#! Lec 10: INNER JOIN

# & SQL – JOINs (Combining Data from Multiple Tables)

# ? Purpose
# * JOIN is used to retrieve data from more than one table.
# * It links rows across tables using related columns (usually PK–FK relationships).
# * Number of JOIN conditions = Number of tables – 1.

# ? Example 1 – Department Manager (Employee + Department)
# * Requirement: Show Employee’s First Name and Department Name (manager).
# * Join Condition: Dept.ManagerSSN = Employee.SSN
# *   SELECT E.FName, D.DName
# *   FROM Employees E, Departments D
# *   WHERE D.ManagerSSN = E.SSN;
# * → Displays each department with its manager’s name.

# ? Example 2 – Employee’s Department
# * Requirement: Show Employee’s First Name and Department Name (where they work).
# * Join Condition: Employee.DeptNo = Department.DeptNo
# *   SELECT E.FName, D.DName
# *   FROM Employees E, Departments D
# *   WHERE E.DeptNo = D.DeptNo;
# * → Displays each employee with the department they belong to.
# * Note: If column names repeat, prefix with table name or alias (E.DeptNo, D.DeptNo).

# ? Aliases
# * Short names for tables to simplify queries.
# * Syntax: TableName AS Alias OR TableName Alias
# * Example: Employees E, Departments D

# ? Equi Join
# * Join condition uses the equality operator (=).
# * Typically written in WHERE clause.
# * Example: E.DeptNo = D.DeptNo

# ? Inner Join (ANSI Syntax)
# * Alternative to Equi Join, uses ON instead of WHERE.
# *   SELECT E.FName, D.DName
# *   FROM Employees E
# *   INNER JOIN Departments D
# *   ON E.DeptNo = D.DeptNo;
# * → Same result as Equi Join.

# ? Example 3 – Multi-table Join (Employee + Project + WorksFor)
# * Requirement: Show Employee Name, Project Name, and Hours worked.
# * Tables: Employees, Projects, WorksFor (M:N relationship table).
# * Join Conditions:
# *   Employees.SSN = WorksFor.ESSN
# *   Projects.PNumber = WorksFor.PNO
# *   SELECT E.FName, P.PName, W.Hours
# *   FROM Employees E
# *   INNER JOIN WorksFor W ON E.SSN = W.ESSN
# *   INNER JOIN Projects P ON P.PNumber = W.PNO;
# * → Displays each employee, the projects they work on, and hours worked.

# ? Key Notes
# * JOIN condition = PK–FK relationship.
# * For N tables → (N – 1) join conditions required.
# * Aliases make queries shorter and clearer.
# * INNER JOIN and Equi Join produce the same results (different syntax).
# * JOINs allow combining data across multiple tables into one result set.

# *=============================================================================================

#! Lec 11: OUTER JOIN (LEFT, RIGHT) & FULL JOIN

# & SQL – OUTER JOIN (LEFT, RIGHT, FULL)

# ? Definition
# * INNER JOIN / EQUI-JOIN → returns only matched records (rows with values in both tables).
# * OUTER JOIN → returns matched records + unmatched records from one or both tables.
# * Subtypes: LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN.

# ? LEFT OUTER JOIN
# * Returns all rows from the left table + matched rows from the right table.
# * If no match exists → NULLs are shown for right table columns.
# ^ Example:
# *   SELECT E.FName, D.DName
# *   FROM Employees E
# *   LEFT OUTER JOIN Departments D
# *   ON E.DeptNo = D.DeptNo;
# * → Displays all employees, with department names if available (NULL if not).

# ? RIGHT OUTER JOIN
# * Returns all rows from the right table + matched rows from the left table.
# * If no match exists → NULLs are shown for left table columns.
# ^ Example:
# *   SELECT E.FName, D.DName
# *   FROM Employees E
# *   RIGHT OUTER JOIN Departments D
# *   ON E.DeptNo = D.DeptNo;
# * → Displays all departments, with employee names if available (NULL if not).

# ? FULL OUTER JOIN
# * Returns all rows from both tables:
# *   - Matched rows (like INNER JOIN)
# *   - Unmatched rows from left table (with NULLs for right)
# *   - Unmatched rows from right table (with NULLs for left)
# ^ Example:
# *   SELECT E.FName, D.DName
# *   FROM Employees E
# *   FULL OUTER JOIN Departments D
# *   ON E.DeptNo = D.DeptNo;
# ~ → Displays:
# *   - Employees with departments
# *   - Employees without departments
# *   - Departments without employees

# ? Key Notes
# * LEFT → all rows from left table + matches from right.
# * RIGHT → all rows from right table + matches from left.
# * FULL → all rows from both tables, matched or not.
# * OUTER JOINs are useful when you want to preserve all data, even if no match exists.

# *=============================================================================================

#! Lec 12: SELF JOIN

# & SQL – SELF JOIN

# ? Definition
# * A Self Join = joining a table with itself.
# * Used when a table has a recursive relationship (e.g., Employee supervises other Employees).
# * Requires using table aliases to differentiate between the two instances of the same table.

# ? Example Scenario
# * Employee table contains:
# *   - SSN (Primary Key)
# *   - FName (Employee Name)
# *   - SuperSSN (Supervisor’s SSN → FK referencing Employee.SSN)
# * Requirement: Display each employee’s name with their supervisor’s name.

# ? SQL Implementation
# *   SELECT E.FName AS EmployeeName,
# *          S.FName AS SupervisorName
# *   FROM Employees E, Employees S
# *   WHERE E.SuperSSN = S.SSN;
# * → E = alias for Employee copy (employee data)
# * → S = alias for Supervisor copy (supervisor data)

# ? Explanation
# * The table is referenced twice:
# *   - First copy (E) → employee’s data
# *   - Second copy (S) → supervisor’s data
# * Join condition: E.SuperSSN = S.SSN
# * Result: Each employee is listed with the name of their supervisor.

# ? Key Notes
# * Self Join is essential for hierarchical/recursive relationships.
# * Always use aliases to avoid ambiguity (same column names in both copies).
# * Output can show pairs like:
# *   Employee: Ahmed → Supervisor: Moheb
# *   Employee: Moheb → Supervisor: Ahmed

# *=============================================================================================

#! Lec 13: SUB-QUERIES
# & SQL – SUBQUERIES (Nested Queries)

# ? Definition
# * A Subquery (Nested Query) = a query inside another query.
# * Used when the required value is not directly available, but can be retrieved from another query.
# * Subquery is written inside parentheses ().

# ? Example 1 – Salary greater than Ahmed Ali’s salary
# * Requirement: Show employees whose salary > Ahmed Ali’s salary.
# *   SELECT *
# *   FROM Employees
# *   WHERE Salary > (
# *       SELECT Salary
# *       FROM Employees
# *       WHERE FName = 'Ahmed' AND LName = 'Ali'
# *   );
# * → Subquery returns Ahmed Ali’s salary, main query compares against it.

# ? Single-Row Operators
# * =, >, <, >=, <=
# * Compare against one value only.
# * Example: Salary > (subquery returning one value)

# ? Example 2 – Salary greater than ALL employees in Dept 10
# * Requirement: Show employees whose salary > all salaries in DeptNo = 10.
# *   SELECT *
# *   FROM Employees
# *   WHERE Salary > ALL (
# *       SELECT Salary
# *       FROM Employees
# *       WHERE DeptNo = 10
# *   );
# * → ALL = compare against every value returned by subquery.
# * → Employee must have salary greater than the maximum salary in Dept 10.

# ? Example 3 – Salary greater than ANY employee in Dept 10
# * Requirement: Show employees whose salary > at least one salary in DeptNo = 10.
# *   SELECT *
# *   FROM Employees
# *   WHERE Salary > ANY (
# *       SELECT Salary
# *       FROM Employees
# *       WHERE DeptNo = 10
# *   );
# * → ANY = compare against at least one value returned by subquery.
# * → Employee must have salary greater than the minimum salary in Dept 10.

# ? Multi-Row Operators
# * IN → checks if value exists in a list of values
# * ALL → condition must be true for ALL values returned
# * ANY → condition must be true for AT LEAST one value returned

# ? Key Notes
# * Subqueries can return:
# *   - Single value (used with single-row operators)
# *   - Multiple values (used with IN, ALL, ANY)
# * ALL → stricter (compare with maximum/minimum depending on operator)
# * ANY → looser (compare with at least one value)
# * IN → shorthand for multiple OR conditions


# *=============================================================================================

#! Lec 14: Aggregate Functions (MAX, MIN, COUNT, SUM, AVG)


# ? Definition
# * Aggregate Functions = built-in SQL functions that perform calculations on a set of values.
# * Common functions: MAX, MIN, AVG, SUM, COUNT.
# * They return a single value as the result.
# * Null values are ignored in calculations.

# ? Example 1 – Maximum and Minimum Salary
# ^ Requirement: Display maximum and minimum salary in the company.
# *   SELECT MAX(Salary) AS MaxSalary,
# *          MIN(Salary) AS MinSalary
# *   FROM Employees;
# * → Returns highest and lowest salary values.

# ? Example 2 – Counting Employees vs Salaries
# ^ Requirement: Count total employees and count of salaries entered.
# *   SELECT COUNT(SSN) AS Employees,
# *          COUNT(Salary) AS Salaries
# *   FROM Employees;
# * → COUNT(SSN) = number of employees (12)
# * → COUNT(Salary) = number of non-null salaries (11)

# ? Example 3 – Average Salary
# ^ Requirement: Display average salary.
# *   SELECT AVG(Salary) AS AvgSalary
# *   FROM Employees;
# * → Calculates total of salaries ÷ number of non-null salaries (ignores missing values).

# ? Example 4 – Sum of Salaries
# ^ Requirement: Display total salaries paid.
# *   SELECT SUM(Salary) AS TotalSalaries
# *   FROM Employees;

# ? Key Notes
# * MAX → highest value
# * MIN → lowest value
# * COUNT → counts rows (ignores NULLs unless COUNT(*))
# * SUM → total of values
# * AVG → average of values
# * Aliases (AS) make results readable (e.g., AS MaxSalary).
# * Null values are excluded from aggregate calculations.

# *=============================================================================================

#! Lec 15: GROUP BY & HAVING

# & SQL – GROUP BY & HAVING

# ? Definition
# * GROUP BY → divides rows into groups based on one or more columns.
# * HAVING → applies conditions on groups (like WHERE, but for aggregated results).
# * Used together with aggregate functions (AVG, MAX, MIN, SUM, COUNT).

# ? Example 1 – Average Salary per Department
# * Requirement: Display average salary for each department.
# *   SELECT DeptNo, AVG(Salary) AS AvgSalary
# *   FROM Employees
# *   GROUP BY DeptNo;
# * → Groups employees by DeptNo, then calculates average salary for each group.

# ? Example 2 – Add Condition with HAVING
# * Requirement: Show average salary for each department, but only if MAX(Salary) > 1800.
# *   SELECT DeptNo, AVG(Salary) AS AvgSalary
# *   FROM Employees
# *   GROUP BY DeptNo
# *   HAVING MAX(Salary) > 1800;
# * → Filters groups: only departments with maximum salary > 1800 are displayed.

# ? Key Notes
# * WHERE → filters rows before grouping.
# * HAVING → filters groups after aggregation.
# * GROUP BY can use multiple columns (e.g., DeptNo, JobTitle).
# * Aggregate functions (AVG, MAX, MIN, SUM, COUNT) are often used with GROUP BY.
# * Without GROUP BY → aggregate functions apply to the entire table.


# *=============================================================================================

#! Lec 16: SELECT – Conclusion

# & SQL – Inclusive SELECT Example & Execution Sequence

# ? Requirement
# * Display Department Name and Maximum Salary for each department
# * Only include departments where Average Salary > 1200
# * Sort results by Department Name (ascending)

# ? SQL Statement
# *   SELECT D.DName, MAX(E.Salary) AS MaxSalary
# *   FROM Employees E
# *   INNER JOIN Departments D ON E.DeptNo = D.DeptNo
# *   GROUP BY D.DName
# *   HAVING AVG(E.Salary) > 1200
# *   ORDER BY D.DName ASC;

# ? Execution Sequence (Backend Order)
# * 1. FROM → Load tables into memory (Employees + Departments).
# * 2. WHERE → Apply row-level filters and JOIN conditions (E.DeptNo = D.DeptNo).
# * 3. GROUP BY → Divide rows into groups based on DName.
# * 4. Aggregate Functions → Calculate MAX(Salary), AVG(Salary) for each group.
# * 5. HAVING → Filter groups based on aggregate condition (AVG(Salary) > 1200).
# * 6. SELECT → Choose which columns/aggregates to display (DName, MAX(Salary)).
# * 7. ORDER BY → Sort final result set by DName (default ASC).

# ? Key Notes
# * GROUP BY creates "labels" (groups) → only grouped columns + aggregates are visible.
# * HAVING filters groups (WHERE filters rows).
# * Aliases (AS) make aggregate results readable (e.g., AS MaxSalary).
# * ORDER BY must use columns available in GROUP BY or SELECT.
# * Anything displayed in SELECT or used in ORDER BY must be part of GROUP BY when grouping is applied.

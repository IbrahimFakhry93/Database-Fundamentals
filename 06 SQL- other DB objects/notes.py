#
#! Lec 01: Views (create, modify, remove, types)

# & SQL – VIEWS

# ? Definition
# * A View = a database object that acts as a logical table.
# * Logical table → does not store data itself, only a stored SELECT query in the data dictionary (meta data)
# * Based on one or more base tables (or other views).
# * Acts like a "shortcut" or "window" to underlying data.

# ? Creation
# ^ Syntax:
# *   CREATE VIEW ViewName [(Column1, Column2, ...)] AS
# *   SELECT ...
# ~ SELECT here acts as subquery

# ^ Example:
# TODO : Create a view to display employee names and total hours employee worked on a project (display project name also)
# *   CREATE VIEW VW_Work_Hours AS
# *   SELECT E.FName, E.LName, P.PName, W.Hours
# *   FROM Employees E
# *   JOIN WorksOn W ON E.SSN = W.ESSN
# *   JOIN Projects P ON P.PNumber = W.PNO;

#! other syntax:
# *   CREATE VIEW VW_Work_Hours AS
# *   SELECT E.FName, E.LName, P.PName, W.Hours
# *   FROM Employees E, Projects P, WorksOn W
# *   Where E.SSN = W.ESSN
# *   AND P.PNumber = W.PNO;

# ^ note:
# * to get these info: E.FName, E.LName, P.PName, W.Hours
# * so we used three tables: Employees E, Projects P, WorksOn W
# * so if a user needs these info:  E.FName, E.LName, P.PName, W.Hours
# * he will need access to these three tables: Employees E, Projects P, WorksOn W
# * which it's not logical, what if I don't want the user to look up other employees salary
# * so we create customized view to restrict the shown data

# ? Usage
# ^ Query a View like a normal table (data base object):
# * SELECT fname,lname,hours FROM VW_Work_Hours
# ? or:
# * SELECT * FROM VW_Work_Hours;

# ? Create views WITH CHECK OPTION
# * Ensures DML operations on the View must satisfy its WHERE condition.
# ^ Example:
# *   CREATE VIEW Suppliers AS
# *   SELECT * FROM Supplier
# *   WHERE Status > 15
# *   WITH CHECK OPTION;
# ! → Prevents inserting/updating rows that don’t meet Status > 15.

# ? DML on Views
# * Views have no data of their own → DML is applied to base tables.
# * Simple Views (one table, no functions/grouping) → allow INSERT/UPDATE/DELETE.
# * Complex Views (joins, functions, grouping) → usually read-only.

# ? Modifying Views
# * CREATE OR REPLACE VIEW → updates definition if View already exists.
# * DROP VIEW ViewName → removes a View.

# ^ Example:
# TODO : Create a view to display employee names and total hours employee
# TODO : worked on a project (display project name also) but exclusively on employees in Department number 5
# *   CREATE OR REPLACE VIEW VW_Work_Hours AS
# *   SELECT E.FName, E.LName, P.PName, W.Hours
# *   FROM Employees E, Projects P, WorksOn W
# *   Where E.SSN = W.ESSN
# *   AND P.PNumber = W.PNO AND Dno =5

# ? Advantages
# * Restrict data access → limit what users can see/edit. (DBMS helps achieve security)
# * Simplify complex queries → save them as Views for reuse.
# * Provide data independence → hide sensitive columns (e.g., salaries). not necessary to display emp's salary while displaying its name,
# * Present different perspectives → same data shown differently for different roles.

# ? Types of Views
# * Simple View → based on one table, no functions/grouping, supports DML.
# * Complex View → based on multiple tables, may include functions/grouping, usually read-only.

# *====================================================

#! Lec 02: Indexes

# & SQL – INDEX

# ? Definition
# * Index = a database object that improves data retrieval speed.
# * Acts like a "phone book" → values are sorted with pointers to actual rows.
# * Logical structure maintained by DBMS, based on one or more columns.

# ? Advantage of using indexes:
# * They are used to speed up the retrieval of records in response to certain search conditions
# * May be defined on multiple columns
# * Can be created by the user or by the DBMS (DBMS usually create index for primary key)
# * They are used and maintained by the DBMS

# ? Why Use Indexes?
# ! Problem 1: Data is unsorted in tables.
# ! Problem 2: Data is scattered in physical memory (not contiguous).
# ^ Without index → DBMS performs a Full Table Scan (slow).
# * With index → DBMS searches ordered index, then jumps directly to rows.

# ? Example
# TODO Requirement: Frequently search Suppliers by Location.
# ^ Index created on Location column:
# *   CREATE INDEX idx_location
# *   ON Suppliers(Location);
# ^ → Index stores sorted Location values + pointers to row addresses.
# ~ Searching "London" → DBMS checks index, retrieves only matching rows.

# ? Advantages
# * Speeds up SELECT queries (especially with WHERE, JOIN, ORDER BY).
# * Reduces need for full table scans.
# * Useful for columns often used in search conditions or joins.
# * DBMS automatically creates index for Primary Keys.

# ? Disadvantages
# * Slows down DML (INSERT, UPDATE, DELETE).
# ! Reason: Data must be updated in both table and index. and also sorted in index table
# * More storage overhead (index is an extra object).

# ? Guidelines for Creating Indexes
# ^ Create index when:
# *   - Column is frequently used in WHERE or JOIN conditions.
# *   - Table is queried often for retrieval.
# *   - Column has many NULLs (index avoids scanning all rows).
# ! Avoid index when:
# *   - Table is updated frequently (high DML cost).
# *   - Column values are rarely used in search conditions.

# ? Syntax
# * Create Index:
# ^   CREATE INDEX idx_salary
# ^   ON Employees(Salary);
# * Drop Index:
# ^   DROP INDEX idx_salary;

# ? Key Notes
# * Index = faster SELECT, slower DML.
# * Can be created by user or automatically by DBMS (for PK).
# * Multiple indexes can exist on one table.
# * Index is invisible to end users → DBMS manages it internally.

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
# ^ Example:
# *   CREATE VIEW VW_Work_Hours AS
# *   SELECT E.FName, E.LName, P.PName, W.Hours
# *   FROM Employees E
# *   JOIN WorksOn W ON E.SSN = W.ESSN
# *   JOIN Projects P ON P.PNumber = W.PNO;

# ? Usage
# * Query a View like a normal table (data base object):
# *   SELECT * FROM VW_Work_Hours;

# ? WITH CHECK OPTION
# * Ensures DML operations on the View must satisfy its WHERE condition.
# ^ Example:
# *   CREATE VIEW Suppliers AS
# *   SELECT * FROM Supplier
# *   WHERE Status > 15
# *   WITH CHECK OPTION;
# * → Prevents inserting/updating rows that don’t meet Status > 15.

# ? DML on Views
# * Views have no data of their own → DML is applied to base tables.
# * Simple Views (one table, no functions/grouping) → allow INSERT/UPDATE/DELETE.
# * Complex Views (joins, functions, grouping) → usually read-only.

# ? Modifying Views
# * CREATE OR REPLACE VIEW → updates definition if View already exists.
# * DROP VIEW ViewName → removes a View.

# ? Advantages
# * Restrict data access → limit what users can see/edit.
# * Simplify complex queries → save them as Views for reuse.
# * Provide data independence → hide sensitive columns (e.g., salaries).
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

# ? Why Use Indexes?
# * Problem 1: Data is unsorted in tables.
# * Problem 2: Data is scattered in physical memory (not contiguous).
# * Without index → DBMS performs a Full Table Scan (slow).
# * With index → DBMS searches ordered index, then jumps directly to rows.

# ? Example
# * Requirement: Frequently search Suppliers by Location.
# * Index created on Location column:
# *   CREATE INDEX idx_location
# *   ON Suppliers(Location);
# * → Index stores sorted Location values + pointers to row addresses.
# * Searching "London" → DBMS checks index, retrieves only matching rows.

# ? Advantages
# * Speeds up SELECT queries (especially with WHERE, JOIN, ORDER BY).
# * Reduces need for full table scans.
# * Useful for columns often used in search conditions or joins.
# * DBMS automatically creates index for Primary Keys.

# ? Disadvantages
# * Slows down DML (INSERT, UPDATE, DELETE).
# * Reason: Data must be updated in both table and index.
# * More storage overhead (index is an extra object).

# ? Guidelines for Creating Indexes
# * Create index when:
# *   - Column is frequently used in WHERE or JOIN conditions.
# *   - Table is queried often for retrieval.
# *   - Column has many NULLs (index avoids scanning all rows).
# * Avoid index when:
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

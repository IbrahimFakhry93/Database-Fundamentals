#
# ~ Structured Query Language(SQL)

#! Lec 01 Database Schema & Constraints

# & Physical Design in Databases

# ? Definition
# * Physical Design = converting logical tables into actual DBMS structures using SQL.
# * SQL (Structured Query Language) = programming language for databases.
# ^ SQL Categories:
# *   - DDL (Data Definition Language) → create/alter/drop schema objects
# *   - DML (Data Manipulation Language) → insert/update/delete/select data
# *   - DCL (Data Control Language) → grant/revoke permissions

# ? Database Schema
# * Schema = group of related objects in a database (tables, views, indexes, etc.)
# * Belongs to one owner (creator).
# * Owner has full rights to structure and modify schema objects.

# ? Data Types (commonly supported)
# * Alphanumeric (CHAR, VARCHAR)
# * Numeric (INT, FLOAT, DECIMAL)
# * Date & Time (DATE, TIME, TIMESTAMP)
# * Others depending on DBMS

# ? Database Constraints
# * Constraints = rules to maintain data integrity.

# ^ Primary Key Constraint
# *   - Ensures uniqueness + not null
# *   - Each table must have one PK
# *   - Example: Employee(SSN as PK)

# ^ Not Null Constraint
# *   - Column must always have a value
# *   - Mandatory but not necessarily unique

# ^ Unique Constraint
# *   - Ensures values in a column are unique
# *   - Used for candidate keys not chosen as PK
# *   - Example: Employee(SSN unique, ID as PK)

# ^ Foreign Key (Referential Integrity Constraint)
# *   - FK = column in one table referencing PK in another
# *   - Parent record = table with PK
# *   - Child record = table with FK
# *   - Insert Rule: insert parent first, then child
# *   - Delete Rule: delete child first, then parent
# *   - Prevents orphan records
# *   - Example: Employee(DeptNo FK) → Department(DeptNo PK)

# ^ Check Constraint
# *   - Custom validation rule
# *   - Example: Salary BETWEEN 1000 AND 12000
# *   - Prevents invalid/typo values

# ? Summary
# * Physical Design = implement schema in DBMS using SQL
# * Entities → Tables
# * Attributes → Columns with proper data types
# * Constraints → enforce data integrity (PK, FK, Unique, Not Null, Check)
# * Referential Integrity ensures parent-child consistency

# *==========================================================================

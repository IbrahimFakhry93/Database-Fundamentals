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

#! Lec 02: Data Definition Language (DDL)

# & SQL – Data Definition Language (DDL)

# ? Definition
# * DDL = Data Definition Language
# * Commands responsible for the structure of database objects
# * Used to create, edit, or delete schema objects (not for manipulating data)

# ? Main DDL Commands
# * CREATE → create new database objects (tables, views, etc.)
# * ALTER → modify existing objects (add/remove columns, change structure)
# * DROP → delete database objects completely
# * TRUNCATE → remove all data from a table but keep its structure (discussed later)

# ? CREATE TABLE
# * Syntax:
# *   CREATE TABLE TableName (
# *       ColumnName DataType [Constraint],
# *       ColumnName DataType(Size) [Constraint],
# *       ...
# *   );
# * Example:
# *   CREATE TABLE Students (
# *       StudentID INT PRIMARY KEY,
# *       Name VARCHAR(50) NOT NULL,
# *       Country VARCHAR(30)
# *   );
# * → Creates table structure without data

# ? ALTER TABLE
# * Add a new column:
# *   ALTER TABLE Students ADD PostalCode VARCHAR(10);
# * → Adds PostalCode column to Students table
# * Remove a column:
# *   ALTER TABLE Students DROP COLUMN Country;
# * → Removes Country column from Students table

# ? DROP TABLE
# * Syntax:
# *   DROP TABLE Students;
# * → Deletes the Students table completely (structure + data)

# ? Key Notes
# * CREATE → build new table
# * ALTER → add/remove/modify columns
# * DROP → remove entire table
# * TRUNCATE → clears data but keeps table (covered next)

# *==========================================================================

#! Lec 03: Data Control Language (GRANT, REVOKE)

# & SQL – Data Control Language (DCL)

# ? Definition
# * DCL = Data Control Language
# * Commands used to control access and privileges on database objects
# * Two main commands: GRANT and REVOKE

# ? Types of Privileges
# * System Privileges → permissions on the database system level (e.g., create user, create tablespace)
# * Object Privileges → permissions on specific database objects (tables, views, etc.)

# ? GRANT Command
# * Used to give privileges to users
# ^ Syntax:
# *   GRANT privilege(s) ON object TO user [WITH GRANT OPTION];
# ^ Examples:
# ~   GRANT SELECT ON Employees TO Ahmed;
# *       → Ahmed can only view (SELECT) data from Employees table
# ~   GRANT ALL ON Department TO Mary, Ahmed;
# *       → Mary and Ahmed can SELECT, INSERT, UPDATE, DELETE on Department
# ~   GRANT SELECT ON Employees TO Ahmed WITH GRANT OPTION;
# *       → Ahmed can SELECT from Employees AND grant this privilege to other users

# ? REVOKE Command
# * Used to remove privileges from users
# ^ Syntax:
# *   REVOKE privilege(s) ON object FROM user;
# ^ Examples:
# ~   REVOKE UPDATE ON Department FROM Mary;
# *       → Removes UPDATE privilege on Department from Mary
# ~   REVOKE ALL ON Department FROM Mary, Ahmed;
# *       → Removes all DML privileges on Department from both users

# ? Key Notes
# * Only the schema owner (object owner) or DBA can grant privileges
# * WITH GRANT OPTION allows the user to pass privileges to others
# * REVOKE removes privileges but does not delete the user or the object

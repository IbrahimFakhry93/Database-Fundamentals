#

#! Lec 01: What is Normalization?

# & Database Normalization

# ? Definition
# * Normalization = process of applying a series of tests (Normal Forms) to:
# *   - Certify the goodness of a database design
# *   - Minimize redundancy (data repetition)
# *   - Avoid anomalies (Insert, Update, Delete problems)
# *   - Or redesign an existing database for better structure

# ? Why Normalization?
# * Reduces redundancy → avoids repeating the same data multiple times
# * Improves storage efficiency and database performance
# * Prevents anomalies (Insert, Update, Delete)
# * Reduces excessive NULL values

# ? Example – Poor Design
# * Tables: Employee_Department, Employee_Project
# ^ Issues:
# *   - Employee SSN repeated in multiple tables
# *   - Department name & manager number repeated for every employee in that department
# *   - Project name & location repeated for every employee working on that project

# ? Problems Caused
# ^ Redundancy:
# *   - Dept name & manager repeated 100 times if 100 employees in Dept 5
# *   - Project name & location repeated for each employee in project
# ^ Insert Anomaly:
# *   - Cannot insert a department without employees
# *   - Cannot insert a project without employees
# ^ Delete Anomaly:
# *   - Deleting last employee in a department → department data lost
# ^ Update Anomaly:
# *   - Changing Dept Manager → must update 100 rows instead of 1
# ^ Null Problem:
# *   - If manager is missing → 100 NULL values appear in column

# ? Benefits of Normalization
# * Avoids redundancy and anomalies (الشذوذ)
# * Ensures data consistency
# * Improves performance by reducing unnecessary repetition
# * Provides cleaner, more flexible design

# ? When to Use Normalization
# * To test the goodness of a new design
# * To redesign an old database or migrate from existing files


# *======================================================================

#! Lec 02: Functional Dependency

# & Functional Dependency (FD)

# ? Definition
# * A Functional Dependency is a constraint between two attributes (columns) or a group of attributes.
# * For every valid instance of A, the value of A uniquely determines the value of B.
# * Notation: A → B (B is functionally dependent on A).

# ? Examples
# * SSN → EName
# *   Each SSN determines exactly one employee name.
# * PNumber → PName, PLocation
# *   Each project number determines its project name and location.
# * (SSN, PNumber) → Hours
# *   Combination of employee SSN and project number determines hours worked.

# ? Types of Functional Dependency

# ^ 1. Full Functional Dependency
# *   - A non-key attribute depends on the whole key (not part of it).
# ~   - Example:
# *       SSN → EName, BirthDate, Address, DNumber
# *       (SSN, PNumber) → Hours
# *   - Hours depends on both SSN and PNumber together.

# ^ 2. Partial Functional Dependency
# *   - A non-key attribute depends on part of a composite key.
# ~   - Example:
# *       EName depends only on SSN (part of composite key).
# *       PName, PLocation depend only on PNumber.
# *   - Leads to redundancy and is removed in 2NF.

# ^ 3. Transitive Functional Dependency
# *   - A non-key attribute depends on another non-key attribute, which depends on a key.
# ~   - Example:
# *       SSN → DNumber → DName
# *       SSN → DNumber → ManagerSSN
# *   - DName and ManagerSSN are transitively dependent on SSN through DNumber.

# ? Key Notes
# * FD is the foundation of Normalization.
# * Full FD → good design.
# * Partial FD → redundancy, removed in 2NF.
# * Transitive FD → indirect dependency, removed in 3NF.

# *======================================================================

#! Lec 03: First Normal Form

# & Normalization – Introduction

# ? Definition
# * Normalization = process of decomposing unsatisfactory ("bad") relations into smaller,
# * well-structured relations.

# * Goal: minimize redundancy, avoid anomalies (Insert, Update, Delete), and improve design.

# * Normal Form = a condition (based on keys & functional dependencies)
# * that determines the quality of a relation.

# & First Normal Form (1NF)

# ? Rule
# ~ A relation is in 1NF if:
# *   - No multivalued attributes
# *   - No repeating groups
# *   - No composite attributes
# * Each attribute must hold atomic (indivisible) values.

# ? Example – School Data (Excel Sheet)
# * Primary Key: StudentID
#! Problems:
# *   - Telephone column contains multiple values → multivalued attribute
# *   - Subject, SubjectDescription, Grade each have multiple values per StudentID → multivalued attributes
# *   - Subject + SubjectDescription + Grade are related → form a repeating group

# ? Solution – Decompose into Separate Tables
# ^ 1. Main Student Table:
# *      StudentID, Name, Address, ...
# ^ 2. Student Telephone Table:
# *      StudentID (FK), Telephone
# *      Composite PK = (StudentID, Telephone)
# ^ 3. Student Subjects Table:
# *      StudentID (FK), Subject, SubjectDescription, Grade
# *      Composite PK = (StudentID, Subject)

# ? Result
# * Data is now atomic (no multivalued attributes).
# * Repeating groups are eliminated.
# * Relation is in First Normal Form (1NF).


# *======================================================================

#! Lec 04: Second Normal Form

# & Second Normal Form (2NF)

# ? Definition
# ^ A relation is in 2NF if:
# *   1. It is already in 1NF
# *   2. It has no Partial Dependency
# *      → No non-key attribute should depend on part of a composite key.

# ? Key Concept
# * Partial Dependency = when a non-key attribute depends only on part of a composite primary key.
# * Normal Forms are sequential → must satisfy 1NF before 2NF.

# ? Example – From 1NF Relations
# * Table: (StudentID, Subject) → Composite Primary Key
# * Non-key attributes: SubjectDescription, Grade

# ^ Check dependencies:
# *   - SubjectDescription depends only on Subject → Partial Dependency ❌
# *   - Grade depends on (StudentID, Subject) together → Full Dependency ✅

# ? Solution – Decomposition
# ~ Break the table into smaller relations:
# ^   1. Subject Table:
# *        Subject (PK), SubjectDescription
# ^   2. Student_Grades Table:
# *        StudentID (FK), Subject (FK), Grade
# *        Composite PK = (StudentID, Subject)

# ? Why Keep Foreign Keys?
# * To maintain relationships between decomposed tables.
# * Ensures data integrity and avoids losing connections.

# ? Result
# * All non-key attributes are fully dependent on the whole key.
# * Partial dependencies removed.
# * Relation is now in Second Normal Form (2NF).


# *======================================================================

#! Lec 05: Third Normal Form
# & Third Normal Form (3NF)

# ? Definition
# * A relation is in 3NF if:
# *   1. It is already in 2NF
# *   2. It has no Transitive Dependency
# * Transitive Dependency = a non-key attribute depends on another non-key attribute, which depends on the key.

# ? Example – From 2NF Relations
# * Table: Student(StudentID, Name, Location, Level, LevelManager)
# ^ Dependencies:
# *   - Name → depends on StudentID (OK)
# *   - Location → depends on StudentID (OK)
# *   - Level → depends on StudentID (OK)
# *   - LevelManager → depends on Level, and Level depends on StudentID → Transitive Dependency ❌

# ? Solution – Decomposition
# * Break transitive dependency into a new table:
# ^   1. Student Table:
# *        StudentID (PK), Name, Location, Level (FK)
# ^   2. Level Table:
# *        Level (PK), LevelManager
# * → Level remains in Student table as FK to preserve relationship.

# ? Result
# * All non-key attributes depend directly on the key.
# * No non-key depends on another non-key.
# * Relation is now in Third Normal Form (3NF).

# & Recap of Normal Forms

# ? First Normal Form (1NF)
# * No multivalued attributes
# * No repeating groups
# * No composite attributes
# * Solution: move multivalued/repeating groups into separate tables with PK as FK.

# ? Second Normal Form (2NF)
# * Must already be in 1NF
# * No Partial Dependency (non-key attribute depending on part of a composite key)
# * Solution: move partial dependency into a separate table, keep FK for relationship.

# ? Third Normal Form (3NF)
# * Must already be in 2NF
# * No Transitive Dependency (non-key → non-key → key)
# ~ Solution:
# * move transitive dependency into a separate table, keep FK for relationship.

# ? Higher Normal Forms
# * 4NF, 5NF, … exist but usually not applied in practice unless required.
# * More normalization = more tables, which may affect performance.
# * Often recommended to stop at 3NF depending on business needs.


# *======================================================================

#! Lec 06: Summary - example

# & Normalization Example – ITI Student Sheet

# ? Zero Normal Form (0NF)
# * All data stored in one big table (StudentNumber as PK).
#! Problems:
# *   - Composite attribute: Address (Street + City)
# *   - Multivalued attribute: Telephone (multiple numbers per student)
# *   - Repeating group: DepartmentName, DeptDescription, AdmissionGrade, Comments

# ? First Normal Form (1NF)
# ~ Rule: No composite, no multivalued, no repeating groups.
# ^ Fixes:
# *   - Split Address → Street, City
# *   - Move Telephone → new table (StudentID + Telephone as composite PK)
# *   - Move Department data → new table (StudentID + DeptName as composite PK)
# ^ Resulting Tables:
# *   1. Student(StudentID, Name, Street, City, FacultyCode, Faculty, Major)
# *   2. StudentPhone(StudentID, Telephone)   → PK = (StudentID, Telephone)
# *   3. StudentDept(StudentID, DeptName, DeptDescription, AdmissionGrade, Comments)
# *        → PK = (StudentID, DeptName)

# ? Second Normal Form (2NF)
# ~ Rule: Must be in 1NF + no Partial Dependency.
# * Check composite keys:
# *   - StudentDept table → PK = (StudentID, DeptName)
# *   - DeptDescription depends only on DeptName → Partial Dependency ❌
# *   - AdmissionGrade, Comments depend on (StudentID, DeptName) → Full Dependency ✅
# ^ Fix:
# *   - Create Department(DeptName, DeptDescription) → PK = DeptName
# *   - Keep StudentDept(StudentID, DeptName, AdmissionGrade, Comments)
# * Result: Partial dependency removed.

# ? Third Normal Form (3NF)
# ~ Rule: Must be in 2NF + no Transitive Dependency.
# ^ Check:
# *   - Faculty depends on FacultyCode
# *   - FacultyCode depends on StudentID
# *   → Transitive Dependency ❌
# ^ Fix:
# *   - Create Faculty(FacultyCode, FacultyName, Major)
# *   - Student table keeps FacultyCode as FK
# * Result: All non-key attributes depend directly on the key.

# ? Final Tables in 3NF
# * Student(StudentID, Name, Street, City, FacultyCode)
# * StudentPhone(StudentID, Telephone)
# * StudentDept(StudentID, DeptName, AdmissionGrade, Comments)
# * Department(DeptName, DeptDescription)
# * Faculty(FacultyCode, FacultyName, Major)

# ? Key Notes
# * 0NF → raw data, unstructured
# * 1NF → remove composite, multivalued, repeating groups
# * 2NF → remove partial dependencies
# * 3NF → remove transitive dependencies
# * Normalization improves design, reduces redundancy, avoids anomalies

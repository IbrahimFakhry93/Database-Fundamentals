#
#! Lec 01: Mapping of strong (regular) and weak entities

# & Converting Conceptual Design (ERD) into Logical Design (Relations == DB tables)

# ? Relational Database Basics
# * A relation = a table consisting of:
# *   - Tuples (rows/records)
# *   - Columns (attributes)
# * Domain = intersection of a column and a tuple (single value only)
# ^ Primary Key = column(s) with:
# *   - Unique values (no duplicates)
# *   - Not Null (cannot be empty)

# ? Rule 1: Each Entity → Table
# ^ Example: Employee entity → Employee table
# * Columns = attributes of the entity

# ? Mapping Attributes
# * Simple/Single Attributes → separate columns (e.g., ID, SSN, Salary, Name, DOB)
# * Composite Attributes → split into subparts (e.g., Address → Street, Zone)
# * Multi-Valued Attributes → moved to a separate table
# * Derived Attributes → usually not stored, (calculated when needed)

# ? Choosing Primary Key
# * Select shortest unique attribute(s): less storage
# * Prefer numeric over text for efficiency
# * Example: Employee → choose SSN as Primary Key

# ? Handling Multi-Valued Attributes
# ! Problem: Domain allows only one value per cell
# ~ Solution: Create a new table for the multi-valued attribute
# ^ Example: Employee Phone table
# *   - Columns: SSN (FK), Phone
# *   - Composite Primary Key = (SSN, Phone)
# *   - SSN is a Foreign Key referencing Employee table
# *   - Ensures phone numbers linked to valid employees

# ? Handling Derived Attributes
# * Default: Do NOT store (calculated on demand)
# ^ Reason: Storing slows performance (recalculation needed on updates)
# ! Exception: Store only if frequently queried or used in reporting
# * Example: Age derived from DOB (Date of Birth)

# ? Mapping Other Entities
# * Department → Table(DeptNo [PK], DeptName, Location)
# * Project → Table(ProjectNo [PK], ProjectName)
# * Car → Table(PlateNo [PK], Model, Color)
# * Contract → Table(ContractID [PK], Type, StartDate)
# * Skill → Table(SkillID [PK], SkillName)

# ? Mapping Weak Entities
# ^  Example: Dependent (weak entity)
# *   - Includes attributes: Name, Relation
# *   - Must include owner’s PK (Employee SSN) as FK
# *   - Composite Primary Key = (SSN, Name)
# *   - Ensures uniqueness and dependency on Employee

# ? Summary of Steps
# * Step 1: Map strong entities → tables with PKs
# * Step 2: Handle multi-valued attributes → separate tables
# * Step 3: Handle derived attributes → usually exclude
# * Step 4: Map weak entities → include owner’s PK as FK + composite PK
# * Step 5: Verify all entities mapped into relations


# *======================================================================

#! Lec 02: Mapping Relationship Types

# & Mapping Relationships from Conceptual to Logical Design

# ? One-to-Many Relationships (Binary or Unary)
# ^ Rule: Add the primary key of the "One" side as a foreign key in the "Many" side.

# ~ Example (Binary): Department (1) → Employee (M)
# *   - DepartmentNo (PK) added as FK in Employee table.
# ~ Reason:
# *  Each employee belongs to one department, but a department has many employees.
# ! If reversed, would require multiple employee IDs in one department row → violates domain rule.

# ~ Unary (Recursive) One-to-Many
# ^ Example: Employee supervises Employee
# *   - Add Employee (Supervisor) SSN (PK) as FK in the same Employee table.
# *   - Rename FK to avoid confusion (e.g., SupervisorSSN).
# ~   - No redundancy: FK represents supervisor relationship, not duplicate data.

# ? One-to-Many with Weak Entity
# ^ Example: Employee (1) → Dependent (M)
# *   - Employee SSN (PK) already added as FK in Dependent table.
# !   - Mapping weak entity automatically maps identifying relationship.

# ? Many-to-Many Relationships
# ^ Rule: Create a new table with PKs of both entities as FKs.

# ~ Example: Employee ↔ Project
# *   - New table: WorkOn(EmployeeSSN [FK], ProjectNo [FK])
# *   - Composite PK = (EmployeeSSN, ProjectNo)
# ~ Relationship Attributes:
# * Relation Attribute always follows the pre-added foreign keys (which are in this case: PK of EmployeeSSN and ProjectNo)
# TODO   - Example: Hours (attribute of WorkOn relationship).
# *  Add them to the new relationship table (workOn table).


# ? One-to-One Relationships
# ^ Case 1: May–Must
# ~  - Rule: Add PK of "May" side as FK in "Must" side.
# &   - Example: Manage (Employee–Department)
# *       • Employee SSN (PK) added as FK in Department table.
# *       • Rename FK → ManagerSSN.
# *       • Relationship attribute (StartDate) also added to Department table.

# ^ Case 2: May–May
# ~   - Rule: Three options:
# *       1. Add PK of Car as FK in Employee
# *       2. Add PK of Employee as FK in Car
# *       3. Create new table (own) with both PKs as FKs
# &   - Example: Own (Employee–Car)
# !       • Recommended: Add Car PlateNo (PK) as FK in Employee.

# ^ Case 3: Must–Must
# ~   - Rule: Merge both tables into one.
# ?   - Example: Has (Employee–Contract)
# *       • Merge Contract into Employee table.
# *       • Keep SSN as PK (equivalent to ContractID).
# *       • If Contract referenced elsewhere, use SSN as FK. (watch video 5:40)

# ? Ternary Relationships
# ~ Rule: Always create a new table with PKs of all participating entities as FKs.
# ^ Example: Employee–Project–Skill
# *   - New table: SkillsUsed(EmployeeSSN [FK], ProjectNo [FK], SkillID [FK])
# *   - Composite PK = (EmployeeSSN, ProjectNo, SkillID)
# *   - Relationship attributes (if any) also added here.

# ? Summary
# * One-to-Many → FK on "Many" side
# * Many-to-Many → New table with composite PK
# * One-to-One → Depends on participation (May–Must, May–May, Must–Must)
# * Ternary → Always new table with all PKs as FKs
# * Relationship attributes → Always follow the FK location

# *===============================================================================================

#! Conclusion:
# &  Rules for Mapping Conceptual Design → Logical Design

# ? Step 1: Mapping Entities
# * Each entity → separate table
# * Attributes → columns of the table

# ? Attribute Types
# * Single/Simple Attribute → normal column
# * Multi-Valued Attribute → separate table + PK of entity as FK
# * Derived Attribute → not stored (calculated when needed)
# * Composite Attribute → split into subparts, each as a column
# * Weak Entity → include PK of owner entity as FK, combine with own attribute(s) to form composite PK

# ? Step 2: Mapping Relationships
# * One-to-Many (Binary/Unary) → PK of "One" side becomes FK in "Many" side
# * Many-to-Many → create new table with PKs of both entities as FKs
# ^ One-to-One:
# *   - May–Must → PK of "May" side becomes FK in "Must" side
# *   - May–May → PK of either side can be FK in the other
# *   - Must–Must → merge both tables into one
# * Ternary Relationship → create new table with PKs of all participating entities as FKs

# ? Step 3: Relationship Attributes
# * Relationship attributes always follow the foreign key
# ^ Example:
# *   - "Hours" → added to WorkOn table (Employee–Project M:N)
# *   - "StartDate" → added to Department table with ManagerSSN (Employee–Department 1:1)

# ? Key Takeaway
# * Entities → Tables
# * Attributes → Columns (with special handling for multi-valued, composite, derived)
# * Relationships → handled based on cardinality & participation
# * Relationship attributes → stored with the foreign key location

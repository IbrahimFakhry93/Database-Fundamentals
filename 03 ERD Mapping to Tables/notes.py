#
#! Mapping of strong (regular) and weak entities

# & Converting Conceptual Design (ERD) into Logical Design (Relations)

# ? Relational Database Basics
# * A relation = a table consisting of:
# *   - Tuples (rows/records)
# *   - Columns (attributes)
# * Domain = intersection of a column and a tuple (single value only)
# ^ Primary Key = column(s) with:
# *   - Unique values (no duplicates)
# *   - Not Null (cannot be empty)

# ? Rule 1: Each Entity → Table
# * Example: Employee entity → Employee table
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
# * Solution: Create a new table for the multi-valued attribute
# ^ Example: Employee Phone table
# *   - Columns: SSN (FK), Phone
# *   - Composite Primary Key = (SSN, Phone)
# *   - SSN is a Foreign Key referencing Employee table
# *   - Ensures phone numbers linked to valid employees

# ? Handling Derived Attributes
# * Default: Do NOT store (calculated on demand)
# * Reason: Storing slows performance (recalculation needed on updates)
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
# *   - Composite Primary Key = (SSN, Name) or (SSN, Name, Relation)
# *   - Ensures uniqueness and dependency on Employee

# ? Summary of Steps
# * Step 1: Map strong entities → tables with PKs
# * Step 2: Handle multi-valued attributes → separate tables
# * Step 3: Handle derived attributes → usually exclude
# * Step 4: Map weak entities → include owner’s PK as FK + composite PK
# * Step 5: Verify all entities mapped into relations


# *======================================================================

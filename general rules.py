#

# & Blueprint for Cardinality Analysis

# ? Step 1 – Identify Entities
# * Choose two (or more) entities that interact (e.g., Employee–Department, Employee–Project).

# ? Step 2 – Ask Cardinality Questions
# * For Entity A:
# *   - Can one instance of A relate to only one instance of B, or to many?
# *   - Answer → "1" (one) or "M" (many).
# * For Entity B:
# *   - Can one instance of B relate to only one instance of A, or to many?
# *   - Answer → "1" or "M".

# ? Step 3 – Assign Cardinality Ratio
# * Combine answers into a ratio:
# *   - 1 : 1 → One-to-One
# *   - 1 : M → One-to-Many
# *   - M : N → Many-to-Many
# * For recursive (unary) relationships, apply the same logic (e.g., Employee supervises Employee).

# ? Step 4 – Ternary or Higher Relationships
# * Treat as three (or more) binary relationships first.
# * Then ask combined questions involving all entities:
# *   - Can A relate to many B’s in the context of C?
# *   - Can B relate to many C’s in the context of A?
# *   - Can C relate to many A’s in the context of B?
# * Assign "1" or "M" for each side.
# * If inconsistent (e.g., 1–M–M), consider redesigning into binary relationships.

# ? Step 5 – Validate with Business Rules
# * Always tie the ratio back to real-world rules:
# *   - "Each employee works in only one department" → 1
# *   - "Each department has many employees" → M
# *   - "Each employee can work on many projects, and each project has many employees" → M:N

# ? Step 6 – Document Clearly
# * Record the ratio (e.g., Employee–Department (Work) = 1:M).
# * Use ERD notation (crow’s foot, etc.) to visualize.

# ? Quick Examples
# * Employee–Department (Work) → 1:M
# * Employee–Department (Manage) → 1:1
# * Employee–Project (Work On) → M:N
# * Employee–Employee (Supervise) → 1:M (recursive)
# * Employee–Dependent (Has) → 1:M
# * Employee–Car (Own) → 1:1
# * Employee–Contract (Has) → 1:1
# * Employee–Project–Skill (ternary) → M:M:M


# & Blueprint for Participation & Relationship Analysis

# ? Step 1 – Identify Entities
# * List the main entities in the domain (e.g., Employee, Department, Project, Contract).
# * For each entity, ask: what other entities does it interact with?

# ? Step 2 – Define Relationship
# * Name the relationship (e.g., "Works In", "Manages", "Owns", "Has").
# * Clarify the business meaning of the relationship.

# ? Step 3 – Ask Participation Questions (Minimum)
# * For Entity A:
# *   - Must every instance of A participate in this relationship?
# *   - Or can some instances of A exist without participating?
# *   - If "must" → Mandatory (double line). If "may" → Optional (single line).
# * For Entity B:
# *   - Must every instance of B participate in this relationship?
# *   - Or can some instances of B exist without participating?
# *   - Again, decide "Must" vs "May".

# ? Step 4 – Ask Cardinality Questions (Maximum)
# * For Entity A:
# *   - With how many instances of B can one A be associated? (1, many, etc.)
# * For Entity B:
# *   - With how many instances of A can one B be associated?
# * → This defines 1:1, 1:N, or M:N.

# ? Step 5 – Check for Weak Entities
# * Is one entity dependent on another for identification?
# * If yes → it’s a weak entity, and its participation in the relationship is always "Must".
# * Represent with double diamond.

# ? Step 6 – Attributes on Relationships
# * Ask: does the relationship itself have attributes?
# * Examples:
# *   - "Start Date" of Manage (Employee–Department).
# *   - "Hours" of Work On (Employee–Project).
# * If yes → attach attributes to the relationship, not the entities.

# ? Step 7 – Ternary or Higher Relationships
# * If relationship involves 3+ entities, ask participation questions for each:
# *   - Must Entity A always appear with B and C?
# *   - Must Entity B always appear with A and C?
# *   - Must Entity C always appear with A and B?
# * Decide "Must" vs "May" for each side.

# ? Step 8 – Validate Against Business Rules
# * Always tie participation and cardinality back to real business rules.
# * Example: "Every contract must belong to an employee" → Must.
# * Example: "A project may exist without employees (tender stage)" → May.

# ? Step 9 – Document Clearly
# * Record participation (Must/May) and cardinality (1, many).
# * Use ERD notation: single vs double lines, crow’s foot, etc.


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
# * Many-to-Many → create new junction table with PKs of both entities as FKs
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

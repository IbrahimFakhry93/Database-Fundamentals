#!
# & Entity-Relationship (ER) Modeling

# ? Definition
# * ER modeling (Entity-Relationship Diagram) is a way to create the conceptual design of a database.
# * It identifies customer requirements and represents them as entities and relationships.

# ? Entity
# * An entity = any stand-alone object or thing in the system.
# * Described by a set of characteristics or attributes.
# ^ Examples:
# *   - Bank: Client entity with attributes (Name, Account Number, ID, Address, Phone).
# *   - ITI: Student entity with attributes (Name, Graduation Year, Faculty, Grades).
# *   - Subject entity with attributes (Code, Number of Hours, Prerequisites).
# ^ Note:
# * A supermarket customer is not an entity if no data is stored about them.

# ? Attributes
# * Characteristics that describe an entity.
# * Must include at least one unique identifier (Primary Key).
# * Example: Student → ID (unique, non-duplicated).

# ? Relationships
# * Define how entities are connected to each other.
# ^ Example: Student "studies" Subject.
# ~ Relationship answers:
# *   - How many subjects does a student study?
# *   - Can a student study one or multiple subjects?

# ? Guidelines for Building ERD
# * 1. Identify entities from requirements.
# * 2. Define attributes for each entity.
# * 3. Ensure each entity has a unique identifier (Primary Key).
# * 4. Define relationships between entities (no isolated entities).
# * 5. Represent entities, attributes, and relationships in the ER diagram.

# ? Key Point
# * Database = group of related data.
# * ERD ensures entities are connected logically through relationships.

# *==================================================================================

#! Lec 02: Entities & Attributes

# & Conceptual Design – Entities, Attributes, and Keys

# ? Example Scenario
# * Company with multiple departments and projects
# * Need to store data about employees, departments, projects, and related entities

# ? Entity: Employee
# ^ Attributes:
# *   - ID (unique, candidate key)
# *   - SSN (unique, candidate key)
# *   - Name
# *   - Email
# *   - Salary (simple attribute)
# *   - Phone (multi-valued attribute → can store multiple numbers)
# *   - Address (composite attribute → Street, Zone)
# *   - Date of Birth (DOB)
# *   - Age (derived attribute → calculated from DOB + current date)

# ? Entity: Department
# ^ Attributes:
# *   - Department Number (unique identifier)
# *   - Department Name
# *   - Location

# ? Entity: Project
# ^ Attributes:
# *   - Project Number (unique identifier)
# *   - Project Name

# ? Entity: Dependent
# ^ Attributes:
# *   - Name
# *   - Relation
# ~ Notes:
# *   - Neither Name nor Relation is unique
# *   - No unique identifier → Weak Entity
# *   - Existence depends on Employee entity
# *   - Represented with double rectangle in ERD

# ? Entity: Car
# ^ Attributes:
# *   - Plate Number
# *   - Model
# *   - Color

# ? Entity: Contract
# ^ Attributes:
# *   - Contract ID
# *   - Type
# *   - Start Date

# ? Entity: Skill
# ^ Attributes:
# *   - Skill ID
# *   - Skill Name

# ? Attribute Types Recap
# * Simple Attribute → single value (e.g., ID, SSN, Salary)
# * Multi-Valued Attribute → multiple values (e.g., Phone)
# * Composite Attribute → divided into subparts (e.g., Address → Street, Zone)
# * Derived Attribute → calculated from other attributes (e.g., Age from DOB)

# ? Keys
# * Candidate Key → attribute(s) that can uniquely identify an entity
# ~ Example:
# *   - Employee: ID, SSN
# *   - Department: Department Number
# *   - Project: Project Number
# * Weak Entity → no unique identifier, depends on another entity (e.g., Dependent)


# *================================================================================================

#! Lec 03: Relationship - degree

# & Defining Relationships Between Entities

# ? Relationship Basics
# * Relationships connect data of different entities.
# ^ Each relationship must define:
# *   1. Degree of Relationship → number of entities involved
# *   2. Cardinality Ratio → how many instances of one entity relate to another
# *   3. Participation → whether all or some entity instances participate

# ? Relationship Notation
# * Represented by a diamond shape in ERD.
# * Relationship names are expressed as verbs (e.g., Work, Manage, Has, Own).

# ? Binary Relationships (2 entities)
# * Example: Employee "works in" Department
# * Example: Employee "manages" Department
# * Example: Employee "has" Dependent
# * Example: Employee "works on" Project
# * Example: Employee "owns" Car
# * Example: Employee "has" Contract

# ? Unary / Recursive Relationships (Entity with itself)
# ^ Example: Employee "supervises" Employee
# * Relationship connects the same entity from both sides.

# ? Ternary Relationships (3 entities)
# * Example: Employee, Project, Skill
# * Relationship: "Skilled Use"
# ^ Meaning: An employee joins a project based on a specific skill.

# ? Degree of Relationship
# * Binary → involves 2 entities (most common)
# * Unary (Recursive) → involves 1 entity related to itself
# * Ternary → involves 3 entities

# *=========================================================================================

#! Lec 04: Relationship - Cardinality ratio


# & Cardinality Ratios in Relationships

# ? Definition
# * Cardinality ratio = maximum number of relationships an entity instance can participate in.
# * Expressed as: 1 (one) or M (many).

# ? Employee – Department (Work)
# * Question: Can an employee work in one or more departments?
# * Rule: Employee works in only one department → "1"
# * Department has many employees → "M"
# ! Cardinality: 1 : M (One-to-Many)

# ? Employee – Department (Manage)
# * Rule: One employee manages one department → "1"
# * One department managed by one employee → "1"
# ! Cardinality: 1 : 1 (One-to-One)

# ? Employee – Project (Work On)
# * Rule: Employee can work on many projects → "M"
# * Project has many employees → "M"
# ! Cardinality: M : N (Many-to-Many)

# ? Employee – Employee (Supervise) [Unary/Recursive]
# * Rule: One employee can supervise many employees → "M"
# * Each employee supervised by only one supervisor → "1"
# ! Cardinality: 1 : M (One-to-Many, recursive)

# ? Employee – Dependent (Has)
# * Rule: Employee can have many dependents → "M"
# * Each dependent belongs to only one employee → "1"
# ! Cardinality: 1 : M (One-to-Many)

# ? Employee – Car (Own)
# * Rule: Each employee owns one car → "1"
# * Each car owned by one employee → "1"
# ! Cardinality: 1 : 1 (One-to-One)

# ? Employee – Contract (Has)
# * Rule: Each employee has one contract → "1"
# * Each contract belongs to one employee → "1"
# ! Cardinality: 1 : 1 (One-to-One)

# ? Ternary Relationship (Employee – Project – Skill)
# * we study it as three binary relation ships, every two we study them separately
# ~ Rule:
# *   - Employee can use many skills → "M"
# *   - Skill can be used by many employees → "M"
# *   - Skill can be used in many projects → "M"
# *   - Project can use many skills → "M"
# ! Cardinality: M : M : M (Many-to-Many-to-Many)
# ^ Note:
# *        If ternary has inconsistent ratios (e.g., "1" on one side, "M" on another),
# *       redesign into 3 binary relationships.

# ? Key Ratios
# * One-to-One (1:1)
# * One-to-Many (1:M)
# * Many-to-Many (M:N)
# * Many-to-Many-to-Many (ternary)


# & Ternary Relationships – Cardinality, consistency, and modeling implications

# ? Definition and context
# * A ternary relationship involves THREE entities simultaneously (e.g., Employee–Project–Skill).
# * Cardinality in ternary means the MAXIMUM participation per entity, considering the other two together.
# * Practical modeling often starts by “thinking in pairs,” but true constraints are 3-way, not just binary.

# & Example: Employee–Project–Skill (meaning: an employee joins a project using a specific skill)

# ? Pairwise reasoning (to build intuition)
# * Employee–Project: An employee can work on MANY projects; a project has MANY employees → M : M
# * Employee–Skill: An employee has MANY skills; a skill can belong to MANY employees → M : M
# * Skill–Project: A skill can be used in MANY projects; a project uses MANY skills → M : M
# * Conclusion (pairwise): All sides suggest “Many” → candidate ternary = M : M : M

# & Ternary cardinality consistency rule
# ? Consistency requirement
# * The cardinality on each branch (for each entity) should be compatible.
# * If one side is “1” while the others are “M”, the ternary often becomes ambiguous or incorrect.

# ? What to do when inconsistent
# * If you get a mix like 1 on one side and M on others, REFACTOR the model:
# * Convert the ternary into THREE BINARY relationships (with an associative entity) to capture constraints precisely.

# & Deep insight: Ternary constraints are 3-way, not just pairwise
# ? Why pairwise is insufficient
# * Even if all pairwise are M : M, the true constraint might say: for a GIVEN (Employee, Project) there is ONE Skill.
# * This cannot be fully enforced with three separate binaries unless you introduce a composite uniqueness (associative entity).

# ? Proper modeling pattern (associative entity)
# * Create an associative entity, e.g., Assignment(Employee, Project, Skill, StartDate, Role, …).
# * Keys/constraints:
# *   - Composite key could be (Employee, Project, Skill) for M:M:M.
# *   - If business rule says “one skill per (Employee, Project)”, then enforce UNIQUE (Employee, Project).

# & ASCII illustration (ternary diamond)
# ? Visual guide
# *                [Project]
# *                 /  M  \
# *                /       \
# *             M /   ◇     \ M
# *              /  Skilled  \
# *             /     Use     \
# *         [Employee] —— M —— [Skill]
# * Legend: ◇ = relationship; M labels show many on all three sides (M:M:M)

# & Cardinality summary and reminder
# ? Cardinality options
# * One-to-One (1:1), One-to-Many (1:M), Many-to-Many (M:N); ternary extends to M:M:M or constrained mixes.

# ? Key reminders
# * Cardinality expresses MAXIMUM participation.
# * For ternary, keep side constraints logically aligned; if not, prefer an associative entity plus binary relationships.
# * Validate against business rules (e.g., “one skill per employee per project” vs “multiple skills per employee per project”).


# *=======================================================================================================

#! Relationship - Participation

# & Participation, Identifying Relationships, and Relationship Attributes

# ? Definition of Participation
# * Participation = minimum number of relationships an entity instance must take part in.
# * Opposite of cardinality (which defines maximum).
# ^ Represented as:
# *   - "Must" → double line
# *   - "May" → single line
# ~ Participation depends on business rules and scenarios.

# ? Examples of Participation

# ^ Employee – Department (Work)
# *   - Must employee work in a department? → Depends on business rule.
# *   - If optional → "May"
# *   - Department may exist without employees (new department) → "May"

# ^ Employee – Department (Manage)
# *   - Each department must have a manager → "Must"
# *   - Not all employees are managers → "May"

# ^ Employee – Project (Work On)
# *   - Not all employees work on projects (e.g., HR, Security) → "May"
# *   - Project may exist without employees (tender stage) → "May"
# *   - Alternative business case: project must have employees → "Must"

# ^ Employee – Dependent (Has)
# *   - Employee may have dependents → "May"
# *   - Each dependent must belong to an employee → "Must"
# *   - Weak entity rule: participation from weak entity side is always "Must"

# ^ Employee – Employee (Supervise, recursive)
# *   - Not all employees supervise others → "May"
# *   - Not all employees have supervisors (e.g., CEO) → "May"

# ^ Employee – Car (Own)
# *   - Employee may own a car → "May"
# *   - Car may not belong to an employee (company-owned) → "May"

# ^ Employee – Contract (Has)
# *   - Each contract must belong to an employee → "Must"
# *   - Each employee must have a contract → "Must"

# ^ Ternary Relationship (Employee – Project – Skill)
# *   - Project must have employees with skills → "Must"
# *   - Skills must be used in projects → "Must"
# *   - Employees must use skills in projects → "Must"
# *   - Participation = Must–Must–Must

# ? Identifying Relationships
# * Relationship between a weak entity and its owner entity.
# * Represented with a double line.
# ^ Example:
# * Dependent (weak entity) depends on Employee (owner).

# ? Attributes on Relationships
# * Sometimes attributes belong to relationships, not entities.
# ~ Example 1: "Start Date" of Employee managing Department.
# *   - Not attribute of Employee or Department.
# *   - Belongs to "Manage" relationship.
# ~ Example 2: "Hours" worked by Employee on Project.
# *   - Not attribute of Employee or Project.
# *   - Belongs to "Work On" relationship.

# ? Summary
# * Participation defines minimum involvement (Must/May).
# * Weak entities always have "Must" participation with their owner.
# * Attributes can be attached to relationships when they describe the interaction, not the entity itself.
# * Conceptual design complete: Entities, Attributes, Keys, Relationships, Cardinality, Participation.

# *=========================================================================================================

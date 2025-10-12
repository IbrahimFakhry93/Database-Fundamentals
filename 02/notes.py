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

#
# & Data Modeling – Concepts, Importance, and Stages

# ? Why Data Modeling Matters
# * Tools differ from company to company, but concepts remain the same.
# * Interviewers focus on concepts, not tools → mastering them is essential.
# * Data modeling is the foundation of any data team:
# *   - Without it → data is unorganized, analysis is difficult, performance is poor.
# *   - With it → queries are faster, business processes are supported, insights are possible.

# ? What is Data Modeling?
# * Similar to an architect’s blueprint for a building.
# * Defines how data will be stored, organized, and related.
# ~ Helps in:
# *   - Organizing data elements
# *   - Creating relationships between entities
# *   - Supporting business processes and applications
# *   - Enabling analytics (e.g., top customers, inactive customers, targeted promotions)

# ? Benefits of Good Data Modeling
# * Performance → well‑designed models make queries run in seconds instead of minutes.
# * Scalability → can handle growth (e.g., from 100k to 2M customers).
# * Organization → links data together so analysis is possible.
# * Collaboration → allows engineers, analysts, BI developers, and data scientists to work together.

# ? Who Needs Data Modeling?
# * Essential for Data Engineers and BI Developers.
# * Important for Data Analysts and Data Scientists to understand (to discuss schema design, add features, etc.).

# & Stages of Data Modeling

# ? 1. Conceptual Data Model
# * High‑level view of the system (no technical details).
# * Identify main entities and relationships.

# * Example entities: Customers, Orders, Products, Sales.
# * Define relationships: one‑to‑many, many‑to‑many, etc.
# * Focus on business requirements and big picture.

# ? 2. Logical Data Model
# * Add more technical details.
# * Define tables, attributes, and relationships.
# * Decide how many tables are needed (e.g., Orders split into Daily vs Monthly).
# ~ Identify Fact Tables vs Dimension Tables:
# ^   - Fact Tables (for analysis) → store numeric/transactional data (sales, quantities, revenue).
# ^   - Dimension Tables → store descriptive data (customer info, product details).
# * Naming convention tip: prefix with Fact_ or Dim_ (e.g., FactOrders, DimCustomer).


# * Implement the schema in the database.
# * Define data types, indexes, constraints, and storage details.
# ^ Choose schema design approach:
# *   - Star Schema → central Fact table surrounded by Dimension tables.
# *       - Simpler, faster queries, but more storage (due to duplication).
# *   - Snowflake Schema → normalized Dimension tables (split into multiple related tables).
# *       - Reduces duplication, saves storage, but queries are slower (more joins).

# & Star Schema vs Snowflake Schema

# ? Star Schema
# * Fact table in the center, surrounded by denormalized Dimension tables (eg. only one table for customer contains all the info, same for products).
# * Simpler design, easier to understand.
# * Faster queries (fewer joins).
# * Uses more storage (due to duplication).

# ? Snowflake Schema
# * Fact table in the center, Dimension tables normalized into multiple related tables.
# * More complex design.
# * Slower queries (more joins).
# * Saves storage by reducing duplication.

# ? Example Trade-off
# * Star Schema → 12 GB storage, faster queries.
# * Snowflake Schema → 8.5 GB storage, slower queries.
# * Choice depends on business needs (speed vs storage efficiency).


# ? 3. Physical Data Model

# ^ Definition
# * The Physical Data Model is the final stage of data modeling.
# * It translates the logical design into actual SQL code and database objects.
# * Focuses on how data will be stored, indexed, and constrained in the DBMS.

# ^ Key Tasks
# * Create tables using SQL (CREATE TABLE statements).
# * Define columns with appropriate data types (e.g., VARCHAR, INT, DATE).
# * Set Primary Keys and Foreign Keys to enforce relationships.
# * Add Indexes to improve query performance.
# * Apply Constraints (e.g., NOT NULL, UNIQUE, CHECK).

# ^ Example – Indexing
# * Index works like a book index → speeds up data retrieval.
# ~ If the model is based on daily sales:
# !   - Queries often filter by SaleDate.
# *   - Create an index on SaleDate for faster lookups.
# *   - Example: CREATE INDEX idx_sales_date ON Sales(SaleDate);

# ^ Example – Table Creation
# *   CREATE TABLE Customers (
# *       CustomerID INT PRIMARY KEY,
# *       Name VARCHAR(100) NOT NULL,
# *       Email VARCHAR(100),
# *       Age INT,
# *       City VARCHAR(50)
# *   );
# ~ Notes:
# *   - Choose VARCHAR length carefully (too small → errors, too large → wasted storage).
# *   - Add Foreign Keys to reference other tables when needed.

# ^ Constraints
# * NOT NULL → column cannot accept NULL values.
# * UNIQUE → ensures all values in a column are distinct.
# * CHECK → enforces a condition (e.g., Age > 0).
# * PRIMARY KEY → uniquely identifies each row.
# * FOREIGN KEY → links to another table’s primary key.

# ^ Iterative Nature
# * Data modeling is not one‑time only.
# ~ Models evolve over time:
# *   - Add new columns
# *   - Create new tables
# *   - Define new relationships
# *   - Adjust indexes and constraints
# * Continuous refinement ensures the model adapts to business needs.

#! Summary
# * Stage 1 → Conceptual Model (high‑level entities & relationships).
# * Stage 2 → Logical Model (tables, fact vs dimension, schema design).
# * Stage 3 → Physical Model (SQL implementation, indexes, constraints).
# * Data modeling is iterative and evolves with requirements.

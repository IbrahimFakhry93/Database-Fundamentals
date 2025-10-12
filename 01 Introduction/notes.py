#!

#! Lec 01: Database Concepts

# ? Importance of Databases
# * Essential for IT professionals
# * Used in daily applications: e-commerce, supermarkets, email systems
# * Databases work in the background to store and manage data

# ? Before Databases: File-Based System
# * Relied on separate programs/applications for each department
# ^ Example:
# *   - HR → Word files for employee data
# *   - Accounting → Excel sheets for salaries
# ^ Issues:
# *   - Same employee data duplicated in multiple places
# *   - Difficult to share/update data across departments

# ? Example Scenario
# * Rule: Employee earns a bonus + salary increase if awarded a certificate/degree
# * HR updates Word file (salary + bonus) → must notify Accounting
#! Problems:
# *   - Accounting only uses Excel → incompatible formats
# *   - If HR delays notification → salaries processed without updates

# ? Limitations of File-Based Systems
# * Separation & isolation of data → scattered, not synchronized
# * Duplication of data → redundancy across departments
# * Program-data dependence → data tied to specific software
# * Incompatible file formats → Word vs Excel issue

# ? Emergence of Databases
# * Database = collection of related data (common relation)
# * Solves duplication, isolation, and compatibility issues

# ? Database Management System (DBMS)
# * Software responsible for creating and maintaining databases
# * Database System = Database + DBMS together
# * This combination is often referred to as a "Database Software System"

# *===================================================================================

#! Lec 02: Database systems Main components

# & Title: Database Systems – Main Components, Advantages & Disadvantages

# ? Main Components of a Database System
# * Database (bottom layer) → stores the actual data
# * DBMS (Database Management System) → software that controls & maintains the database
# * Application Program → interface used by end-users (e.g., e-commerce website UI)
# * End-user interacts with the application → application sends queries to DBMS → DBMS accesses database

# ? DBMS Internal Functions
# * Part 1: Processes queries from application programs
# * Part 2: Accesses the database to return, add, or edit data

# ? Database Structure
# * Divided into two parts:
# *~ 1. Metadata (Database Definition)
# *    - Info about data: table names, column names, datatypes
# *    - Constraints (e.g., unique, not null)
# *    - Permissions: usernames, passwords, privileges
# *    - Database object structures
# *    - Log files: transactions & actions history
# ~ 2. Stored Database
# *    - The actual data itself
# *    - Example: Employee record → Name: Mohamed, Birth: 1980, Salary: 10,000

# ? Advantages of DBMS
# * Controls redundancy → data stored in one location, accessible by many users
# * Controls unauthorized access → user accounts, permissions, privileges
# * Enforces integrity constraints → ensures data follows business rules
# *   - Example: Phone column must contain numbers, ID column must be unique
# * Avoids inconsistency → updates shared across all users simultaneously
# * Backup & recovery → compressed backups (file) to save space (memory) and restore data if needed

# ? Disadvantages of DBMS
# * Requires expertise → need to hire database administrators
# * Expensive → software cost + infrastructure + network requirements
# * Compatibility issues → not all DBMS are compatible for migration
# *   - Metadata helps transfer, but sometimes requires third-party tools to facilitate the transfer process

# ? Summary
# * Database System = Database + DBMS + Application Program
# * Metadata = "data about data" (structure, rules, permissions, logs)
# * Stored Database = actual records (e.g., employee info)
# * DBMS provides control, security, integrity, and recovery but comes with cost & complexity

# *===========================================================

#! Database Users and the Cycle of Creating a Database

# ? Step 1: Requirement Gathering & Analysis
# ^ - System analyst meets customer (company) to understand:
# *   • Why the system is needed
# *   • Nature of data usage (updates, additions, frequency)
# *   • Number and type of users
# *   • Data size, format, and growth rate
# *   • Infrastructure and budget
# ~ - Output: documented requirements

# ? Step 2: Database Design
# ^ - Database designer receives requirements from system analyst
# * - Creates data model (ERD, schema)
# * - Converts design into tables and database objects

# ? Step 3: DBMS Selection & Setup
# ^ - DBA (Database Administrator) recommends suitable DBMS based on:
# *   • Requirements, budget, number of users
# * - Purchase software, set up infrastructure
# * - Install DBMS

# ? Step 4: Database Creation
# * - DBA creates schema and tables based on designer’s model
# * - Load initial data into the database
# * - Create users and assign privileges

# ? Step 5: Application Development
# ^ - Application programmer builds user interface (UI)
# * - UI allows end-users to interact with the database without direct access
# * - Screens designed for specific tasks and permissions

# ? Step 6: Testing & Training
# * - Test the entire system (DB + UI)
# * - Train end-users on how to use the application

#! Roles of Database Users
# * System Analyst → gathers requirements, analyzes customer needs
# * Database Designer → converts requirements into data models and tables
# * DBA (Database Administrator) → installs DBMS, creates schema, loads data, manages users & privileges
# * Application Programmer → develops user interface for end-users
# * End-User → interacts with the system through the application program


# *===========================================================================

# & Database Management System (DBMS) Architecture

# ? Three-Schema Architecture
# * External Schema
# * Conceptual Schema
# * Physical Schema

# ? External Schema
# * Multiple external schemas can exist (e.g., External Schema 1, 2, 3)
# * Represents a set of final data which accessed only by specific types of users
# ~ Example:
# *   - Financial schema → accessed by Finance department
# *   - HR schema → accessed by HR department
# * Provides customized views of the database for different user groups

# ? Conceptual Schema
# * Contains all tables and relationships between data
# * Represents the overall logical structure of the entire database
# * Independent of physical storage details

# ? Physical Schema
# * Explains how data is stored on disk (explains allocation of the data on the disk)
# * The data at the end  is a group of files stored on my hard disk
# * Identifies physical file paths and storage locations (files location in the hard disk)
# * Tracks allocated space, free space, and used space
# * Works as a map of how data is distributed across the hard disk

# ? Why Three separate Schemas? → to achieve Data Independence
# * Data independence = changes in one schema do not require changes in higher-level schemas

# ~ Example:
# *   - Changing file location in physical schema → no effect on conceptual or external schemas
# *   - Adding a new table in conceptual schema → only external schemas that use or access this table should be affected
# * Ensures flexibility and stability for users and applications

# ? Data Models
# ^ Conceptual Data Model
# *   - Represents the conceptual schema
# *   - Full design of database schema (entities, relationships, ERD), covered later in ERD Chapter
# ^ Physical Data Model
# *   - Represents the physical schema
# *   - Explains how data is stored on hard disk
# *   - Defines access paths to facilitate efficient searching

# *====================================================================================


# & Mapping in DBMS Architecture

# ? Definition
# * Mapping is the process of transferring requests and results between the three schema levels:
# * - External Schema
# * - Conceptual Schema
# * - Physical Schema

# ? Example Flow of a Data Request
# * 1. End-user makes a request for a specific data through External Schema 1
# * 2. External Schema forwards the request to the Conceptual Schema
# * 3. Conceptual Schema identifies the relevant table for the requested data
# *     and forwards the request to the Physical Schema
# * 4. Physical Schema locates the data on the hard disk and processes the request on the disk
# * 5. Physical Schema retrieves the required data and sends it back to the Conceptual Schema
# * 6. Conceptual Schema passes the result to External Schema 1
# * 7. External Schema displays the result to the end-user

# ? Purpose of Mapping
# * Ensures smooth communication between schema layers
# * Allows abstraction and separation of concerns
# * Supports data independence by isolating changes at each level

# ? Key Benefit
# * Changes in one schema (e.g., physical file location) do not require changes in other schemas
# ^ Example:
# *   - Moving a file in the Physical Schema does not affect the Conceptual or External Schemas
# *   - Adding a new table in the Conceptual Schema only affects External Schemas that access it


# *====================================================================================

# & Advanced Data Types and Functions in DBMS

# ? Traditional DBMS Data
# * Initially supported only numbers and characters
# * Focused on storing and retrieving structured, textual data

# ? Support for Multimedia Data
# * Modern DBMS can store images, audio, and video
# * Each type has its own storage and retrieval mechanisms

# ? Spatial Data
# * Spatial data = data for maps and geographic systems
# * GIS (Geographical Information System) integrates with DBMS to handle spatial data
# * Enables specialized queries and operations on location-based data

# ? Time-Series Data
# * Data stored against time (e.g., stock market prices, timestamps)
# ^ Examples:
# *   - Share prices with start time and last price
# *   - Snapshots of all shares at a specific time
# ^ Benefits:
# *   - Faster processing for time-based queries
# *   - Specialized functions for time-series analysis
# * Some DBMS provide built-in support for time-series data

# ? Data Mining Functions
# * Data mining = analyzing data to extract insights
# * Common algorithms: clustering, classification, association rules
# ^ Applications:
# *   - E-commerce: segmenting customers into groups
# *   - Marketing: targeting offers to specific customer segments
# * Some DBMS include built-in data mining functions:
# *   - Provide access to algorithms with minimal customization
# *   - Useful for initial insights, even for small businesses
# * Limitation: less flexibility to modify algorithms compared to dedicated tools or system for data mining and analysis

# ? Key Takeaway
# * Modern DBMS go beyond traditional data storage
# * They support multimedia, spatial, time-series, and even data mining functions
# * This expands their role from simple storage to advanced analytics and decision support

# *=======================================================================================================

# & Centralized Database Environments

# ? Types of Centralized Database Environments
# * Mainframe Environment
# * Client-Server Environment (Two-Tier)
# * Internet Computing Environment (Three-Tier / N-Tier)

# ? Mainframe Environment
# * One mainframe machine hosts both database server and application server
# * Users connect via dummy terminals (no processing power, only request/response)
# * All processing happens on the mainframe
#! Problems:
# *   - Single point of failure (database + application on one machine)
# *   - High traffic → slow performance and response time
# *   - If mainframe fails → all users disconnected

# ? Client-Server Environment (Two-Tier)
# ~ Two tiers:
# *   - Database server (back-end)
# *   - Client application (front-end, installed locally on each user machine)
# * Client = "Thick Client" (application installed on every end-user machine)
# ^ Advantages:
# *   - Application not a single point of failure (only DB server is critical)
# *   - Processing divided: client handles part of application logic, DB handles data
#! Problems:
# *   - Still a single point of failure at the database server
# *   - High maintenance cost (updates must be applied on every client machine)
# *   - Expensive for large organizations (e.g., 1000 users in a bank)

# ? Internet Computing Environment (Three-Tier)
# ~ Three tiers:
# *   - Database server (back-end)
# *   - Application server (middle tier)
# *   - Thin client (front-end, accessed via browser or small applet)
# ^ Advantages:
# *   - Application logic centralized on application server
# *   - Easier maintenance (update once on app server → all clients updated automatically)
# *   - Lower client-side cost and support effort
#! Problems:
# *   - Still a single point of failure at the database server

# ? N-Tier Architecture (Extension of Three-Tier)
# * Multiple application servers in parallel (middle tier)
# ^ Benefits:
# *   - Load balancing: distribute users across servers
# *   - Fault tolerance: if one app server fails, users rerouted to another
# *   - Supports multiple applications (e.g., Finance app, HR app) connected to same DB
#! Problems:
# *   - Database server remains a single point of failure
# *   - If DB server fails → entire system goes down

# ? Summary
# * Mainframe → single machine, high failure risk, slow performance
# * Client-Server (Two-Tier) → thick clients, better distribution, but costly maintenance
# * Three-Tier → thin clients, centralized app server, easier updates, but DB still critical
# * N-Tier → multiple app servers for scalability and reliability, DB still single point of failure
# *=======================================================================================================


# & Distributed Database Environment

# ? Definition
# * A distributed database environment stores data across multiple servers/locations.
# ~ Two main methods:
# * Replication and Fragmentation.
# * Goal: improve availability, reduce downtime, and support geographically separated users.

# ? Benefits
# * High availability → system continues running even if one server fails.
# * as a server in a branch fails, the headquarter won't be affected
# * Critical for systems where downtime = financial loss.
# * Useful for organizations with branches in different locations.
# * Reduces single point of failure compared to centralized databases.

# ? Replication
# * Concept: "Copy & Paste" of the database.
# ^ Types:
# !   - Full Replication → entire database copied to another server.
# *       • Servers work back-to-back with heartbeat signals.
# *       • If one fails, the other starts up and takes over automatically.
# !  - Partial Replication → only part of the database is copied.
# *        copy part of database and is set up and installed in a different separated server
# *       • Example: branch office stores only relevant subset of database.
# *       • Original database still holds all data and is updated regularly.
# ^ Notes:
# *   - Requires synchronization to keep replicas consistent.
# *   - Increases availability but adds cost and complexity.

# ? Fragmentation
# * Concept: "Cut & Paste" of the database.
# ^ Types:
# !   - Horizontal Fragmentation → split by rows (records).
# !   - Vertical Fragmentation → split by columns (attributes).
# !   - Hybrid Fragmentation → combination of both.
# ^ Constraints:
# *   - Must preserve database rules, structure, and constraints.

# * Each fragment stored on a different server but connected via a network.
# ^ Benefits:
# *   - No single point of failure (if one fragment fails, others still work).
# *   - Each location stores only the data it needs.


# ? Practical Considerations
# * Each distributed node (replica or fragment) requires its own DBMS software and license.
# ~ Choice between centralized vs distributed depends on:
# *   - Business criticality of data
# *   - Tolerance for downtime
# *   - Budget for infrastructure and licenses
# * If data is not critical → centralized DB may be sufficient.
# * If high availability is essential → distributed DB is preferred.

# & Categories of Distributed Databases

# ? Homogeneous (Same Vendor)
# * All database servers use the same DBMS vendor and version
# * Easier to manage, configure, and maintain
# * Consistent data models, query language, and tools
# * Example: All servers running Microsoft SQL Server

# ? Heterogeneous (Different Vendor)
# * Database servers use different DBMS vendors or versions
# * More complex to integrate and maintain
# * Requires middleware or connectors to translate queries and data formats
# * Example: One server running Oracle DB, another running MySQL, both part of the same distributed system

# ? Key Point
# * Homogeneous = simpler, unified environment
# * Heterogeneous = flexible, but higher complexity and cost

# ! Summary
# * Distributed DB = Replication (copy) or Fragmentation (split).
# * Solves single point of failure in centralized systems.
# * Costs more but ensures uptime and resilience.
# * Decision depends on business needs and trade-offs.

# *=======================================================================================

# & Database Fundamentals – Summary & Next Steps

# ? Completed Topics
# * Database fundamentals concepts
# * Different models for database environments
# * Cycle of creating and setting up a database

# ? Upcoming Topics
# ~ Database Life Cycle
# ^ Conceptual Design
# *   - Created using ER (Entity Relationship) diagrams
# ^ Logical Design
# *   - Converting conceptual design into logical schema
# ^ Implementation in DBMS
# *   - Converting logical design into actual DBMS structures
# ^ Data Manipulation
# *   - How to deal with and manipulate data inside DBMS
# ^ Normalization
# *   - Process to improve database design
# *   - Ensures efficiency, stability, and reduced redundancy

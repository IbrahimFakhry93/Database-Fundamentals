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



# Academic Database Queries

## Overview
This project involves creating and querying a relational database for an academic setting. The database includes tables for students, groups, teachers, subjects, and grades. It is populated with random data using the Faker package. The project also contains a series of SQL query files to extract specific information from the database.

## Database Schema
- **Students Table**: Information about students.
- **Groups Table**: Details of student groups.
- **Teachers Table**: Records of teachers.
- **Subjects Table**: List of subjects with corresponding teachers.
- **Grades Table**: Students' grades for each subject with timestamps.

## Data Generation
- Approximately 30-50 students, 3 groups, 5-8 subjects, 3-5 teachers.
- Up to 20 grades for each student across all subjects.
- Data populated using the Faker package.

## SQL Queries
### Basic Queries
1. `query_1.sql`: Top 5 students with the highest average score across all subjects.
2. `query_2.sql`: Student with the highest average in a specific subject.
3. `query_3.sql`: Average scores in groups for a specific subject.
4. `query_4.sql`: Overall average score across all students and subjects.
5. `query_5.sql`: Courses taught by a specific teacher.
6. `query_6.sql`: List of students in a specific group.
7. `query_7.sql`: Grades of students in a specific group for a particular subject.
8. `query_8.sql`: Average grades given by a specific teacher.
9. `query_9.sql`: List of courses attended by a student.
10. `query_10.sql`: Courses taught to a specific student by a specific teacher.

### Advanced Queries
1. `advanced_query_1.sql`: Average grade a particular teacher gives to a specific student.
2. `advanced_query_2.sql`: Grades of students in a specific group for a particular subject during the last class.

## Usage
1. Set up the database using the provided schema.
2. Populate the database with data using Faker.
3. Execute SQL queries using a database client or through a programming language interface like Python's `cursor.execute(sql)`.

## Installation
Clone the repository. To set up the database, you'll need a SQL database server like MySQL or PostgreSQL. The Faker package is required for data generation.

## Development and Testing
- Ensure the database schema is correctly set up.
- Validate the data generation scripts for proper and randomized data entry.
- Test each SQL query for accuracy and efficiency.

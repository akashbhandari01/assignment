--1. Create a MySQL database with name "users".
CREATE DATABASE users;
--2. Create a table named "users" with columns: 
--      id (Int Primary Key), 
--      name (VARCHAR), 
--      email (VARCHAR), 
--      role (VARCHAR).
USE users;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  role VARCHAR(255)
);

--3. Write SQL quries to:
--       a) Insert three records into the "users" table.
INSERT INTO users (name, email, role)
VALUES
('Alice Johnson', 'alice@example.com', 'Admin'),
('Bob Kumar', 'bob@example.com', 'Editor'),
('Chitra Singh', 'chitra@example.com', 'Viewer');

--       b) Retrive all users from the "users" table.
SELECT * FROM users;

--       c) Retrieve a specific user by thre id.

SELECT * FROM users WHERE id = 1;
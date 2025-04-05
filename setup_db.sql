-- ------------------------------------------------------------
-- Database Setup Script for MySQL Database:
-- Create database, user and grant priviledges.
-- ------------------------------------------------------------

DROP DATABASE IF EXISTS bible_quiz_db;
CREATE DATABASE IF NOT EXISTS bible_quiz_db;
CREATE USER IF NOT EXISTS 'bible_quiz_root'@'localhost' IDENTIFIED BY 'bible_quiz_root_pwd';
GRANT ALL PRIVILEGES ON `bible_quiz_db`.* TO 'bible_quiz_root'@'%';
GRANT SELECT ON `performance_schema`.* TO 'bible_quiz_root'@'%';
FLUSH PRIVILEGES;
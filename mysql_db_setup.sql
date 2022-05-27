-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS memedom_dev_db;
CREATE USER IF NOT EXISTS 'sheezy_dev'@'localhost' IDENTIFIED BY 'memedom_dev_pwd';
GRANT ALL PRIVILEGES ON `memedom_dev_db`.* TO 'sheezy_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'memedom_dev'@'localhost';
FLUSH PRIVILEGES;
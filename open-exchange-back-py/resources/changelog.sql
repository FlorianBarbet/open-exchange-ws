CREATE DATABASE open_exchange;
CREATE USER 'rate_service'@'localhost' IDENTIFIED BY 'toto';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, INDEX on *.* TO 'rate_service'@'localhost' WITH GRANT OPTION;

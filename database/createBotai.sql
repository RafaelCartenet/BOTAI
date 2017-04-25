drop database if exists botai;
Create database IF not Exists botai;

CREATE USER IF not Exists 'eclipse'@'localhost' IDENTIFIED BY 'tcho1nTch0in';
GRANT ALL ON botai.* TO 'eclipse'@'localhost';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'eclipse'@'localhost';
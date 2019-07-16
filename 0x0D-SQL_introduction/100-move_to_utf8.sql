-- Go to UTF8
-- script that converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0;
-- used notes from https://dev.mysql.com/doc/refman/8.0/en/charset-conversion.html
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
-- used notes from Stack Overflow on ALTAR TABLE
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

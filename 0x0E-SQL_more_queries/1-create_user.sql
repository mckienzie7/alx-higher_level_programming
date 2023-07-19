-- Write a script that creates the MySQL server user user_0d_1.
--  User_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fail
CREATE USER IF NOT EXISTS user_0d_1
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL
ON Classicmodels.*
TO user_0d_1;

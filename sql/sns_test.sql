USE python_sns;
SET FOREIGN_KEY_CHECKS = 0;
DELETE from posting;
ALTER TABLE `posting` auto_increment = 1;

DELETE from users;
ALTER TABLE `users` auto_increment = 1;

DELETE from evaluation;
ALTER TABLE `evaluation` auto_increment = 1;

DELETE from user_icon;
ALTER TABLE `user_icon` auto_increment = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- table_derete
DROP TABLE evaluation;
DROP TABLE user_icon;
DROP TABLE posting;
DROP TABLE users;

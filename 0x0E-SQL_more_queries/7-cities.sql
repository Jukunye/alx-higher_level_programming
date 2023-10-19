-- script that creates a database and table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`state_id`),
    REFERENCES `hbtn_0d_usa`.`states`(`id`)
);

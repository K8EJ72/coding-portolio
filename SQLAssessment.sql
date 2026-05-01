-- =======================================================================================

-- WIZARD101 BATTLE DATABASE
-- This program is a database made based on the MMORPG Wizard101.
-- It details the final dungeon of Dragonspyre 'The Great Spyre' and takes you through
-- each battle until the final boss fight against Malistaire Drake. Each wizard will bring
-- their own spells and will be assigned in a specific battle order to fulfil their roles to
-- complete the dungeon. Essentially, this is my perfect run of the final dungeon.

-- =======================================================================================

CREATE DATABASE IF NOT EXISTS Wizard101BattleDB;
USE Wizard101BattleDB;

DROP TABLE IF EXISTS Battles;
DROP TABLE IF EXISTS Spells;
DROP TABLE IF EXISTS Wizards;
DROP TABLE IF EXISTS Enemies;
DROP TABLE IF EXISTS Schools; 

CREATE TABLE Schools (
    school_id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(50)
);


CREATE TABLE Wizards (
    wizard_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    level INT CHECK (level >= 40),
    school_id INT,
    FOREIGN KEY (school_id) REFERENCES Schools(school_id)
);


CREATE TABLE Spells (
	spell_id INT AUTO_INCREMENT PRIMARY KEY,
	spell_name VARCHAR(100),
	spell_type VARCHAR(20),
	pip_cost INT CHECK (pip_cost >= 0),
	school_id INT,
	FOREIGN KEY (school_id) REFERENCES Schools(school_id)
);


CREATE TABLE Enemies (
    enemy_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    enemy_rank INT,          
    health INT,
    school_id INT,           
    FOREIGN KEY (school_id) REFERENCES Schools(school_id)
);


CREATE TABLE Battles (
    battle_id INT AUTO_INCREMENT PRIMARY KEY,
    firstwizard_id INT,
    secondwizard_id INT,
    thirdwizard_id INT,
    fourthwizard_id INT,
    bossenemy_id INT,
    minion_enemy1_id INT,
    minion_enemy2_id INT,
    minion_enemy3_id INT,
    winner_id INT,
    battle_date DATE,
    FOREIGN KEY (firstwizard_id) REFERENCES Wizards(wizard_id),
    FOREIGN KEY (secondwizard_id) REFERENCES Wizards(wizard_id),
    FOREIGN KEY (thirdwizard_id) REFERENCES Wizards(wizard_id),
    FOREIGN KEY (fourthwizard_id) REFERENCES Wizards(wizard_id),
    FOREIGN KEY (bossenemy_id) REFERENCES Enemies(enemy_id),
    FOREIGN KEY (minion_enemy1_id) REFERENCES Enemies(enemy_id),
    FOREIGN KEY (minion_enemy2_id) REFERENCES Enemies(enemy_id),
    FOREIGN KEY (minion_enemy3_id) REFERENCES Enemies(enemy_id),
    FOREIGN KEY (winner_id) REFERENCES Wizards(wizard_id)
);

-- INSERTING SAMPLE DATA TO TABLE
-- The examples provided are from my own Wizard101 characters, and those of my
-- friends. Thank you Sam and Beth for allowing me to mention your wizards!
-- Other data includes the school types, spells used and enemies.


INSERT INTO Schools (school_name) VALUES
('Fire'),
('Ice'),
('Storm'),
('Life'),
('Myth'),
('Death'),
('Balance'),
('Sun'),
('Moon'),
('Star'),
('Shadow');


INSERT INTO Wizards (name, level, school_id) VALUES
('Taryn Frost', 170, 2),
('Alyssa Dragon', 170, 1),
('Alia Storm', 125, 3),
('Morgan Drake', 105, 6),
('Laurel Garden', 65, 4),
('Sestiva Sand', 65, 7),
('Samuel RisingWand', 65, 3),
('Eli Temple', 40, 5),
('Saffron WillowWeaver', 170, 4);


INSERT INTO Spells (spell_name, spell_type, pip_cost, school_id) VALUES
('Tower Shield', 'Defense', 0, 2),
('Legion Shield', 'Defense', 1, 2),
('Volcanic Shield', 'Defense', 0, 2),
('Balanceblade', 'Support', 0, 7),
('Elemental Blade', 'Support', 1, 7),
('Bladestorm', 'Support', 1, 7),
('Hex', 'Support', 0, 7), 
('Elemental Trap', 'Support', 1, 7),
('Availing Hands', 'Healing', 3, 7),
('Sharpened Blade', 'Support', 0, 8),
('Potent Trap', 'Support', 0, 8),
('Primordial', 'Support', 0, 8),
('Feint', 'Support', 1, 6),
('Stormblade', 'Support', 0, 3),
('Storm Trap', 'Support', 0, 3),
('Windstorm', 'Support', 1, 3),
('Storm Lord', 'Attack', 7, 3),
('Glowbug Squall', 'Attack', 5, 3),
('Frenzy', 'Support', 0, 10),
('Legend Shield', 'Support', 0, 4),
('Minor Blessing', 'Healing', 0, 4),
('Satyr', 'Healing', 4, 4),
('Rebirth', 'Healing', 7, 4),
('Pigsie', 'Healing', 5, 4),
('Guiding Light', 'Support', 0, 4),
('Brillaint Light', 'Support', 2, 4);


INSERT INTO Enemies (name, enemy_rank, health, school_id) VALUES
('Gurtok Firebender', 9, 5600, 1),
('Feral Lavaling', 8, 890, 1),
('Magma Fury', 8, 890, 1),
('Gurtok Piercer', 9, 5600, 2),
('Sharpshard Warrior', 8, 890, 2),
('Sharpshard Warrior', 8, 890, 2),
('Soul Servant', 8, 890, 6),
('Soul Servant', 8, 890, 6),
('Soul Servant', 8, 890, 6),
('Soul Servant', 8, 890, 6),
('Malistaire Drake', 10, 8000, 6),
('Soul Servant', 8, 890, 6),
('Soul Servant', 8, 890, 6),
('Soul Servant', 8, 890, 6),
('Soul Servant', 8, 890, 6),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Decaying Blackguard', 8, 890, 2),
('Tumok Gravelbeard', 9, 6400, 5),
('Vengeful Fireheart', 8, 890, 5),
('Vengeful Fireheart', 8, 890, 5),
('Soul Searcher', 8, 1115, 6),
('Feral Lavaling', 8, 890, 1),
('Feral Lavaling', 8, 890, 1);


INSERT INTO Battles (firstwizard_id, secondwizard_id, thirdwizard_id, fourthwizard_id, 
     bossenemy_id, minion_enemy1_id, minion_enemy2_id, minion_enemy3_id, 
     winner_id, battle_date) VALUES
(1, 5, 6, 3, 11,  7,  8,  9, 1, '2026-04-19'),
(1, 5, 6, 3,  4,  5,  6, NULL, 3, '2026-04-19'),
(1, 5, 6, 3, NULL, 27, 28, 29, 1, '2026-04-19'),
(1, 5, 6, 3, 24, 25, 26, NULL, 3, '2026-04-19'),
(1, 5, 6, 3, NULL, 17, 18, 19, 6, '2026-04-19'),
(1, 5, 6, 3, NULL, 21, 22, 23, 1, '2026-04-19'),
(1, 5, 6, 3, NULL,  7,  8,  9, 5, '2026-04-19'),
(1, 5, 6, 3, 11, 12, 13, 14, 3, '2026-04-19');


-- TIME FOR A FUNCTION.
-- I have chosen to write a function that gathers the total strength of
-- my four chosen wizards, to see if they'd do well against the final boss.

-- Write the function

DELIMITER //

-- CREATE FUNCTION WizardTeamStrength(
DROP FUNCTION IF EXISTS WizardTeamStrength(
	p_wizard1 INT, p_wizard2 INT, p_wizard3 INT, p_wizard4 INT
	) RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE wizard_strength INT;
	SELECT (w1.level + w2.level + w3.level + w4.level)
	INTO wizard_strength
	
	FROM Wizards w1
	JOIN Wizards w2 ON w2.wizard_id = p_wizard2
	JOIN Wizards w3 ON w3.wizard_id = p_wizard3
	JOIN Wizards w4 ON w4.wizard_id = p_wizard4
	WHERE w1.wizard_id = p_wizard1;
	
	RETURN wizard_strength;
END //

DELIMITER ;

-- Now for my selected wizards collective strength
SELECT WizardTeamStrength(1,3,5,6) as wizard_strength;


-- QUERIES

-- Wizard information, name and school. List them by their levels.
SELECT UPPER(w.name)
AS wizard_name
w.level, s.school_name AS School
FROM Wizards w
JOIN Schools s ON w.school_id = s.school_id
ORDER BY w.level DESC;

-- Sort wizards based on their battle achievements
SELECT w.name, 
COUNT(*) AS battle_victories
FROM Wizards w
JOIN Battles b ON w.wizard_id = b.winner_id
GROUP BY w.name
ORDER BY battle_victories DESC;

-- Showcase which spells my wizard team are able to use
SELECT 
w.name AS wizard_name, 
sp.spell_name, 
sp.spell_type, 
sp.pip_cost
FROM Wizards w
JOIN Spells sp ON sp.school_id = w.school_id
WHERE w.wizard_id IN (1, 3, 5, 6)
ORDER BY w.name, sp.pip_cost DESC;

DELETE FROM Wizards
WHERE level < 40;
-- remove any wizard from the lineup who doesn't meet the dungeon level requirement.



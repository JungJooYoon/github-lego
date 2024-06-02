--- 02-06-2024 14:15:08
--- LEGO.db
--  List all sets released in a specific year
SELECT s.name, s.set_num, s.year
FROM sets s
WHERE s.year = 2024;

--- 02-06-2024 14:15:09
--- LEGO.db.1
--  List all sets released by theme
SELECT s.name, s.set_num, s.year
FROM sets s
JOIN themes t ON s.theme_id = t.id
WHERE t.id = 158 OR t.parent_id = 158;

--- 02-06-2024 14:15:11
--- LEGO.db.2
--  List all sets released by theme in a specific year
SELECT s.name, s.set_num, s.year
FROM sets s
JOIN themes t ON s.theme_id = t.id
WHERE s.year = 2024 AND (t.id = 158 OR t.parent_id = 158);

--- 02-06-2024 14:15:12
--- LEGO.db.3
--List of parts in a set
SELECT p.part_num, p.name, ip.quantity
FROM inventory_parts ip
JOIN parts p 
ON ip.part_num = p.part_num
WHERE ip.inventory_id = (SELECT id FROM inventories WHERE set_num = '10179-1');


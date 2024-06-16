GROUP BY
-- GROUP BY example
SELECT t.name AS theme_name, COUNT(s.set_num) AS set_count
FROM themes t
JOIN sets s ON t.id = s.theme_id
GROUP BY t.name
ORDER BY set_count DESC
LIMIT 1;


HAVING
-- HAVING
SELECT theme_id, t.name, COUNT() as num_sets
FROM sets s
JOIN themes t ON t.id = s.theme_id
GROUP BY theme_id
HAVING COUNT() > 50
ORDER BY num_sets DESC;


MAX
-- MAX
SELECT theme_id, MAX(year) as most_recent_year
FROM sets
GROUP BY theme_id;


SUM
-- SUM
SELECT inventory_id, SUM(quantity) as total_parts
FROM inventory_parts
GROUP BY inventory_id; 


DELETE (Anomalies)

-- Anomalies (DELETE)
DELETE FROM sets
WHERE sets.set_num LIKE '4727-1';

-- Anomalies (DELETE)
DELETE FROM sets
WHERE sets.set_num LIKE '4727-1';
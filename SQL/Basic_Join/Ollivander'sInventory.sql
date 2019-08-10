SELECT id,age,coins_needed,power
FROM wands as w 
    INNER JOIN wands_property as p
        ON w.code = p.code
WHERE is_evil = 0 and 
    (SELECT count(*) 
    FROM wands as a 
    INNER JOIN wands_property as r
        ON a.code = r.code
    WHERE p.age = r.age and w.power = a.power and a.coins_needed <= w.coins_needed)<=1
ORDER BY power desc,age desc

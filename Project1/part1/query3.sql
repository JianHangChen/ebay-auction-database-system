SELECT COUNT(*)
FROM (SELECT ItemID, COUNT(*) AS C
	FROM belong_to_Cat
	GROUP BY ItemID)
WHERE C = 4;


--Find the number of auctions belonging to exactly four categories. SELECT ItemID
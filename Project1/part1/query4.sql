SELECT ItemID
FROM Item,
	(SELECT MAX(Currently) AS highest
	FROM Item)
WHERE Currently = highest;



--Find the ID(s) of auction(s) with the highest current price. 
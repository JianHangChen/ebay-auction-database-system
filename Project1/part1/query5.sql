SELECT count(DISTINCT Sell.UserID)
FROM User, Sell
WHERE Rating > 1000 AND User.UserID = Sell.UserID;


--Find the number of sellers whose rating is higher than 1000. 
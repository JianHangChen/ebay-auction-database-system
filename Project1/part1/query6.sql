SELECT count(DISTINCT Sell.UserID)
FROM Sell,Bid
WHERE Sell.UserID = Bid.UserID;




--6. Find the number of users who are both sellers and bidders.
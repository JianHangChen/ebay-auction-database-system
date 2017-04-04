SELECT COUNT(DISTINCT CategoryName)
FROM belong_to_Cat,Bid
WHERE belong_to_Cat.ItemID = Bid.ItemID AND Bid.Amount > 100;


-- include at least one item with a bid of more than $100. 
DROP TABLE IF EXISTS Item;
CREATE TABLE Item(
	ItemID INTEGER PRIMARY KEY,
	Name TEXT,
	Description TEXT,
	Started TEXT,
	Ends TEXT,
	First_Bid REAL,
	Currently REAL,
	Number_of_Bids INTEGER,
	Buy_Price REAL
);

DROP TABLE IF EXISTS User;
CREATE TABLE User( 
	UserID TEXT PRIMARY KEY, 
	Rating INTEGER,
	Country TEXT,
	Location TEXT
);

DROP TABLE IF EXISTS Category;
CREATE TABLE Category( 
	CategoryName TEXT PRIMARY KEY
);

DROP TABLE IF EXISTS Bid;
CREATE TABLE Bid( 
	BTime TEXT,
	ItemID INTEGER,
	UserID TEXT,
	Amount REAL,
	PRIMARY KEY (BTime,ItemID,UserID),
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID),
	FOREIGN KEY (UserID) REFERENCES User(UserID)
);


DROP TABLE IF EXISTS Sell;
CREATE TABLE Sell(
	ItemID INTEGER,
	UserID TEXT,
	PRIMARY KEY (ItemID,UserID),
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID),
	FOREIGN KEY (UserID) REFERENCES User(UserID)
);


DROP TABLE IF EXISTS belong_to_Cat;
CREATE TABLE belong_to_Cat(
	ItemID INTEGER,
	CategoryName TEXT,
	PRIMARY KEY (ItemID,CategoryName),
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID),
	FOREIGN KEY (CategoryName) REFERENCES Category(CategoryName)
);
#RunParser
rm -f *.dat;
python 20166418.py ./ebay_data/items-*.json;

sort Item.dat | uniq > Item_table.dat
sort User.dat | uniq > User_table.dat
sort Category.dat | uniq > Category_table.dat
sort Bid.dat | uniq > Bid_table.dat
sort Sell.dat | uniq > Sell_table.dat
sort belong_to_Cat.dat | uniq > belong_to_Cat_table.dat

##################
# sqlite3 test.db < create.sql
# sqlite3 test.db < load.txt
# sqlite3 test.db < query1.sql
# sqlite3 test.db < query2.sql
# sqlite3 test.db < query3.sql
# sqlite3 test.db < query4.sql
# sqlite3 test.db < query5.sql
# sqlite3 test.db < query6.sql
# sqlite3 test.db < query7.sql
#RunParser
rm -f *.dat;
python 20166418.py ./ebay_data/items-*.json;

sort Item.dat | uniq > Item_table.dat
sort User.dat | uniq > User_table.dat
sort Category.dat | uniq > Category_table.dat
sort Bid.dat | uniq > Bid_table.dat
sort Sell.dat | uniq > Sell_table.dat
sort belong_to_Cat.dat | uniq > belong_to_Cat_table.dat

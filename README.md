# Price Impact Project
*Diane PERES and Larysa MATIUKHA*

---
### Data 
* Files \[ Time; Values \]
  *  Bid Price
  *  Bid Volume
  *  Ask Price
  *  Ask Volum
  *  MO 

### 1st step

Build a file with all the LO : Time, Ask Price, Bid Price, Ask Volum and Bid Volum

* **Merging.py**
  * *function merging* output MergedTimebis.csv: \['Time','Offer_Bid','Row' \]
    * 'Time' 
    * 'Offer' = o, 'Bid' = b or 'Bid and Offer' = ob, 
    * 'Row' of the bid in the file , 'Offer_Row' = row of the offer in the file OR 'Row' of the offer in its file, 'Offer_Row' = empty

### 2nd step
In this step we will focus on specific values of the spread (Spread = Ask - Bid)

* **LO_creation.py**
  * *function combinaison* output LO_File.csv: \['Time','Bid_Price','Bid_Volume','Offer_Price','Offer_Volume' \]
  * *function extract_spread* output the same file with a selected spread


### 3d step

Compute Imbalance and True price

Plot the 'Distribution of traded volume across imbalance levels, for spread = 1’

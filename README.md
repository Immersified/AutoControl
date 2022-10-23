# AutoControl
Automatic NFT bidder / lister on Opensea

Durring the summer break, the development started on a system that automatically bids and list's nft's. AutoControl is the name given to it.
Where the main objective is to create a high bidding bot that buy's nft's and sells them automatically for a tiny profit in high volume.

Over 50000 data points have been collected from around 1600 collections on ones to bid. It's time to put this information to use. 
A combination between Python and Windows power automate, a bot is created that automatically puts out collection offers. 
It changes the offer price based on the floor price and bids on certain collections put in an excel sheet.

However, buying is only 50% of the task. Selling them is another challenge that must be acomplished to make it fully passive.

In this project, updates will be given about the progress with context and toughts. The final product would include:

- Quick collection offer bidding (5-10 colletions / min)
- Outbid function where the bot scans wether higher offers are made to outbid them untill a certain degree
- Automatically list's the nft's on Opensea, looksrare & x2y2

Optional:
- Swap eth to wrapped eth after selling nft's to continue bidding

# AutoControl
Automatic NFT bidder / lister on Opensea

Durring the summer break, the development started on a system that automatically bids and list's nft's. AutoControl is the name given to it.
Where the main objective is to create a high bidding bot that buy's nft's and sells them automatically for a tiny profit in high volume.

With an OpenSea Scraper created on Windows Power Automate, Over 50000 data points have been collected from around 1600 collections on ones to bid. It's time to put this information to use. This is how one of the excel file look like: 
![image](https://user-images.githubusercontent.com/115187612/197599197-74fb091a-76f6-45ea-92f3-1be5d866f451.png)

The data then gets filtered in ([Opensea Data Scraper filter.py](https://github.com/Immersified/AutoControl/blob/main/Opensea%20Scraper%20Data%20Filter.py)) which sorts data based on activity, floor price and best offer to study which collections are most profitable based on net profit and profit to floor ratio. To visualize this more clear, two graphs are created. ![Github graph](https://user-images.githubusercontent.com/115187612/197601865-96ac8888-d147-4f98-8d4b-a1d73ab998a1.png)
Where the upper shows net profit and the lower net profit to floor ratio.

To actually use this data, a combination between Python and Windows power automate is used to create a bot. Which automatically puts out collection offers. 
It changes the offer price based on the floor price and bids on certain collections put in an excel sheet.![image](https://user-images.githubusercontent.com/115187612/197603927-48edea0b-7f75-4a2c-a6e9-3f8dff0ee253.png)

However, buying is only 50% of the task. Selling them is another challenge that must be acomplished to make it fully passive.

In this project, updates will be given about the progress with context and toughts. The final product would include:

- Quick collection offer bidding (5-10 colletions / min)
- Outbid function where the bot scans wether higher offers are made to outbid them untill a certain degree
- Automatically list's the nft's on markets such as: Opensea, looksrare & x2y2

Optional:
- Swap eth to wrapped eth after selling nft's to continue bidding

The current priority is to obtain an API key. Preferably from Opensea but options like the x2y2, nftgo and compass would possibly do the job.
If you have any reccomendations which one would be the best for our objectives, let it know :)

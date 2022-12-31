# AutoControl
Automatic NFT bidder / lister on Opensea

Project AutoControl develops an nft trading bot that automatically buys and sells nft's. Creating an environment where passive income is generated. The following subjects will be discussed:
* Bidding bot statistics
* Vision of Project AutoControl
* The bidding bot:
* Data Scraper:
* Bidding bot version 2:

## Bidding Bot Statistics:

This is the current version being used and connected to the wallet adres: 0x4fb1136a1122b2312089B0a7bA2111866A6f7b59
A statistic overview of the bot's performance can be seen here: https://flips.watch/0x4fb1136a1122b2312089b0a7ba2111866a6f7b59

The bot made it's first purchase on 22-oct-2022. And has gained a total profit of 7.275 Ethereum according to flips.watch as of 31-dec-2022. This number is however not 100% accurate as some assets have been transferred through nft trading. Which results in the website considering the selling price as full profit. A more realistic estimation would be 4 Ethereum. The amount of liquidity used in this proces varies a lot. However, the bot started with a capital of about 1.5 Ethereum.

## Vision of project AutoControl:

When looking at the end goal of project AutoControl, we perceive a bidding bot that automatically buys and sells nft's. Here, Collection offers are made with a certain profit margin set by the user. Trait bidding would also be an option. Different marketplaces will be used to send collection offers. Mainly Opensea and Blur at the time of writing. 

Once an nft get's bought, it automatically get's listed on Opensea, Blur, X2Y2 and Looksrare for the same net profit. Here, the listing price depends on the royalty fee, market fee and floor price of different marketplaces.

To access the bot, an nft collection will be created which can be used as access key. With this, the user can connect a wallet to use a special interface. Which gives all the different options to edit collections the bot bids on and profit margins. One important aspect is the user friendlyness the interfaces provides. By making a 'plug and play' option. This option doesn't require anything other then assigning a wallet with a certain capital to use for bidding. All the collections the bot bids on are pre-determined by a data scraper mentioned later in this readme and a profit percentage that optimizes between amount of sales and profit per sale.

Of course some users prefer a more diversified experience. Which includes the following options:
* Collections to bid on with trait bidding included
* Custom profit formula to determine how much profit at a certain floor price or seperate profit percentage per collection
* Use data scraper reccomendations based on needs of user (min / max floor price, min / max activity etc.)
* Abiltiy to turn autolisting on and of with certain collections
* Notifications when an offer gets accepted

This section will become more detailed as time passes (last updated on 31-dec-2022). 

## The bidding bot:

A combination between Python and Windows power automate is used to create the bidding bot. Which automatically puts out collection offers. 
It changes the offer price based on the floor price and bids on certain collections put in an excel sheet. Moreover, the bot has the ability to outbid the highest collection offer. The speed of the bidding bot is about one transaction every 40 seconds.

First, an excel sheet with the collections get's created:

![image](https://user-images.githubusercontent.com/115187612/197603927-48edea0b-7f75-4a2c-a6e9-3f8dff0ee253.png) 

Notice how the floor and bid price columns are empty. Those will be filled up with the code from: ([Bidding estimations.py](https://github.com/Immersified/AutoControl/blob/main/Bidding%20estimations.py)) 
Which includes a formula the user can edit. The end result would be a file such as: 

![image](https://user-images.githubusercontent.com/115187612/197606901-a6b5d79e-2ef6-41c2-83af-b9f058a12f68.png)

This file get's send to the Windows Power Automate bot which places the bids on collections. The following pseudo code is used for the bot:

![Untitled Diagram drawio (12)](https://user-images.githubusercontent.com/115187612/210140890-89609c38-e826-4b43-958b-f4e38dddbf33.png)

### Bidding bot Issues:

The current bidding bot does not use the api of Opensea to write collection offers. Which results in the speed of collection offers being only one per 40 seconds. Improving this is needed to enable users to bid on much more collections. Meaning much more potential to make profit. Moreover, it uses two programs to run the system which is too complicated for a non-experienced user. Another downside is the lack of automatic listing once an nft is purchased. Which is impossible to develop in the current setup. The bot also needs virtual machine or seperate computer to keep it running 24/7. At last, the uptime of the bidding bot is too low due to errors often conjesting the proces.

## Data scraper

Due to market circumstances, it's mandatory to update collections the bot bids on. First, an analysys of the current bidding collections needs to be obtained. Which is done by the file: ([Current Collection Analyzer.py](https://github.com/Immersified/AutoControl/blob/main/Current%20collection%20analyzer.py)) This results in a graph such as the following: 

![image](https://user-images.githubusercontent.com/115187612/210141306-b83be809-8b3f-45f0-87ec-f16d87acfed5.png)

The figure shows three graphs. The upper are the daily sales, the middle are the daily amount of sales averaged over a week and the bottom shows averaged over a month. For easier readability, the collections are given different bar colors which show to what extend the averages sales are within the threshold put in by the user. In this case it would be between 5 and 25 sales per day. 
* Green means the treshold is met on all three graphs
* Yellow means on two out of three graphs
* Red on one out of three
* Black on none of the graphs

The last detail are the black and green lables of the collections. Green meaning the floor price is between the recommended price of the user. In this case, 0.3 to 3 Ethereum. Black means it's out of this bandwidth. 

Now the user is able to consider which collections to keep bidding on and can replace them with new collections. For this, a database of about 2000 collections is stored which all get tested in the same manner the current collections get analyzed. Which are the desired floor price and activity threshhold.
The only part missing is an estimate whether the bot will be able to compete with the highest collection offer. This get's acomplished by a data scraper who collects the currect highest collection offer of the extraced collections. Once the current offers are collected, two graphs are made of the new suggested collections to bid on in the code: ([New collection offer / Offer est.py](https://github.com/Immersified/AutoControl/blob/main/New%20Collection%20Offer%20%26%20Offer%20est.py)) One graph is  the same activity graph seen in: ([Current Collection Analyzer.py](https://github.com/Immersified/AutoControl/blob/main/Current%20collection%20analyzer.py))

The other graph shows the comparison of estimated collection bid (Best Offer est.) to the actual highest collection offer (Best Offer):

![image](https://user-images.githubusercontent.com/115187612/210148610-c032427a-a407-454a-a5ef-574aa3720844.png)

This creates a good indication which collections are interesting to bid on. 

## Bidding bot Version 2:

To improve on the aspects mentioned of the first bidding bot, a second version is created which uses the opensea api to acces all the features needed to make a fully passive bidding bot.

The new version will have the following features:
* Average time to create a collection offer: 2 seconds
* Virtualy no downtime 
* Easier to use interface
* All previous features of version one

A new language is intorduced for the bot which is Javascript to enable writing of collection offers and in the future, listing nft's. This also enables easier connection to an online or offline interface people can use to manage the bot. This also applies when connecting the bot to an nft collection who users can access the bot through. 

Inorder to use the bot, the command prompt is used. First the user has to direct to the folder of the bot. Which is done by the code: cd [Bidding bot script] directory>. Next up: yarn install is written to install the needed packages to use the bot. Finally the following command is used to start the bot: yarn start -p [private key] -a [api key] -l [bidding links excel]

### Issues and Security

Currently the bot is functional but not 100% reliable. It sometimes extracts the wrong number for the highest collection offer which can lead to a wrong collection offer being put out. Moreover, the interface is still not friendly enough for people to use. Another issue is the fact a virtual machine or extra computer is needed to have the bot operational 24/7. Another aspect to be added is the auto listing feature. This will be introduced in the third version. At last, an API key is required to use the bot. This is something we cannot require from the clients to have prematurely.

Security is another important aspect to consider because the user has to hand in a private key of their wallet. If that private key gets compromised, so does the wallet and everyone with that key, can access someone's wallet with any intent. In the current testing phase, this is not priority tough it will become a big aspect once the bidding bot will be available publicly. 

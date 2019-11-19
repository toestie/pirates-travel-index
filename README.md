# Group Members
* Chris Nguyen (Team Leader) : [@c-l-nguyen](https://github.com/c-l-nguyen)
<!-- * Hayley Jellison : [@hayleyjellison](https://github.com/hayleyjellison) -->
* Hazel Despain : [@hazeldespain](https://github.com/hazeldespain)
* Nathan Wong (Git Master) : [@toestie](https://github.com/toestie)

![TouristBanner](./Resources/images/banner.jpg)

# Project Proposal
The idea for this project is comparing tourist count versus local population count through the years 2011 - 2017. There is no one particular data set that has all the data that we are interested, so we will curate and compile data from multiple sources into one database that has everything we want by using ETL (extract, transform, load.

### Data Sources (Extract):
* City Population (as gotten from CSVs on http://worldpopulationreview.com/)
* Number of International Visitors per city (as gotten from pdfs from MasterCard Index of Global Destination Cities; https://newsroom.mastercard.com/press-releases/bangkok-tops-mastercards-global-destination-cities-index-for-the-fourth-consecutive-year/)

### Cleaning and Aggregation (Transform):
All data will be linked by city name.

City population can be scraped by finding the city page on the website, downloading the CSV with the CSV button, and uploaded into postgresSQL tables.

The pdfs for international visitor counts was a little bit more difficult to parse through (as the information is in pdfs). The information can be pasted into Excel, a short macro executed to make the desired table, then saved as a csv to be uploaded into postgresSQL tables.

### Compiled Data (Load):
All of the data can then be linked by city names for a table showing:
* City Name
* Population Count
* International Visitor Count

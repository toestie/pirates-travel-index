# Project Proposal
As a group of high-tech pirates, we will study the change in tourism in the most popular tourist destinations of the past decade (2011-2018). We will create maps that track amount of tourists and how much they are spending to try to discover patterns in their behavior over the years. We will also use the annual World Happiness Report to see if there are any qualities that may contribute to tourism for cities. Finally, we will rank the top 10 tourist destinations according to number of tourists, expenditures, and their density index (i.e. number of tourists vs. local population ratio). That way, we will determine the best targets to plunder!

Link to deployed project on Heroku: https://pirates-travel-index.herokuapp.com/

# Group Members
* Chris Nguyen (Team Leader): [@c-l-nguyen](https://github.com/c-l-nguyen)
* Hayley Jellison (QA Tester): [@hayleyjellison](https://github.com/hayleyjellison)
* Hazel Despain (Tableau Visualization Analyst): [@hazeldespain](https://github.com/hazeldespain)
* Nathan Wong (Git Master): [@toestie](https://github.com/toestie)

![TouristBanner](./Pirates-Travel-Index-App/static/resources/images/banner.jpg)

# Sketch of Final Design
<!-- Sketch of the final design -->
<img src="./Pirates-Travel-Index-App/static/resources/images/sketch.jpg" alt="sketch" width="75%" height="75%"/>

# Findings
Through our exploration and visualization of the data, we were able to find that:
* Asia has the most number of the top visited cities in the world
* It's also one of the least expensive regions so cost is very much top of mind for visitors
* Amongst the most popular tourist cities, Istanbul, Tokyo, and Paris had the largest year-over-year percent difference or variation
* From the World Happiness Report, happiness did not seem to correlate very well with freedom to make life choices. The correlation with happiness was twice as strong with country GDP, life expectancy, and social support in comparison
* From our bump chart, we can see that Bangkok has spent the most time as the #1 tourist spot in the world during the 2010s, with London and Paris not far behind in rankings
* In terms of tourism expenses, Dubai consistently takes the top spot as the most expensive destination (although 2011 is strange. Perhaps it was only partially reported or data is incomplete?)
* Tourism density was highest in Amsterdam for the longest time. That is, until Phuket, Thailand and Antalya, Turkey suddenly shot up in 2017. Especially Phuket since it had almost 24 tourist per local person by 2018
* Despite Tokyo being on the top 10 tourist destination list, its tourism density is quite low. However, there is an obvious reason why: it's local population is 37 million people! Hard for tourist to outnumber that

Snapshots of working website:

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="1604" alt="website-1" src="Pirates-Travel-Index-App/static/img/1-pirates-travel-index.herokuapp.com_.png">  |  <img width="1604" alt="website-2" src="Pirates-Travel-Index-App/static/img/2-pirates-travel-index.herokuapp.com_maps.png">  |  <img width="1604" alt="wesbite-3" src="Pirates-Travel-Index-App/static/img/3-pirates-travel-index.herokuapp.com_patterns.png">  |
|<img width="1604" alt="website-4" src="Pirates-Travel-Index-App/static/img/4-pirates-travel-index.herokuapp.com_rankings.png">  |  <img width="1604" alt="website-5" src="Pirates-Travel-Index-App/static/img/5-pirates-travel-index.herokuapp.com_density.png">  |    |

# Special Notes
Please note that this project requires a URI string to be saved locally in a path file (such as a .bash_profile or .zshrc file) or as a config variable in Heroku as 'DATABASE_URL' to be able to access data stored in a database. The environment URI string (or ENV_URI as referenced in the code) should be in the form:

> `postgresql://{username}:{password}@{host}:{port}/{database_name}`

ex: `postgresql://postgres:changeme@localhost:5432/pirates-db`

Bonus: try to find our little pirate theme hidden somewhere on the site by clicking around.

# Data Sources

* https://github.com/toestie/pirates-travel-index/tree/master/data
* https://worldhappiness.report/
* https://data.worldbank.org
* https://newsroom.mastercard.com/wp-content/uploads/2019/09/GDCI-Global-Report-FINAL-1.pdf
* https://population.un.org/wup/Download/
   * https://population.un.org/wup/Download/Files/WUP2018-F12-Cities_Over_300K.xls
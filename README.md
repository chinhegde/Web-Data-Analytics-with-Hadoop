# Web Data Analytics with Hadoop MapReduce 

## Data Crawling

Data was scraped from WikiCFP website (www.wikicfp.com).
Guidelines for scraping were reviewed and followed strictly.

File: web_crawl.py
Packages used to crawl: BeautifulSoup, urllib
To limit the queries to run every 10 seconds (policy states 5 seconds), “sleep” function from the time module has been used.

URLs crawled (Big Data, Machine Learning & Data Mining)
http://www.wikicfp.com/cfp/call?conference=big%20data%20&page=1
http://www.wikicfp.com/cfp/call?conference=machine%20Learning&page=1
http://www.wikicfp.com/cfp/call?conference=data%20mining&page=1

After crawling the data, we have the following columns:
1. conference_acronym
2. conference_name
3. conference_date (only considered the “Start date”)
4. conference_location

## Data Cleaning

Data cleaning was done using OpenRefine.

Total number of rows before cleaning: 1200
Conditions used:
* The conference location is not N/A
* The conference location is a city (i.e., only country name OR online/cyberspace is removed)
* The conference date is not N/A or blank
* The conference name is not N/A
* Matching rows (same acronym, name, date, location) are removed from the dataset. Only the first entry is considered

## Hadoop MapReduce for Analysis & Visualization
### a. Compute and plot the number of conferences per city. Which are the top 10 locations?
Mapper emits: (City, 1)
Reducer adds all the values to give (City, count)

The graphs were not shown with plt.show as Ubuntu does not have an interactive GUI. Instead, plt.savefig() was used to directly save the bar chart result.
NOTE: All the Hadoop MapReduce output files (part-00000) have been renamed to the “number”.txt using the redirection command (“>”).

### b. For each conference regardless of the year (e.g., Big Data), output the list of cities.
Mapper emits (Topic, City)
Eg.: Big Data, San Jose
Reducer returns (Topic - Number of unique cities - List of cities joined with a comma (“,”))

### c. For each city compute and plot a time series of #conferences per year.
Mapper emits (City, Year) for each record
Reducer (City, {Year: #conferences}) -> (String, Dictionary)
Eg.: San Jose {2020: 45, 2021: 32,...}

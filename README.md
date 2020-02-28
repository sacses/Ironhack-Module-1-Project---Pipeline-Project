# Ironhack-Module-1-Project---Pipeline-Project


In this pipeline I imported the dataset using SQLite connection, after having browsed the provided database from Kaggle and selected the relevant columns from each table. The database contained information of members of the 2018 Forbes billionaire list.

Afterwards, the dataset is transformed into a DataFrame using pandas, the only Phyton library used to clean the features from inconsistencies in their records. The resulted cleaned DataFrame is exported for future reference into .csv format. 

Moving on, the dataset is enriched from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_research_and_development_spending) with a table containing Research and Development expenditures per country. Apart from using pandas, I ised json and requests Phyton libraries to scrap the web page and parse it into a DataFrame. Both, the original DataFrame obtained from Wikipedia and the resulted merged Dataframe are exported as well into .csv for future reference.

Finally, 3 graphs are plotted and exported into .png format based on the results of the merged DataFrame. The graphs show % of GDP spent in R&D compared to the number of billionaires in the top 20 countries with the greattest %, their R&D expenditured compared to the the total worth of their billionaires, and the same excluding China and USA, as their are outliers.


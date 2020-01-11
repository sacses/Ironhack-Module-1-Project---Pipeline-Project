# Ironhack-Module-1-Project---Pipeline-Project


In this pipeline we import the dataset using SQLite connection, after having browsed the provided database from Kaggle and selected the desired columns from each table. The database contains information of members of the 2018 Forbes billionaire list.

Afterwards, the database is transformed into a DataFrame using pandas, the only library used to clean the features from inconsistencies in their records. The resulted cleaned DataFrame is exported for future reference. 

Moving on, the dataset is enriched from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_research_and_development_spending) with a table showing Research and Development expenditures per country. Apart from leveraging pandas, json and requests libaries are used to scrap the web page and parse it into a DataFrame. Both, the original DataFrame obtained from Wikipedia and the resulted merged Dataframe are exported as well into .csv for future reference.

Finally, 3 graphs are plotted and exported into .png format based on the results of the merged DataFrame. The reports show % of GDP spent in R&D compared to the number of billionaires in the top 20 countries with the greates %, their R&D expenditured compared to the the total worth of their billionaires, and the same excluding China and USA, as their are outliers.


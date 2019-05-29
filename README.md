Environments
Before we start Its necessary to download few packages in python

bs4 (Beautiful Soup)
       
        For python prompt
        $ pip install bs4                         

        For Anaconda Prompt
        $ conda install -c anaconda beautifulsoup4 

gbq library (google big query) is used to directly import the data frame from python environment itself for that you need to           run this command in command prompt

        gbq (Google Big Query)

        For python prompt
        $ pip install pandas-gbq

        For Anaconda Prompt
        $ conda install pandas-gbq --channel conda-forge
        
Sources 

        •	 https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population
        •	 https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States


•	Wikipedia data provides the table of cities with attributes of population density, land area, change. Estimate, State values.

•	For this project bs4 and requests libraries are used to scrap the data.


Steps

        •	Initially data is scraped from Wikipedia using the bs4 (link is provided under sources section).

        •	Next step is data cleaning in this process we remove all the encoded formats from the data, using string logics (to see                 the code please open wiki.py).

        •	Once the data is cleaned it moved to pandas Data Frame.

        •	Same steps are repeated to extract cost of living index values from the numbeo.com (link is provided under sources                       section) and code is available at (City_index.py).

        •	In final step we concat both Data Frames and fill all n/a values with 0 and download it as csv file.

        •	This csv file compatible to upload into Bigquery table.

        •	In Another case we can directly import pandas dataframe to Bigquery table using pandas gbq (to see code open                             download_csv.py)

# Coronavirus Infected Visualization on Google Maps 
### Using the Kaggle's Novel Corona Virus 2019 Dataset's COVID19_open_line_list.csv
[The current Repo](https://github.com/josephedradan/Coronavirus_Mapping_kml)

[LINK TO VISUALIZATION](https://josephedradan.github.io/coronavirus_mapping_to_kml/)

Using the [Kaggle's Novel Corona Virus 2019 Dataset](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset) on the COVID19_open_line_list.csv file, map the locations of infected individuals.
I made this because the JohnHopkins [map](https://coronavirus.jhu.edu/map.html) was not very specific and I don't have money for the google cloud platform for the Google Maps Platform.

Note: The Latitude and Longitude values from the dataset don't accurately represent the location on the map.

Edit 3/23/2020:
LOOKS LIKE THE GUYS AT JOHNHOPKIN'S ACTUALLY DECIDED TO SHOW THE AMOUNT OF PEOPLE INFECTED PER CITY RATHER THAN JUST STATE RENDERING THIS SCRIPT USELESS.

How to use:
1. Download the Kaggle's Novel Corona Virus 2019 Dataset
2. Place the COVID19_open_line_list.csv file in the same directory as this repository
4. pip install these packages openpyxl, pandas, nupy, simplekml 
3. Run Coronavirus_Mapping_kml.py
4. Go to google maps Menu > Your Places > Maps > CREATE MAP > Add layer > Untitled layer > Import
5. Upload the kml files created by the script.

<iframe src="https://www.google.com/maps/d/embed?mid=1ohBdb42Q5zrpkFQYuJaOB5DOPlWR5nL2&hl=en" width="1000" height="1000"></iframe>

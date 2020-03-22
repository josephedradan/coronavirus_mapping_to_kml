"""
3/20/2020

Purpose:
    Make a KML file for the Coronavirus, basically to visualize the virus infected areas base on latitude and longitude
    values.

Reference:
    Python Create Custom KML File Map Layers
        https://www.youtube.com/watch?v=9Hs4uOZGJCA

    A Python library to read/write Excel 2010 xlsx/xlsm files
        https://openpyxl.readthedocs.io/en/stable/

Data:
    Novel Corona Virus 2019 Dataset
        https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#COVID19_open_line_list.csv

How to Use:
    Download the Novel Corona Virus 2019 Dataset
    Open zip file and extract the COVID19_open_line_list.csv
    Save it as an .xlsx file
    Run script

"""
from os import path
from typing import List

import openpyxl
import pandas as pd
import numpy as np
import simplekml

from LatitudeLongitudeContainer import LatitudeLongitudeContainer

# pandas prerequisite
PATH_CSV_FILE = r"COVID19_open_line_list.csv"

# openpyxl prerequisite
OUTPUT_FILE_NAME = "{}".format(path.splitext(__file__)[0])
PATH_EXCEL_FILE = r"COVID19_open_line_list.xlsx"
SHEET_NAME = 'COVID19_open_line_list'

COLUMN_CITY = "D"
COLUMN_PROVINCE = "E"
COLUMN_COUNTRY = "F"

COLUMN_DATE_CONFIRMATION = "M"

COLUMN_LATITUDE = "H"
COLUMN_LONGITUDE = "I"

ROW_START = 2
ROW_END = 13175

# Make the Excel file
pd.read_csv(PATH_CSV_FILE).to_excel(PATH_EXCEL_FILE, sheet_name=SHEET_NAME)

# openpyxl open excel file
WORKBOOK = openpyxl.load_workbook(PATH_EXCEL_FILE)
SHEET = WORKBOOK[SHEET_NAME]


def get_dict_key_tuple_lat_long_value_lat_long_container_pandas():
    data = pd.read_csv(PATH_CSV_FILE)
    df = pd.DataFrame(data)

    dict_temp = {}

    for i, row in df.iterrows():

        """
        row["latitude"].isna() will not work since the return might be a str
        row["latitude"] != "nan" will not work because return might be a float
        row["latitude"] is not "nan" is not correct
        
        np.isnan(row["latitude"]) is correct
        """
        if isinstance(row["latitude"], (float, int)) and isinstance(row["longitude"], (float, int)) and \
                not np.isnan(row["latitude"]) and not np.isnan(row["longitude"]):

            # (lat, long)
            tuple_lat_long_temp = tuple([float(row["latitude"]), float(row["longitude"])])

            # Check if Key (lat, long) Tuple and Value LatitudeLongitudeContainer exist
            if dict_temp.get(tuple_lat_long_temp, False) is False:
                # Create LatitudeLongitudeContainer object
                lat_long_container_temp = LatitudeLongitudeContainer(tuple_lat_long_temp)

                # Set dict key value pair for tuple and LatitudeLongitudeContainer
                dict_temp[tuple_lat_long_temp] = lat_long_container_temp

            # Get value from dict
            lat_long_container_object = dict_temp.get(tuple_lat_long_temp)

            # Increment infected count
            lat_long_container_object.count_infected += 1

            """
            Assigning the the container's values
            
            row["province"].isna() will not work since the return might be a str
            row["city"] != "nan" will not work because return might be a str
            "" if row["city"] is "nan" else row["country"] does not work because nan is not a string
            "" if str(row["city"]) is "nan" else row["country"] does not work because idk
            
            "" if np.isnan(row["city"]) else row["city"] does not work because
            ufunc 'isnan' not supported for the input types, and the inputs could not be safely coerced to any supported 
            types according to the casting rule ''safe''
            
            "" if not isinstance(row["country"], str) else row["country"] works because nan is a float
            """

            lat_long_container_object.country = "" if not isinstance(row["country"], str) else row["country"]
            lat_long_container_object.province = "" if not isinstance(row["province"], str) else row["province"]
            lat_long_container_object.city = "" if not isinstance(row["city"], str) else row["city"]
            lat_long_container_object.set_date_confirmation.add(
                "" if not isinstance(row["date_confirmation"], str) else row["date_confirmation"])

    return dict_temp


def get_dict_key_tuple_lat_long_value_lat_long_container_openpyxl():
    """
    Creates dict using the lat long values as a key in a tuple and a LatitudeLongitudeContainer object as a value

    :return: dict
    """
    dict_temp = {}

    for row_index in range(ROW_START, ROW_END):

        # Lat and Long cells
        cell_lat = "{}{}".format(COLUMN_LATITUDE, row_index)
        cell_long = "{}{}".format(COLUMN_LONGITUDE, row_index)

        # Additional cells
        cell_country = "{}{}".format(COLUMN_COUNTRY, row_index)
        cell_province = "{}{}".format(COLUMN_PROVINCE, row_index)
        cell_city = "{}{}".format(COLUMN_CITY, row_index)
        cell_date_confirmation = "{}{}".format(COLUMN_DATE_CONFIRMATION, row_index)

        # Lat and Long cell values
        cell_lat_value = SHEET[cell_lat].value
        cell_long_value = SHEET[cell_long].value

        # Additional cells values
        cell_country_value = SHEET[cell_country].value
        cell_province_value = SHEET[cell_province].value
        cell_city_value = SHEET[cell_city].value
        cell_date_confirmation_value = SHEET[cell_date_confirmation].value

        if isinstance(cell_lat_value, (float, int)) and isinstance(cell_long_value, (float, int)):

            # (lat, long)
            tuple_lat_long_temp = tuple([cell_lat_value, cell_long_value])

            # Check if Key (lat, long) Tuple and Value LatitudeLongitudeContainer exist
            if dict_temp.get(tuple_lat_long_temp, False) is False:
                # Create LatitudeLongitudeContainer object
                lat_long_container_temp = LatitudeLongitudeContainer(tuple_lat_long_temp)

                # Set dict key value pair for tuple and LatitudeLongitudeContainer
                dict_temp[tuple_lat_long_temp] = lat_long_container_temp

            # Get value from dict
            lat_long_container_object = dict_temp.get(tuple_lat_long_temp)

            # Increment infected count
            lat_long_container_object.count_infected += 1

            # Assigning the the container's values
            lat_long_container_object.country = "" if cell_country_value is None else cell_country_value
            lat_long_container_object.province = "" if cell_province_value is None else cell_province_value
            lat_long_container_object.city = "" if cell_city_value is None else cell_city_value
            lat_long_container_object.set_date_confirmation.add(
                "" if cell_date_confirmation_value is None else cell_date_confirmation_value)

        # print("{:<10}{}, {}".format(row_index, cell_lat_value, cell_long_value))

    return dict_temp


def get_list_from_sorted_dict_key_tuple_lat_long_value_lat_long_container(dict_given: dict):
    """
    Make the dict in to a list and sort it based on the amount of people infected

    :param dict_given: dict
    :return: list
    """
    temp_list = []

    for key, value in dict_given.items():
        temp_list.append(value)

    temp_list.sort(reverse=True)

    # [print(i) for i in temp_list]
    return temp_list


def create_kml(list_given: List[LatitudeLongitudeContainer], name_ending=""):
    kml = simplekml.Kml()

    for container in list_given:
        string_location = "{} {} {}".format(container.country, container.city, container.count_infected)

        # Marker
        point = kml.newpoint(name=string_location)

        # Coordinates
        point.coords = [tuple([container.tuple_lat_long[1], container.tuple_lat_long[0]])]

        # Style (meh...)
        # point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
        # point.style.labelstyle.color = simplekml.Color.red

        # Description
        string_description = "Infected count: {}\n(Lat, Long): {}\nCountry: {}\nCity: {}\nProvince: {}\nDates Confirmed: {}".format(
            container.count_infected,
            container.tuple_lat_long,
            container.country,
            container.city,
            container.province,
            ", ".join(str(i) for i in list(container.set_date_confirmation))
        )

        # Tags via snippet (I don't think this works)
        point.snippet.context = string_location
        point.snippet.maxlines = 1

        # Marker description
        point.description = string_description

    # Save file
    kml.save("{}{}.kml".format(OUTPUT_FILE_NAME, name_ending))


if __name__ == '__main__':
    # Get dict
    dict_temp_pandas = get_dict_key_tuple_lat_long_value_lat_long_container_pandas()
    dict_temp_openpyxl = get_dict_key_tuple_lat_long_value_lat_long_container_openpyxl()

    # Get dict to list
    list_temp_pandas = get_list_from_sorted_dict_key_tuple_lat_long_value_lat_long_container(dict_temp_pandas)
    list_temp_openpyxl = get_list_from_sorted_dict_key_tuple_lat_long_value_lat_long_container(dict_temp_openpyxl)

    # Create kml file
    create_kml(list_temp_pandas, "_pandas")
    create_kml(list_temp_openpyxl, "_openpyxl")

    print("Done!")

"""Module to clean assignment data"""

import os
import re
import argparse
import pandas as pd
import numpy as np
from pandas import DataFrame


def load_data():
    """
    This function is responsible for loading the raw data,
    applying the correct split and tranforming it to a pandas dataframe

    return: eu_life_expectancy_raw_dataframe -> pandas dataframe
    """

    #Get parent directory
    parent_directory = os.path.dirname(__file__)
    raw_data_file_path = '/data/eu_life_expectancy_raw.tsv'

    #Read tsv file
    file_with_split_lines = []
    with open(parent_directory + raw_data_file_path,
              encoding="utf-8") as file:

        #Get list of file delimiters
        delimiters = [',', '\\time\t', '\t', '\n']
        delimiters_pattern = '|'.join(map(re.escape, delimiters))

        #Split file line by line
        for line in file:
            splitted_line = re.split(delimiters_pattern, line)
            file_with_split_lines.append(splitted_line[:-1]) #Exclude \n last split

    #Create pandas dataframe
    eu_life_expectancy_raw_dataframe = pd.DataFrame(data = file_with_split_lines[1:],
                                               columns = file_with_split_lines[0])


    return eu_life_expectancy_raw_dataframe

def clean_data(
    raw_dataframe: DataFrame,
    country: str = 'PT'
):
    """
    This function takes the raw data as a pandas dataframe
    and returns the cleaned data as a pandas dataframe

    param: raw_dataframe -> raw data
    param: country -> region to filter data by

    return: clean_dataframe -> clean data
    """

    #Unpivot dataframe
    unpivoted_dataframe = pd.melt(raw_dataframe,
                                  id_vars = ['unit','sex','age',"geo"],
                                  var_name = 'year',
                                  value_name = 'value')

    #Set and check data types
    dataframe_correct_dtypes = unpivoted_dataframe
    #Cast year column as integer
    dataframe_correct_dtypes['year'] = dataframe_correct_dtypes['year'].astype('int')
    #Cast value column as float
    dataframe_correct_dtypes['value'] = dataframe_correct_dtypes['value'].str.split(' ').str[0]
    #Deal with null values
    dataframe_correct_dtypes['value'] = dataframe_correct_dtypes['value'].replace({':': -1, ': ': -1})
    dataframe_correct_dtypes['value'] = dataframe_correct_dtypes['value'].astype('float')
    dataframe_correct_dtypes = dataframe_correct_dtypes[dataframe_correct_dtypes['value'] != -1]
    #Rename columns
    dataframe_correct_dtypes.columns = ['unit', 'sex', 'age', 'region', 'year', 'value']

    #Filter by region
    clean_dataframe = dataframe_correct_dtypes[dataframe_correct_dtypes['region'] == country]

    return clean_dataframe

def save_data(
    clean_dataframe: DataFrame,
):
    """
    This function saves the final dataframe in the desired path
    param: clean_dataframe -> Cleaned pandas dataframe
    """

    #Get parent directory
    parent_directory = os.path.dirname(__file__)
    save_data_path = '/data/pt_life_expectancy.csv'

    clean_dataframe.to_csv(parent_directory + save_data_path,
                           index = False)

def main(country : str = 'PT'):
    """
    This function should load the data, clean it and save it

    param: country -> region to filter the data by
    """
    raw_dataframe = load_data()
    clean_dataframe = clean_data(raw_dataframe = raw_dataframe,
                                 country = country)
    save_data(clean_dataframe = clean_dataframe)



if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser(description='Find EU life Expectancy for country/region')
    parser.add_argument('-c', '--country', type=str,
                        help='Country to choose')

    args = parser.parse_args()
    main(args.country)

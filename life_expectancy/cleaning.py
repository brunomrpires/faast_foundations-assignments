"""Module to clean assignment data"""
import os
import re
import argparse
import pandas as pd
from pandas import DataFrame


def load_raw_data(
    raw_data_file_path: str
):
    """
    This function is responsible for loading the raw data,
    applying the correct split and tranforming it to a pandas dataframe

    param: raw_data_file_path -> path to the raw data file

    return: Pandas dataframe with columns properly defined
    """
    os_path_pardir = os.path.dirname(__file__)

    #Read tsv file
    splitted_file = []
    with open(os_path_pardir + raw_data_file_path, encoding="utf-8") as file:
        delimiters = ',', '\\time\t', '\t', '\n'
        regex_pattern = '|'.join(map(re.escape, delimiters))
        #Read first line
        for line in file:
            splitted_line = re.split(regex_pattern,line)
            splitted_file.append(splitted_line[:-1])

    eu_life_expectancy_raw_data = pd.DataFrame(splitted_file[1:], columns = splitted_file[0])


    return eu_life_expectancy_raw_data



def unpivot_date(
    raw_dataframe: DataFrame
):
    """
    This function unpivots the date to long format so that
    the dataframe has the following columns: unit, sex, age, region, year, value

    param: raw_dataframe -> raw pandas DataFrame with pivoted date column

    return: pandas dataframe with date column unpivoted
    """
    #unpivoted_dataframe = pd.melt(raw_dataframe, id_vars='year')


    unpivoted_dataframe = pd.melt(raw_dataframe,
                                id_vars=['unit','sex','age',"geo"],
                                var_name='year',
                                value_name = 'value')


    return unpivoted_dataframe

def set_and_check_data_types(
    unpivoted_dataframe: DataFrame
):
    """
    This function sets each columns datatypes according to the assignments specs and scheck them

    param: unpivoted_dataframe -> pandas DataFrame after unpivotting date column

    return: pandas dataframe with columns in the correct data type
    """

    data_types_dataframe = unpivoted_dataframe

    #Cast year column as integer
    data_types_dataframe['year'] = data_types_dataframe['year'].astype('int')

    #Cast value column as float (deal with null values)
    data_types_dataframe['value'] = data_types_dataframe['value'].str.split(' ').str[0]

    data_types_dataframe['value'] = data_types_dataframe['value'].replace({':': 0, ': ': 0})
    data_types_dataframe['value'] = data_types_dataframe['value'].astype('float')
    data_types_dataframe = data_types_dataframe[data_types_dataframe['value'] != 0]

    data_types_dataframe.columns = ['unit', 'sex', 'age', 'region', 'year', 'value']

    return data_types_dataframe

def filter_by_region(
    all_regions_dataframe: DataFrame,
    region: str
):
    """
    This function filters the provided dataframe by the specified region

    :param all_regions_dataframe -> dataframe with every region's data
    :param region -> region to filter the data by

    return region_filtered_dataframe -> dataframe filtered by region
    """

    region_filtered_dataframe = all_regions_dataframe[all_regions_dataframe['region'] == region]

    return region_filtered_dataframe

def save_data(
    filtered_dataframe: DataFrame,
    safe_path: str
):
    """
    This function saves the final dataframe in the desired path
    """
    os_path_pardir = os.path.dirname(__file__)

    filtered_dataframe.to_csv(os_path_pardir + safe_path, index = False)

def clean_data(country: str = 'PT'):
    """
    This function performs the full data cleaning process
    """
    raw_data_file_path = '/data/eu_life_expectancy_raw.tsv'
    final_data_file_path = '/data/pt_life_expectancy.csv'
    raw_dataframe = load_raw_data(raw_data_file_path)

    unpivoted_dataframe = unpivot_date(raw_dataframe)

    data_types_dataframe = set_and_check_data_types(unpivoted_dataframe)

    region_diltered_dataframe = filter_by_region(data_types_dataframe, region = country)

    save_data(region_diltered_dataframe, final_data_file_path)


if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser(description='Find EU life Expectancy for country/region')
    parser.add_argument('-c', '--country', type=str,
                        help='Country to choose')

    args = parser.parse_args()
    clean_data(args.country)

"""Module to load and save data"""

import os
import re
import pandas as pd
from pandas import DataFrame


def load_data(file_path: str):
    """
    This function is responsible for loading the raw data,
    applying the correct split and tranforming it to a pandas dataframe

    return: eu_life_expectancy_raw_dataframe -> pandas dataframe
    """

    #Read tsv file
    file_with_split_lines = []
    with open(file_path,
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


def save_data(
    clean_dataframe: DataFrame,
    file_path: str
):
    """
    This function saves the final dataframe in the desired path
    param: clean_dataframe -> Cleaned pandas dataframe
    param: file_path -> output file path
    """

    clean_dataframe.to_csv(file_path,
                           index = False)

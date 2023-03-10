"""Module to load and save data"""
from abc import ABC
import json
import re
import pandas as pd
from pandas import DataFrame

from life_expectancy.env_variables import JSON_FILE_PATH, CSV_FILE_PATH, SAVE_FILE_PATH_JSON

class DataLoader(ABC):
    """Loads data from specific file extensions"""
    def __init__(self,
                 file_path:str
                 ):
        self.file_path = file_path

    def load_data(self):
        """Loads the data into a pandas dataframe"""

    def get_file_path(self) -> str:
        """Gets the file path as str"""
        return self.file_path

class CSVDataLoader(DataLoader):
    """Loads the data froma .csv file"""
    def __init__(self,
                 file_path: str = CSV_FILE_PATH
                 ):
        if file_path is None:
            file_path = CSV_FILE_PATH

        super().__init__(file_path)

    def load_data(self):
        """
        This function is responsible for loading the raw data,
        applying the correct split and tranforming it to a pandas dataframe

        return: eu_life_expectancy_raw_dataframe -> pandas dataframe
        """

        #Read tsv file
        file_with_split_lines = []
        with open(self.file_path,
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

class JSONDataLoader(DataLoader):
    """Loads the data from a .json file"""
    def __init__(self,
                 file_path: str = JSON_FILE_PATH
                 ):
        if file_path is None:
            file_path = JSON_FILE_PATH

        super().__init__(file_path)

    def load_data(self) -> pd.DataFrame:
        """Load the data into a pd"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return pd.DataFrame(data)

def save_data(
    clean_dataframe: DataFrame = None,
    file_path: str = SAVE_FILE_PATH_JSON
):
    """
    This function saves the final dataframe in the desired path
    param: clean_dataframe -> Cleaned pandas dataframe
    param: file_path -> output file path
    """

    clean_dataframe.to_csv(file_path,
                           index = False)

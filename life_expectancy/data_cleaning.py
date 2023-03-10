"""Module to clean assignment data"""
from abc import ABC
import pandas as pd
from life_expectancy.loading_saving import DataLoader, CSVDataLoader, JSONDataLoader
from life_expectancy.country import Country

class DataCleaner(ABC):
    """
    Data Cleaner class responsible for cleaning several
    types of data objects
    """
    def __init__(self,
                 file_path : str = None
                 ) -> None:
        self.dataloader = DataLoader(file_path)

    def clean_data(self,
                   data: pd.DataFrame,
                   country : Country
                   ) -> pd.DataFrame:
        """
        Cleans data
        Args:
            country (Country): name of country to filter data
            data (pd.DataFrame): data object
        Returns:
            pd.DataFrame: cleaned final pandas dataframe
        """

    def load_data(self) -> pd.DataFrame:
        """Loads the data from file
        Returns:
            pd.DataFrame: dataframe with loaded data
        """
        return self.dataloader.load_data()

    @staticmethod
    def check_country_exists(country: str) -> bool:
        """Test if the country receives is possible
        Args:
            country (Country): Country received
        Returns:
            bool: True or false based on if it exists
        """
        if country.upper() in Country.__members__:
            return True
        return False

class CSVDataCleaner(DataCleaner):
    """Reads data from .csv file and cleans it"""

    def __init__(self,
                 file_path : str=None
                 ) -> None:

        super().__init__(file_path)
        self.loader = CSVDataLoader(file_path)

    def clean_data(self,
                   data: pd.DataFrame,
                   country: Country = 'PT'
                   ) -> pd.DataFrame:
        """
        This function takes the raw data as a pandas dataframe
        and returns the cleaned data as a pandas dataframe

        param: raw_dataframe -> raw data
        param: country -> region to filter data by

        return: clean_dataframe -> clean data
        """

        #Unpivot dataframe
        unpivoted_dataframe = pd.melt(data,
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
        dataframe_correct_dtypes['value'] = dataframe_correct_dtypes['value'].replace({':': -1,
                                                                                    ': ': -1})
        dataframe_correct_dtypes['value'] = dataframe_correct_dtypes['value'].astype('float')
        dataframe_correct_dtypes = dataframe_correct_dtypes[dataframe_correct_dtypes['value'] != -1]
        #Rename columns
        dataframe_correct_dtypes.columns = ['unit', 'sex', 'age', 'region', 'year', 'value']

        #Filter by region
        clean_dataframe = dataframe_correct_dtypes[dataframe_correct_dtypes['region'] == country]

        clean_dataframe = clean_dataframe.reset_index(drop=True)

        clean_dataframe = clean_dataframe.astype({
                'unit':'object',
                'sex':'object',
                'age':'object',
                'region':'object',
                'year':'int64',
                'value':'float64'
                })

        return clean_dataframe

class JSONDataCleaner(DataCleaner):
    """
        This function takes the raw data as a pandas dataframe
        and returns the cleaned data as a pandas dataframe

        param: raw_dataframe -> raw data
        param: country -> region to filter data by

        return: clean_dataframe -> clean data
        """

    def __init__(self,
                 file_path : str=None
                 ) -> None:

        super().__init__(file_path)
        self.loader = JSONDataLoader(file_path)

    def clean_data(self,
                   data: pd.DataFrame,
                   country: Country = None
                   ) -> pd.DataFrame:

        data = data.rename(columns={'country': 'region', 'life_expectancy': 'value'})
        data = data.drop(columns=['flag', 'flag_detail'])

        if country is not None:
            data = data.loc[data.region.str.upper() == country.upper()]

        return data

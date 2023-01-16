"""Module to clean assignment data"""
import os
import pandas as pd
from pandas import DataFrame

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

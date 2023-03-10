"""Tests for the loading_saving module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.data_cleaning import CSVDataCleaner
from life_expectancy.loading_saving import save_data
from life_expectancy.env_variables import  CSV_TEST_FILE_PATH


def test_load_data_csv(eu_life_expectancy_loaded_dataframe_test_csv):
    """Test the load_data method that loads the raw test dataframe"""

    data_loader = CSVDataCleaner(file_path=CSV_TEST_FILE_PATH)
    data = data_loader.loader.load_data()

    pd.testing.assert_frame_equal(
        data, eu_life_expectancy_loaded_dataframe_test_csv
    )

@patch("life_expectancy.loading_saving.pd.DataFrame.to_csv", autospec=True)
def test_save_data_csv(mock_save_data):
    """Test the save_data method by testing the call to the to_csv function using mock info"""

    mock_df = pd.DataFrame({'mock_col':['mock_value_1','mock_value_2']})
    mock_path = 'mock_output_file_path.csv'

    save_data(mock_df, mock_path)

    mock_save_data.assert_called()

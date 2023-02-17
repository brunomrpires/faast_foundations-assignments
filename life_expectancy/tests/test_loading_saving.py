"""Tests for the loading_saving module"""
from unittest.mock import patch
import pandas as pd

from life_expectancy.loading_saving import load_data, save_data
from . import FIXTURES_DIR


def test_load_data(eu_life_expectancy_loaded_dataframe_test):
    """Test the load_data method that loads the raw test dataframe"""

    loaded_test_data = load_data(file_path=FIXTURES_DIR / 'eu_life_expectancy_raw_test.tsv')

    pd.testing.assert_frame_equal(
        loaded_test_data, eu_life_expectancy_loaded_dataframe_test
    )

@patch("life_expectancy.loading_saving.pd.DataFrame.to_csv", autospec=True)
def test_save_data(mock_save_data):
    """Test the save_data method by testing the call to the to_csv function using mock info"""

    mock_df = pd.DataFrame({'mock_col':['mock_value_1','mock_value_2']})
    mock_path = 'mock_output_file_path.csv'

    save_data(mock_df, mock_path)

    mock_save_data.assert_called()

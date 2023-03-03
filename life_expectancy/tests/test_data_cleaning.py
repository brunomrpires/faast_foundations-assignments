"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.data_cleaning import CSVDataCleaner
from life_expectancy.env_variables import  CSV_TEST_FILE_PATH


def test_clean_data(
    pt_life_expectancy_expected_test_csv
    ):
    """Test the `clean_data` function and compare the output to the expected output"""

    cleaner = CSVDataCleaner(CSV_TEST_FILE_PATH)
    raw_dataframe = cleaner.loader.load_data()
    cleaned_dataframe_test = cleaner.clean_data(data=raw_dataframe)

    pd.testing.assert_frame_equal(
        cleaned_dataframe_test, pt_life_expectancy_expected_test_csv
    )

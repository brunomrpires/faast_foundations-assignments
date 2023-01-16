"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.data_cleaning import clean_data
from . import FIXTURES_DIR


def test_clean_data(
    eu_life_expectancy_loaded_dataframe_test,
    pt_life_expectancy_expected_test
    ):
    """Test the `clean_data` function and compare the output to the expected output"""

    cleaned_dataframe_test = clean_data(eu_life_expectancy_loaded_dataframe_test)

    print(cleaned_dataframe_test.shape)
    print(cleaned_dataframe_test.index)
    print(pt_life_expectancy_expected_test.shape)
    print(pt_life_expectancy_expected_test.index)

    pd.testing.assert_frame_equal(
        cleaned_dataframe_test, pt_life_expectancy_expected_test
    )

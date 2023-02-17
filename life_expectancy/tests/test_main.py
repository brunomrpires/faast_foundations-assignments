"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.main import main
from . import FIXTURES_DIR
from pytest import MonkeyPatch


def test_main(monkeypatch: MonkeyPatch, pt_life_expectancy_expected_test):
    """Run the `clean_data` function and compare the output to the expected output"""

    monkeypatch.setattr( "life_expectancy.loading_saving.save_data", 
                        lambda _ : print('MOCK SAVE')
                        )
    monkeypatch.setattr( "life_expectancy.loading_saving.load_data", 
                        lambda  : pd.read_csv(FIXTURES_DIR/'eu_life_expectancy_loaded_dataframe_test.csv')
                        )

    pt_life_expectancy_obtained_test = main(
        country='PT',
        input_file_path=FIXTURES_DIR / "eu_life_expectancy_raw_test.tsv",
        output_file_path=FIXTURES_DIR / 'pt_life_expectancy_obtained_test.csv'
    )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained_test, pt_life_expectancy_expected_test
    )
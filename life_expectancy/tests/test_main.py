"""Tests for the cleaning module"""
import pandas as pd
from pytest import MonkeyPatch
from life_expectancy.main import main
from life_expectancy.file_extension import FileExtension
from life_expectancy.env_variables import SAVE_TEST_FILE_PATH_CSV, SAVE_TEST_FILE_PATH_JSON
from life_expectancy.env_variables import CSV_TEST_FILE_PATH, JSON_TEST_FILE_PATH
from . import FIXTURES_DIR


def test_main_csv(monkeypatch: MonkeyPatch, pt_life_expectancy_expected_test_csv):
    """Run the `clean_data` function for a original csv file
    and compare the output to the expected output"""

    monkeypatch.setattr( "life_expectancy.loading_saving.save_data",
                        lambda _ : print('MOCK SAVE')
                        )
    monkeypatch.setattr( "life_expectancy.loading_saving.CSVDataLoader.load_data",
                        lambda _ : pd.read_csv(FIXTURES_DIR/
                                              'eu_life_expectancy_loaded_dataframe_test.csv')
                        )

    pt_life_expectancy_obtained_test = main(
        country='PT',
        input_file_path=CSV_TEST_FILE_PATH,
        output_file_path=SAVE_TEST_FILE_PATH_CSV,
        file_extension=FileExtension.CSV
    )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained_test, pt_life_expectancy_expected_test_csv
    )

def test_main_json(monkeypatch: MonkeyPatch, pt_life_expectancy_expected_test_json):
    """Run the `clean_data` function for a original json file
    and compare the output to the expected output"""

    monkeypatch.setattr( "life_expectancy.loading_saving.save_data",
                        lambda _ : print('MOCK SAVE')
                        )
    monkeypatch.setattr( "life_expectancy.loading_saving.CSVDataLoader.load_data",
                        lambda  : pd.read_csv(FIXTURES_DIR/
                                              'eu_life_expectancy_loaded_dataframe_test.csv')
                        )

    pt_life_expectancy_obtained_test = main(
        country='PT',
        input_file_path=JSON_TEST_FILE_PATH,
        output_file_path=SAVE_TEST_FILE_PATH_JSON,
        file_extension=FileExtension.JSON
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained_test, pt_life_expectancy_expected_test_json
    )

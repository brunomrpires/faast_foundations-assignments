"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd

from life_expectancy.main import main
from . import FIXTURES_DIR

def test_main(pt_life_expectancy_expected_test):
    """Run the `clean_data` function and compare the output to the expected output"""

    main(
        country='PT',
        input_file_path=FIXTURES_DIR / "eu_life_expectancy_raw_test.tsv",
        output_file_path=FIXTURES_DIR / 'pt_life_expectancy_obtained_test.csv'
    )

    pt_life_expectancy_obtained_test = pd.read_csv(FIXTURES_DIR/'pt_life_expectancy_obtained_test.csv')

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained_test, pt_life_expectancy_expected_test
    )

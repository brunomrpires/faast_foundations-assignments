"""ENVIRONMENT VARIABLES"""
from pathlib import Path


FIXTURES_DIR = Path(__file__).parent / "tests/fixtures"
OUTPUT_DIR = Path(__file__).parent / "data"

#Path of file to save
SAVE_FILE_PATH = OUTPUT_DIR/"pt_life_expectancy.csv"
SAVE_FILE_PATH_JSON = OUTPUT_DIR/"pt_life_expectancy_obtained_json.csv"
SAVE_TEST_FILE_PATH_JSON = FIXTURES_DIR/"pt_life_expectancy_obtained_test_json.csv"
SAVE_TEST_FILE_PATH_CSV = FIXTURES_DIR/"pt_life_expectancy_obtained_test.csv"

#Path of file to load
CSV_FILE_PATH = OUTPUT_DIR/'eu_life_expectancy_raw.tsv'
JSON_FILE_PATH = OUTPUT_DIR/'eurostat_life_expect.json'

#Path of test file to load
CSV_TEST_FILE_PATH = FIXTURES_DIR/'eu_life_expectancy_raw_test.tsv'
JSON_TEST_FILE_PATH = FIXTURES_DIR/'eurostat_life_expect_test.json'

#Path of test file expected
JSON_EXPECTED_TEST_FILE_PATH = FIXTURES_DIR/"pt_life_expectancy_expected_test_json.csv"
CSV_EXPECTED_FILE_PATH = FIXTURES_DIR/"pt_life_expectancy_expected_test.csv"

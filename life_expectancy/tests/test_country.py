"""Test country function"""
from life_expectancy.data_cleaning import DataCleaner
from life_expectancy.env_variables import  CSV_FILE_PATH

def test_check_country():
    """Test if country Enum only has actual countries"""
    cleaner = DataCleaner(CSV_FILE_PATH)
    country = 'EU28'
    assert not cleaner.check_country_exists(country)
    country = 'EFTA'
    assert not cleaner.check_country_exists(country)
    country = 'PT'
    assert cleaner.check_country_exists(country)
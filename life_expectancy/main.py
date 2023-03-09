"""Module to clean assignment data"""
import os
import argparse
from life_expectancy.data_cleaning import JSONDataCleaner, CSVDataCleaner
from life_expectancy.loading_saving import save_data
from life_expectancy.country import Country
from life_expectancy.file_extension import FileExtension
from life_expectancy.env_variables import SAVE_FILE_PATH, CSV_FILE_PATH


def main(
    country : str = Country.PT.value,
    input_file_path: str = None,
    output_file_path: str = None,
    file_extension: FileExtension = FileExtension.JSON
):
    """
    This function should load the data, clean it and save it

    param: country -> region to filter the data by
    """

    if file_extension == FileExtension.CSV:
        cleaner = CSVDataCleaner(input_file_path)
    elif file_extension == FileExtension.JSON:
        cleaner = JSONDataCleaner(input_file_path)

    raw_dataframe = cleaner.loader.load_data()
    clean_dataframe = cleaner.clean_data(country=country,
                                         data=raw_dataframe)

    save_data(
        clean_dataframe = clean_dataframe,
        file_path=output_file_path
    )

    return clean_dataframe

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser(description='Find EU life Expectancy for country/region')
    parser.add_argument(
        '-c',
        '--country',
        required=False,
        default="PT",
        type=str,
        help='Country to choose'
        )
    parser.add_argument(
        '-in',
        "--input_file_name",
        type=str,
        required=False,
        help="input file name",
    )
    parser.add_argument(
        '-out',
        "--output_file_name",
        type=str,
        required=False,
        help="output file name",
    )

    args = parser.parse_args()

    parent_directory = os.path.dirname(__file__)

    main(
        country=args.country,
        input_file_path=CSV_FILE_PATH,
        output_file_path=SAVE_FILE_PATH
    )

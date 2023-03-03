"""Module to clean assignment data"""
import os
import argparse
from .data_cleaning import clean_data
from .loading_saving import load_data, save_data


def main(
    country : str,
    input_file_path: str,
    output_file_path: str
):
    """
    This function should load the data, clean it and save it

    param: country -> region to filter the data by
    """
    raw_dataframe = load_data(file_path=input_file_path)
    clean_dataframe = clean_data(
        raw_dataframe = raw_dataframe,
        country = country
        )

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
        input_file_path=parent_directory + '/data/' + args.input_file_name,
        output_file_path=parent_directory + '/data/' + args.output_file_name
    )

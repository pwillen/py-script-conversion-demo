"""
conversion_demo.py
A Script to Demo File Conversions and Preston's Coding Structure
Author: Preston Gerritsen-Willen
"""

import os
from typing import Optional

import pandas as pd
from pandas import DataFrame


# Adding *args and **kwargs since I'm basically wrapping the pandas function
def convert_df_to_csv(
        df: DataFrame,
        file_path: Optional[str] = None,
        *args,
        **kwargs
) -> str | None:
    """
    A Function to Convert Pandas Dataframe to CSV
    :param df: Pandas DataFrame
    :param file_path: Output Path to Write CSV Directly to
    :return: Either Write to File or Return CSV String
    """

    # Supplying File Path Allows the Function to Skip the Return
    if file_path:
        df.to_csv(*args, **kwargs)
    else:
        return df.to_csv(*args, **kwargs)


# Adding *args and **kwargs since I'm basically wrapping the pandas function
def convert_xml_to_df(
        file_path: str,
        *args,
        **kwargs
) -> DataFrame:
    """
    A Function to Convert xml to Pandas Dataframe
    :param file_path: File Path to Read XML from
    :return: Pandas Dataframe
    """

    # Note pandas.read_xml() Accepts XML as String Unlike pandas.read_csv
    # Otherwise I Would Implement os.path.isfile checks
    return pd.read_xml(file_path, *args, **kwargs)


def main():

    # Filenames
    xml_filename = 'example.xml'
    output_csv_name = 'example.csv'

    # Pathing Setup
    demo_directory = 'data'
    xml_file_path = os.path.join(demo_directory, xml_filename)
    output_csv_path = os.path.join(demo_directory, output_csv_name)

    df = convert_xml_to_df(xml_file_path)

    csv_str = convert_df_to_csv(df, index=False)
    with open(output_csv_path, 'w') as f:
        f.write(csv_str)
    convert_df_to_csv(df, output_csv_path, index=False)


if __name__ == "__main__":

    main()
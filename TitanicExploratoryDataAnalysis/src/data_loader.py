"""
data_loader.py
This module contains methods to load and display infos for CSV data
"""

import pandas as pd

def load_data(file_path: str):
    """
    Loads a CSV file as a Pandas DataFrame.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame | None
        Loaded data or None if an error occurs.

    Notes
    -----
    - Removes leading/trailing whitespaces
    - Catches loading errors
    """
    if not file_path:
        print("Error: The path is invalid")
        return None

    if " " in file_path:
        file_path = file_path.strip()


    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Datei nicht gefunden -> {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Error: Datei konnte nicht geparst werden -> {file_path}")
        return None


def show_info(data_frame: pd.DataFrame):
    """
    Displays basic information about a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be analyzed.

    Returns
    -------
    None
        Prints information about the DataFrame to the console.
    """

    print("--DataFrame Info--\n", data_frame.info())
    print("--Statistic--\n", data_frame.describe())
    print("--Missing values--\n", data_frame.isna().sum())




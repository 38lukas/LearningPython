"""
preprocessing.py
Takes a DataFrame and handles missing values, etc.
"""

import pandas as pd


def refactor(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the DataFrame missing values.

    Parameters
    __________
    data_frame: pd.DataFrame
        The DataFrame to be handled.

    Returns
    __________
    pd.DataFrame
        The cleared DataFrame.
    """

    new_data_frame = data_frame.copy()

    # Refactoring
    new_data_frame["Age"] = new_data_frame["Age"].fillna(0).round().astype(int)
    new_data_frame["Embarked"] = new_data_frame["Embarked"].fillna("missing")
    new_data_frame["Cabin"] = new_data_frame["Cabin"].fillna("missing")
    return new_data_frame

def remove_column(data_frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Removes unused columns

    Parameters
    __________
    data_frame: pd.DataFrame
        The DataFrame to be handled.
    columns: list[str]
        The columns to be removed

    Returns
    __________
    pd.DataFrame
        The cleared DataFrame.
    """

    data_frame = data_frame.copy()
    return data_frame.drop(columns = columns, errors = "ignore")
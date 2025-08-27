"""
plots.py
Utility functions for creating common plots based on a Pandas DataFrame.
Includes validation checks to prevent plotting with invalid inputs.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def create_countplot(data_frame: pd.DataFrame, column: str):
    """
    Create a countplot (frequency plot) for a categorical column.

    Parameters
    ----------
    data_frame : pd.DataFrame
        The DataFrame containing the data.
    column : str
        The column name to plot. Must be categorical or discrete.

    Returns
    -------
    None
        Displays the countplot using matplotlib.
    """
    if not check_validity(data_frame, [column]):
        return

    plt.figure(figsize=(8, 6))
    sns.countplot(data=data_frame, x=column)
    plt.title(f"Count of {column}")
    plt.show()


def create_histplot(data_frame: pd.DataFrame, column: str):
    """
    Create a histogram for a numeric column.

    Parameters
    ----------
    data_frame : pd.DataFrame
        The DataFrame containing the data.
    column : str
        The numeric column name to plot.

    Returns
    -------
    None
        Displays the histogram using matplotlib.
    """
    if not check_validity(data_frame, [column]):
        return

    plt.figure(figsize=(8, 6))
    sns.histplot(data=data_frame, x=column, bins=30)
    plt.title(f"Distribution of {column}")
    plt.show()


def create_barplot(data_frame: pd.DataFrame, columns: list[str]):
    """
    Create a barplot showing the mean of a numeric column grouped by a categorical column.

    Parameters
    ----------
    data_frame : pd.DataFrame
        The DataFrame containing the data.
    columns : list of str
        A list with exactly two elements:
        - The first should be a categorical column (x-axis).
        - The second should be a numeric column (y-axis).

    Returns
    -------
    None
        Displays the barplot using matplotlib.
    """
    if not check_validity(data_frame, columns, True):
        return

    plt.figure(figsize=(8, 6))
    sns.barplot(data=data_frame, x=columns[0], y=columns[1], estimator="mean")
    plt.title(f"Mean of {columns[1]} grouped by {columns[0]}")
    plt.show()


def create_boxplot(data_frame: pd.DataFrame, columns: list[str]):
    """
    Create a boxplot showing the distribution of a numeric column grouped by a categorical column.

    Parameters
    ----------
    data_frame : pd.DataFrame
        The DataFrame containing the data.
    columns : list of str
        A list with exactly two elements:
        - The first should be a categorical column (x-axis).
        - The second should be a numeric column (y-axis).

    Returns
    -------
    None
        Displays the boxplot using matplotlib.
    """
    if not check_validity(data_frame, columns, True):
        return

    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data_frame, x=columns[0], y=columns[1])
    plt.title(f"Distribution of {columns[1]} grouped by {columns[0]}")
    plt.show()


def create_heatmap(data_frame: pd.DataFrame):
    """
    Create a heatmap of the correlation matrix between numeric columns.

    Parameters
    ----------
    data_frame : pd.DataFrame
        The DataFrame containing the data.

    Returns
    -------
    None
        Displays the heatmap using matplotlib.
    """
    if not check_validity(data_frame):
        return

    numeric_columns = data_frame.select_dtypes(include="number")
    if numeric_columns.empty:
        print("Error: No numeric columns available for heatmap")
        return

    plt.figure(figsize=(8, 6))
    sns.heatmap(data=numeric_columns.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation between numeric columns")
    plt.show()


def check_validity(data_frame: pd.DataFrame, columns: list[str] = ["no columns given"], two_columns_needed: bool = False) -> bool:
    """
    Validate that the DataFrame and required columns are suitable for plotting.

    Parameters
    ----------
    data_frame : pd.DataFrame
        The DataFrame to validate.
    columns : list of str, optional
        A list of column names to check. Default is ["no columns given"].
    two_columns_needed : bool, optional
        Whether the function requires exactly two valid columns. Default is False.

    Returns
    -------
    bool
        True if the DataFrame and columns are valid for plotting, False otherwise.
    """
    if data_frame is None or data_frame.empty:
        print("Error: Please provide a valid DataFrame")
        return False

    if not columns:
        print("Error: Column needed")
        return False

    if two_columns_needed and len(columns) != 2:
        print("Error: Type in 2 columns")
        return False

    if columns[0] != "no columns given":
        for column in columns:
            if column not in data_frame.columns.tolist():
                print(f"Error: Column {column} does not exist in given DataFrame")
                return False

    return True

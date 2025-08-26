"""
plots.py
Creating all sorts of plots based on a DataFrame
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def create_histplot(data_frame: pd.DataFrame, categorie: str):

    if not categorie:
        print("Error: Categorie syntax invalid")
        return

    if categorie not in data_frame.columns.tolist():
        print(f"Error: Column {categorie} does not exist in given DataFrame")
        return

    new_data_frame = data_frame.copy()

    sns.histplot(data_frame[categorie], )
    plt.show()

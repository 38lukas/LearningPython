from src import load_data, show_info, refactor, remove_column

def main():

    titanic_df = load_data("data/Titanic-Dataset.csv")
    titanic_df = refactor(titanic_df)
    show_info(titanic_df)

if __name__ == "__main__":
    main()
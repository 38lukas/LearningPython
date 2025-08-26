import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Main:
    @staticmethod
    def learn_numpy():
        # 1
        arr = np.array([4, 8, 15, 16, 23, 42])
        print(arr.mean())

        # 2
        A = np.array([[1, 2, 3],
                      [4, 5, 6]])

        B = np.array([[7, 8],
                      [9, 10],
                      [11, 12]])

        print(A @ B)

        # 3
        arr1 = np.array([5, 10, 15, 20, 25])
        print(arr1.sum(), arr1.std())

        # 4
        arr2 = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

        print(arr2.mean(axis=0))

        # 5
        X = np.array([[2, 0],
                      [1, 3]])

        Y = np.array([[4, 5],
                      [6, 7]])

        print(X @ Y)
        print(X * Y)

    @staticmethod
    def learn_pandas():
        data = {
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 30, 35],
            "City": ["Berlin", "Paris", "London"]
        }

        data_frame = pd.DataFrame(data)
        print(data_frame)

        # Einfaches Ausgeben
        data_frame1 = pd.read_csv("Titanic-Dataset.csv")
        print(data_frame1.columns.tolist(), "\n")
        print(data_frame1.head(5))
        print(data_frame1["Age"])
        print(data_frame1.loc[3, "PassengerId"])
        print(data_frame1.iloc[3, 1])

        #
        print(data_frame1[data_frame1["Age"] > 40])
        print(data_frame1[(data_frame1["Age"] > 40) &  (data_frame1["Sex"] == "male")])

        print(data_frame1.groupby("Sex")["PassengerId"].mean())

        print(data_frame.isnull().sum())

        # 1
        durchschnitts_alter: int = data_frame1["Age"].mean()
        print(durchschnitts_alter)
        #2
        male_count: int = data_frame1[data_frame1["Sex"] == "male"]["Sex"].count()
        female_count: int = data_frame1[data_frame1["Sex"] == "female"]["Sex"].count()
        print(male_count, female_count)
        #or
        print(data_frame1["Sex"].value_counts())
        #3
        durchschnitts_preis = data_frame1.groupby("Pclass")["Fare"].mean()
        print(durchschnitts_preis)
        #4
        data_frame1["Age"] = data_frame1["Age"].fillna(data_frame1["Age"].mean())

        #Bonus
        #1
        fehlende_werte = data_frame1.isnull().sum()
        print(fehlende_werte)
        #2
        print(data_frame1.groupby("Pclass")["Age"].mean())
        #3
        print(data_frame1.groupby(["Pclass", "Sex"])["Fare"].max())

    @staticmethod
    def learn_matplot():
        #1
        x = [1, 2, 3, 4, 5]
        y = x

        plt.plot(x, y)
        plt.xlabel("X-Werte")
        plt.ylabel("Y-Werte")
        plt.show()

        #2
        titanic_df = pd.read_csv("Titanic-Dataset.csv")
        age_column = titanic_df["Age"].dropna()

        plt.hist(age_column, bins=20, color="skyblue", edgecolor= "black")
        plt.xlabel("Alter")
        plt.ylabel("Anzahl der Passagiere")
        plt.title("Verteilung der Altersdaten (Titanic)")
        plt.show()

        #3
        data = titanic_df["Sex"].value_counts()
        beschriftung = ["male", "female"]

        plt.bar(beschriftung, data, color="skyblue", edgecolor="black")
        plt.ylabel("Anzahl der Personen")
        plt.xlabel("Geschlecht")
        plt.title("Anzahl der Personen nach Geschlecht")
        plt.show()

    @staticmethod
    def learn_seaborn():
        titanic_df = pd.read_csv("Titanic-Dataset.csv")

        sns.countplot(data=titanic_df, x="Sex")
        plt.xlabel("Geschlecht")
        plt.ylabel("Anzahl")
        plt.title("Anzahl Männer/Frauen auf der Titanic")
        plt.show()

        numerische_spalten = titanic_df.select_dtypes(include="number")
        corr = numerische_spalten.corr()

        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Korrelationsmatrix der Titanic-Daten")
        plt.show()

        sns.boxplot(data=titanic_df, x="Sex", y="Age")
        plt.title("Verteilung des Alters nach Geschlecht")
        plt.show()

if __name__ == "__main__":
    #Main.learn_numpy()
    #Main.learn_pandas()
    #Main.learn_matplot()
    Main.learn_seaborn()



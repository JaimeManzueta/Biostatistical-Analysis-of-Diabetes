import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import requests

def download(URL, filename):
    response = requests.get(URL)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)



def visualization(values, labels):
    plt.pie(values, labels=labels, autopct="%0.2f%%")
    plt.legend()
    plt.show()
    


def statistical_overview(df):
    print("Dataset Overview:")
    df.info()


    
def correct_the_data(df):
    # Missing values check
    print("\n Missing Values:")
    print(df.isnull().sum())

    # Data types check
    print("\n Data Types:")
    print(df.dtypes)

    # Duplicate rows check
    print("\n Duplicate Rows:")
    print(df.duplicated().sum())





def main():
    Filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

    download(Filename,"Diabetes_Data.csv")
    dataframe = pd.read_csv("Diabetes_Data.csv")
    statistical_overview(dataframe)


    if "Outcome" in dataframe.columns:
        outcome_counts = dataframe["Outcome"].value_counts()
        visualization(outcome_counts.values,outcome_counts.index)
    else:
        print("Outcome column not found")

    correct_the_data(dataframe)






if __name__ == "__main__":
    main()



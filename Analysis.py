import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import requests

def download(URL, filename):
    """Downloads a file from a specified URL and saves it locally."""
    # Send an HTTP GET request to the file URL
    response = requests.get(URL)
    
    # Check if the download was successful (HTTP status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(filename, "wb") as f:
            f.write(response.content)


def visualization(values, labels):
    """Generates and displays a pie chart showing data distribution."""
    # Create a pie chart with percentage formatting up to two decimal places
    plt.pie(values, labels=labels, autopct="%0.2f%%")
    # Add a legend to the chart
    plt.legend()
    # Render the plot on the screen
    plt.show()
    

def statistical_overview(df):
    """Prints a high-level summary and structure of the dataset."""
    print("Dataset Overview:")
    # Display columns, non-null counts, and data types
    df.info()


def main():
    # Define the URL source for the diabetes dataset CSV file
    Filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

    # Step 1: Download the dataset and load it into a pandas DataFrame
    download(Filename, "Diabetes_Data.csv")
    dataframe = pd.read_csv("Diabetes_Data.csv")
    
    # Step 2: Display structural and statistical info about the dataset
    statistical_overview(dataframe)

    # Step 3: Check for the target column ("Outcome") and visualize its breakdown
    if "Outcome" in dataframe.columns:
        # Calculate frequency counts of the outcome categories
        outcome_counts = dataframe["Outcome"].value_counts()
        # Plot the outcome counts as a pie chart
        visualization(outcome_counts.values, outcome_counts.index)
    else:
        print("Outcome column not found")


if __name__ == "__main__":
    main()
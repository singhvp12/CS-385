import pandas as pd

def analyze_data(file_path):
    # Read data from a CSV file into a Pandas DataFrame
    try:
        df = pd.read_csv(file_path)

        # Display basic information about the DataFrame
        print("Data Overview:")
        print(df.info())

        # Display descriptive statistics
        print("\nDescriptive Statistics:")
        print(df.describe())

        # Display the first few rows of the DataFrame
        print("\nFirst Few Rows:")
        print(df.head())

        # Perform additional data analysis as needed

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your CSV file
    csv_file_path = "sample_data.csv"

    # Analyze the data
    analyze_data(csv_file_path)

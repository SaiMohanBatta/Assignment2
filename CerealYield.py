import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew


def read_data(file_path):
    """
    Reads data from a CSV file and returns two dataframes: one with years as
    columns and one with countries as columns.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    Tuple[pd.DataFrame, pd.DataFrame]: DataFrames with different orientations.
    """
    # Load the dataset
    data = pd.read_csv(file_path)

    # Transpose the data 
    t_data = data.T

    # Cleaning the transposed dataframe
    t_data.columns = t_data.iloc[0]
    t_data = t_data.drop(t_data.index[0])

    return data, t_data


def plot_line(data):
    """
    Generate a line plot representing cereal yield from 
    1970 to 2020 for different
    countries. Additionally, prints statistical descriptions of the data.

    Parameters:
    - data (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    None
    """
    # get country codes and years
    country_codes = data['Country Name']
    years = data.columns[1:]

    # Create a line plot
    plt.figure(figsize=(10, 6))
    for idx in range(len(country_codes)):
        plt.plot(years, data.iloc[idx, 1:], label=country_codes[idx])

    # Add plot axis names
    plt.title('Cereal Yield from 1970 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Cereal yield (kg per hectare)')
    plt.legend()
    plt.show()

    # Using statistic methods
    mean_yield = np.mean(data.iloc[:, 1:], axis=0)
    std_yield = np.std(data.iloc[:, 1:], axis=0)
    skewness_yield = skew(data.iloc[:, 1:], axis=1)
    kurtosis_yield = kurtosis(data.iloc[:, 1:], axis=1)

    # using statistical methods
    stats = data.iloc[:, 1:].describe()
    print("\nDescriptive Statistics:\n", stats)
    print("Mean Cereal Yield: ", mean_yield)
    print("Standard Deviation: ", std_yield)
    print("Skewness: ", skewness_yield)
    print("Kurtosis: ", kurtosis_yield)



# calling functions to generate line plot
file_path = 'CerealYield.csv'
data, t_data = read_data(file_path)
plot_line(data)

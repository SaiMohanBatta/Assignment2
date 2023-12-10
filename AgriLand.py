import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew


def read_data(filename):
    
    """
    Reads a dataframe in Worldbank format and returns two dataframes:
    one with years as columns and one with countries as columns.

    Parameters:
    - filename (str): Path to the CSV file containing the dataset.

    Returns:
    - Tuple of two dataframes
    """
    # Load dataset
    data = pd.read_csv(filename, index_col=0)

    # Transpose the data
    df_years = data.transpose()
    df_countries = data

    # Clean dataframes
    df_years = df_years.apply(pd.to_numeric, errors='coerce')
    df_countries = df_countries.apply(pd.to_numeric, errors='coerce',
                                      axis=1)

    return df_years, df_countries


def plot_line(path_to_file):
    """
    Generate a line plot showing agricultural land area trends
    from 1970 to 2020 for multiple countries.

    Parameters:
    - path_to_file (str): Path to the CSV file containing the dataset.

    Returns:
    None
    """
    # Load dataset
    df_y, df_c = read_data(path_to_file)

    # Get country codes and years
    country_codes = df_c.index
    years = df_y.index

    # Describe the dataset for summary statistics
    print("Summary Statistics:")
    print(df_c.describe())

    # Create line plot
    plt.figure(figsize=(10, 6))
    for country_code in country_codes:
        plt.plot(years, df_c.loc[country_code], label=country_code)

    # Add plot title and axis labels
    plt.title('Agricultural land area from 1970 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Agricultural land (% of land area)')

    # Add legend outside plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Display plot
    plt.show()

    # using statistical methods
    print(" Statistics:")
    for country_code in country_codes:
        country_data = df_c.loc[country_code]
        print(f"\nStatistics for {country_code}:")
        print(f"Mean: {np.mean(country_data)}")
        print(f"Median: {np.median(country_data)}")
        print(f"Standard Deviation: {np.std(country_data)}")
        print(f"Kurtosis: {kurtosis(country_data)}")
        print(f"Skewness: {skew(country_data)}")


# Calling function to generate Line Plot
path_to_file = 'AgriLand.csv'
plot_line(path_to_file)

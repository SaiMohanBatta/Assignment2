import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis


def read_data(file_name):
    
    """
    Reads a dataframe in World Bank format and returns two dataframes:
    one with years as columns and one with countries as columns.

    Parameters:
    - file_name (str): The file path of the CSV file.

    Returns:
    Tuple[pd.DataFrame, pd.DataFrame]: Two dataframes.
    """
    # Read the CSV file
    df = pd.read_csv(file_name, index_col='Country Name')

    # DataFrame with years as columns
    y_col = df.copy()

    # DataFrame with countries as columns
    c_col = df.transpose()

    # Cleaning the transposed dataframe
    c_col.index = pd.to_numeric(c_col.index, 
                                errors='coerce')
    c_col.dropna(inplace=True)

    return y_col, c_col


def plot_lifeexp(data):
    
    """
    Plots life expectancy data for multiple countries over the years.

    Parameters:
    - data (dict): Life expectancy data for different countries.

    Returns:
    None
    """
    countries = list(data.keys())
    years = list(data[countries[0]].keys())

    bar_width = 0.1  # Bar thickness

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, year in enumerate(years):
        values = [data[country][year] for country in countries]
        ax.bar([x + i * bar_width for x in range(len(countries))],
               values, width=bar_width, label=year)

    ax.set_xlabel('Countries')
    ax.set_ylabel('Life Expectancy (years)')
    ax.set_title('Life Expectancy at Birth')

    # Center the x-ticks
    ax.set_xticks([i + (len(years) - 1) * bar_width / 2 
                   for i in range(len(countries))])
    ax.set_xticklabels(countries)

    # Adjust legend position
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

    # using statistics methods
    for country in countries:
        values = np.array([data[country][year] for year in years])
        print(f"\nStatistics for {country}:")
        print(pd.DataFrame(values).describe())
        print(f"Skewness: {skew(values)}")
        print(f"Kurtosis: {kurtosis(values)}")
        

# using above functions for the data
file_path = 'LifeExp.csv'
years_df, countries_df = read_data(file_path)
plot_lifeexp(years_df.to_dict(orient='index'))

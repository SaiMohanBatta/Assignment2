import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis


def read_data(file_path):
    
    """
    Read urbanization data from a CSV file and return two dataframes.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - DataFrame: With years as columns.
    - DataFrame: With countries as columns.
    """
    # Read data from CSV
    df = pd.read_csv(file_path, index_col='Country Name')

    # Transpose the dataframe
    df_transposed = df.transpose()
    
    return df, df_transposed


def plot_urbanpop(data):
    
    """
    Plot urbanization rate over years for various countries.

    Parameters:
    - data (dict): Urbanization rate data for countries and years.
    """
    countries = list(data.keys())
    years = list(data[countries[0]].keys())
    bar_width = 0.1

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, year in enumerate(years):
        values = [data[country][year] for country in countries]
        x_positions = [x + i * bar_width for x in range(len(countries))]
        ax.bar(x_positions, values, width=bar_width, label=year)

    ax.set_xlabel('Countries')
    ax.set_ylabel('Urbanization rate')
    ax.set_title('Urbanization Rate Over Years for Countries')
    ax.set_xticks([i + (len(years) - 1) * bar_width / 2 
                   for i in range(len(countries))])
    ax.set_xticklabels(countries)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

    Val_arr = np.array([data[country][year] 
                        for year in years for country in countries])
    print("Descriptive Statistics:")
    print(pd.DataFrame(Val_arr).describe())
    print("\nSkewness:", skew(Val_arr))
    print("Kurtosis:", kurtosis(Val_arr))


# plotting using Data
file_path = 'UrbanPop.csv'
df, df_transposed = read_data(file_path)

# Convert DataFrame to dictionary for plot function
urbanpop_data = df.to_dict(orient='index')
plot_urbanpop(urbanpop_data)

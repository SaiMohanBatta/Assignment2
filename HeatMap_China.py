import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


def plot_heatmap(file_path, indicators):
    
    """
    Generate a correlation heatmap for specified indicators 
    and display descriptive statistics.

    Parameters:
    - file_path (str): The path to the CSV file containing the data.
    - indicators (list): A list of indicators to include in the analysis.

    Returns:
    None
    """
    # Read data from CSV file 
    data = pd.read_csv(file_path)

    # Ensure 'Life Expectancy' is in the list of indicators
    if 'Life Exp' not in data.columns:
        raise ValueError("Column 'Life Exp' not found in the DataFrame.")

    # Extract relevant columns for analysis
    ind_data = data[indicators + ['Life Exp']]

    # Calculate correlation matrix
    corr_mat = ind_data.corr()

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_mat, annot=True, cmap='coolwarm', 
		fmt=".2f", linewidths=.5)
    plt.title('Correlation Heatmap for China')
    plt.show()

    # Describe function using Numpy
    print("\nDescriptive Statistics:")
    print(ind_data.describe())

    # Calculate skewness and kurtosis using Scipy
    print("\nSkewness:")
    for i in indicators:
        skewness = skew(ind_data[i])
        print(f"{i}: {skewness:.4f}")

    print("\nKurtosis:")
    for i in indicators:
        kurt = kurtosis(ind_data[i])
        print(f"{ind_data}: {kurt:.4f}")

#filename of CSV file
file_path = 'ChinaData.csv'

# Specifying the indicators
sel_ind = [
    'Urbanization', 'Cereal Yield', 'Agriculture Land', 
    'Fertilizer Consumption', 'GreenHouse Gas'
]

# Calling the function
plot_heatmap(file_path, sel_ind)

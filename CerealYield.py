import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import describe, pearsonr

def Plot_Line(path_to_file):
    
    # Load the dataset from the CSV file
    data = pd.read_csv(path_to_file)

    # Getting the data of country codes and years
    # Fetched the country codes from the CSV
    country_codes = data['Country Name']
    # The columns of years start from the 3rd column.
    years = data.columns[1:]

    # Create a line plot with multiple lines based on the number of countries
    plt.figure(figsize=(10, 6))
    for idx in range(len(country_codes)):
        # The data of years starts from column 3.
        plt.plot(years, data.iloc[idx, 1:], label=country_codes[idx])

    # Adding plot title and axis labels to append to the graphs.
    plt.title('Cereal Yield from 1970 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Cereal yield (kg per hectare)')

    # Adding legend to the map countrywide
    plt.legend()

    # Display the plot after generating
    plt.show()

    # Statistical Analysis using NumPy and SciPy
    # Calculate mean and standard deviation
    mean_yield = np.mean(data.iloc[:, 1:], axis=0)
    std_yield = np.std(data.iloc[:, 1:], axis=0)

    # Descriptive statistics using SciPy's describe function
    stats_result = describe(data.iloc[:, 1:], axis=1)

    # Calculate correlation coefficient between the first two countries
    country1_yield = data.iloc[0, 1:]
    country2_yield = data.iloc[1, 1:]
    correlation_coefficient, _ = pearsonr(country1_yield, country2_yield)

    # Print the statistical results
    print("Mean Cereal Yield: ", mean_yield)
    print("Standard Deviation of Cereal Yield: ", std_yield)
    print("Descriptive Statistics: ", stats_result)
    print("Correlation Coefficient between Country 1 and Country 2: ", correlation_coefficient)

# Calling the function to generate the Line Plot
path_to_file = 'CerealYield.csv'
Plot_Line(path_to_file)

import pandas as pd
import matplotlib.pyplot as plt

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


# Calling the function to generate the Line Plot
path_to_file = 'CerealYield.csv'
Plot_Line(path_to_file)

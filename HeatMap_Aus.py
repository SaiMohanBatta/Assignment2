import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def Plot_Heatmap(file_path, indicators):
    
    # Read data from CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Ensure 'Life Expectancy' is in the list of indicators
    if 'Life Exp' not in data.columns:
        raise ValueError("Column 'Life Exp' not found in the DataFrame.")

    # Extract relevant columns for correlation analysis
    indicators_data = data[indicators + ['Life Exp']]  # Include 'Life Expectancy' in the list

    # Calculate correlation matrix
    correlation_matrix = indicators_data.corr()

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Heatmap for Australia')
    plt.show()

# Replace 'your_data.csv' with the actual filename or path to your CSV file
file_path = 'AusData.csv'

# Specify the indicators of interest
selected_indicators = ['Urbanization', 'Cereal Yield', 'Agriculture Land', 'Fertilizer Consumption', 'GreenHouse Gas']

# Call the function to generate the heatmap
Plot_Heatmap(file_path, selected_indicators)

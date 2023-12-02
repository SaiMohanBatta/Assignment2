import pandas as pd
import matplotlib.pyplot as plt

def plot_LifeExp(data):
    countries = list(data.keys())
    years = list(data[countries[0]].keys())
    
    bar_width = 0.1  # Adjust this value to make bars thinner or thicker
    
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size as needed
    
    for i, year in enumerate(years):
        values = [data[country][year] for country in countries]
        # Offset the bars for each year to avoid overlap
        ax.bar([x + i * bar_width for x in range(len(countries))], values, width=bar_width, label=year)

    ax.set_xlabel('Countries')
    ax.set_ylabel('Life Expectancy(total years')
    ax.set_title('Life Expetency at Birth')
    
    # Center the x-ticks under each group of bars
    ax.set_xticks([i + (len(years) - 1) * bar_width / 2 for i in range(len(countries))])
    ax.set_xticklabels(countries)
    
    # Move legend outside the plot area
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

# Read data from CSV
file_path = 'LifeExp.csv'
LifeExp_data = pd.read_csv(file_path, index_col='Country Name').to_dict(orient='index')

# Plotting the data with a larger figure size and adjusted legend position
plot_LifeExp(LifeExp_data)

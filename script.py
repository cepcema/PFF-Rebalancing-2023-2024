import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib.dates import MonthLocator, DayLocator, DateFormatter

# Read the CSV file into a DataFrame
file_path = r'C:\Users\qvor_\Desktop\Rebalance\PFF_historical_data_03_2023_03_2024.csv'
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a folder to save the output graphs
output_folder = r'C:\Users\qvor_\Desktop\Rebalance\output_graphs'
os.makedirs(output_folder, exist_ok=True)

# Iterate over unique symbols in the DataFrame
for symbol in df['Symbol'].unique():
    # Filter the DataFrame for the current symbol
    df_symbol = df[df['Symbol'] == symbol]

    # Fit the linear regression model for the current symbol
    X = df_symbol[['Volume']]
    y = df_symbol['Adj Close']
    model = LinearRegression().fit(X, y)

    # Plotting
    fig, ax1 = plt.subplots(figsize=(15, 5))  # Set the figure size to 15:5

    # Plot adjusted close prices
    ax1.plot(df_symbol['Date'], df_symbol['Adj Close'], color='blue', alpha=0.5, label="Close Price")
    ax1.set_ylabel('Close Price', color='blue')

    # Create a secondary y-axis for volume
    ax2 = ax1.twinx()
    ax2.plot(df_symbol['Date'], df_symbol['Volume'], color='orange', alpha=0.5, label="Volume")
    ax2.set_ylabel('Volume', color='orange')

    # Add red dots at specified dates with corresponding labels
    red_dot_dates = pd.to_datetime(['2024-02-29','2024-01-31', '2023-12-29', '2023-11-30',
                                    '2023-10-31', '2023-09-29', '2023-08-31', '2023-07-31',
                                    '2023-06-30', '2023-05-31', '2023-04-28', '2023-03-31'])

    red_dot_indices = [idx for idx, date in enumerate(df_symbol['Date']) if date in red_dot_dates]

    # Plot red dots at specified indices with legend and corresponding labels
    ax1.scatter(df_symbol['Date'].iloc[red_dot_indices], df_symbol['Adj Close'].iloc[red_dot_indices], color='red', label='Rebalance Dates', zorder=5)
    for i, idx in enumerate(red_dot_indices):
        ax1.annotate(f'{df_symbol["Price Change"].iloc[idx]:.2f}', (df_symbol['Date'].iloc[idx], df_symbol["Adj Close"].iloc[idx]), textcoords="offset points", xytext=(0,10), ha='center')

    # Calculate average volume
    avg_volume = df_symbol['Volume'].mean()

    # Plot average volume as a green horizontal line
    ax2.axhline(y=avg_volume, color='green', linestyle='--', label='Average Daily Volume')

    # Add label for average volume number
    ax2.annotate(f'Avg Volume: {avg_volume:.2f}', xy=(0, avg_volume), xytext=(-50, 0), textcoords='offset points', ha='right', va='center', color='green', fontsize=10)

    # Add grid lines only for the primary y-axis and x-axis
    ax1.grid(True)
    ax2.grid(False)  # Disable grid for the secondary y-axis

    # Adjust x-axis ticks to show each month with day and year
    locator_month = MonthLocator()
    locator_day = DayLocator()
    formatter = DateFormatter('%m-%d-%Y')

    ax1.xaxis.set_major_locator(locator_month)
    ax1.xaxis.set_minor_locator(locator_day)
    ax1.xaxis.set_major_formatter(formatter)

    # Set x-axis limits to match the range of dates in the DataFrame
    ax1.set_xlim(df_symbol['Date'].min(), df_symbol['Date'].max())

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.title(f'{symbol} graph')
    
    # Save the output graph in the project folder
    output_path = os.path.join(output_folder, f'{symbol}_graph.png')
    plt.savefig(output_path)
    plt.close()  # Close the figure to release memory
    
    print(f"Graph saved as '{output_path}'")

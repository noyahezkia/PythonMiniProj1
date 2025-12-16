import pandas as pd
import matplotlib.pyplot as plt

# Plot a histogram of one column
def plot_column_histogram(dataset, column_name, axes_name, plot_name):
    plt.hist(dataset[column_name], color="pink", edgecolor="black")
    plt.xlabel(axes_name)
    plt.ylabel("Frequency")
    plt.title(plot_name)
    plt.show() 

laptop_data = pd.read_csv("laptop_price - dataset.csv")
price_column = "Price (Euro)"

# Plot a histogram of all the prices
plot_column_histogram(laptop_data, price_column, price_column, "Price Distribution")
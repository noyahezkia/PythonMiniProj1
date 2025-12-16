import pandas as pd
import matplotlib.pyplot as plt

# Plot a histogram of one column distribution
def plot_column_histogram(dataset, column_name, axes_name, plot_name):
    plt.hist(dataset[column_name], color="pink", edgecolor="black")
    plt.xlabel(axes_name)
    plt.ylabel("Frequency")
    plt.title(plot_name)
    plt.show() 

laptop_data = pd.read_csv("laptop_price - dataset.csv")
price_column = "Price (Euro)"
company_column = "Company"

# Plot a histogram of all the prices
plot_column_histogram(laptop_data, price_column, price_column, "Price Distribution")

# Find the average price per company 
avg_price_per_company = (laptop_data.groupby(company_column)[price_column]
                        .mean()
                        .sort_values(ascending=False))

# Find the most expensive company on average
most_expensive_company = avg_price_per_company.idxmax()

print("Most expensive company on average: " + most_expensive_company)
print("Average prices per company:")
print(avg_price_per_company)

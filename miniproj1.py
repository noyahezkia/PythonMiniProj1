import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a histogram of one column distribution
def plot_column_histogram(dataset, column_name, axes_name, plot_name):
    plt.hist(dataset[column_name], color='pink', edgecolor='black')
    plt.xlabel(axes_name)
    plt.ylabel('Frequency')
    plt.title(plot_name)
    plt.show() 

laptop_data = pd.read_csv('laptop_price - dataset.csv')
price_column = 'Price (Euro)'
company_column = 'Company'
os_column = 'OpSys'

# Plot a histogram of all the prices
plot_column_histogram(laptop_data, price_column, price_column, 'Price Distribution')

# Find the average price per company 
avg_price_per_company = (laptop_data.groupby(company_column)[price_column]
                        .mean()
                        .sort_values(ascending=False))

# Find the most expensive company on average
most_expensive_company = avg_price_per_company.idxmax()

print('Most expensive company on average: ' + most_expensive_company)
print('Average prices per company:')
print(avg_price_per_company)

# Uniforming the OS types into a new column (to not override existing data)
laptop_data['UniformOpSys'] = laptop_data[os_column].replace({
    'Mac OS X': 'macOS',
    'Windows 10': 'Windows',
    'Windows 10 S': 'Windows',
    'Windows 7': 'Windows'
})

# Create a list of the unique values (OS types)
unique_os = laptop_data['UniformOpSys'].unique()

print('Operating system types:')
print(*unique_os, sep='\n')

# Plot price distributions for each OS type
# Create a seperate histogram of the prices for each OS type 
subplots_grid = sns.FacetGrid(laptop_data, col='UniformOpSys', col_wrap=3, sharex=False)
subplots_grid.map_dataframe(sns.histplot, x=price_column, color="skyblue", edgecolor="black")
subplots_grid.set_axis_labels(price_column, 'Count')
subplots_grid.set_titles('Price Distribution for {col_name}')
plt.tight_layout()
plt.show()


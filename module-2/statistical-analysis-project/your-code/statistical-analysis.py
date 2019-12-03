#%%
#Import the necessary libraries:
import numpy as np
import pandas as pd
from scipy.stats import ttest_rel
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Exploring data and understanding what the fields mean:
data = pd.read_csv('C:/Users/Ironhack/Documents/Ironhack/Week12/Statistical Analysis Project/train.csv')
data.head()
# %%
data.describe()

# %%
data.shape

# %%
data.dtypes

# %%
# Saving the SalesPrice in a variable to use it along the project:
price = data['SalePrice']

# %%
#Examining the relationships between the sales price and other features in the dataset.
#Using scatter plot to see the relationship between SalesPrice and some numerical fields:
plt.scatter(data['BsmtFinSF1'], price, alpha = .5)
plt.scatter(data['BsmtUnfSF'], price, color = 'red', alpha = .5)
plt.scatter(data['TotalBsmtSF'], price, color = 'green', alpha = .5)

# %%
#Using box to study the SalesPrice field:
price.iplot(kind = 'box')

# %%
#Using bar plot to see the relationship between SalesPrice and some categorical fields:
price_neightborhood = data.pivot_table(
    index = 'Neighborhood',
    values = 'SalePrice',
    aggfunc = 'mean'
)
price_neightborhood.iplot(kind = 'bar')

#%%
quantity_neightborhood = data.pivot_table(
    index = 'Neighborhood',
    values = 'Id',
    aggfunc = 'count'
)
quantity_neightborhood.iplot(kind = 'bar')
#The are more sold houses in NAmes, CollgCr and OldTown,
#but the more expensive neighborhoods are: NoRidges, NridgHt and StoneBr
#with an average between $300 and $350.

# %%
price_condition1 = data.pivot_table(
    index = 'Condition1',
    values = 'SalePrice',
    aggfunc = 'mean'
)
price_condition1.iplot(kind = 'bar')

# %%
quantity_condition1 = data.pivot_table(
    index = 'Condition1',
    values = 'Id',
    aggfunc = 'count'
)
quantity_condition1.iplot(kind = 'bar')

#There are more than 1200 house with Norm as Condition1, 
#but PosA, PosN and RRNn are the most expensive, with an
#average greater than 200K.


# %%
#Data cleaning & manipulation
#Reviewing columns with missing values to drop them:
data.isnull().sum()

# %%
#Removing columns with high proportion of missing values:
data = data.drop(['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'FireplaceQu'], axis=1) 
data.head()

# %%
#Converting categorical data to numerical:
#(Including only the object columns in a new dataframe. 
#Pandas has a helpful select_dtypes function which we can use to build 
# a new dataframe containing only the object columns and SalePrice).
obj_data = data.select_dtypes(include=['object']).copy()
obj_data['Price'] = data['SalePrice']
obj_data.head()  


# %%
#Counting values of Central Air:
obj_data['CentralAir'].value_counts()

# %%
obj_data['CentralAir'] = np.where(obj_data['CentralAir'] == 'Y', 1, 0)

# %%
obj_data['PavedDrive'].value_counts()
obj_data['PavedDrive'] = np.where(obj_data['PavedDrive'] == 'Y', 1, 0)
obj_data.head()

# %%
obj_data['PavedDrive'].dtypes

# %%
# Changing numerical data in original dataframe "data":
data['PavedDrive'] = obj_data['PavedDrive']
data['CentralAir'] = obj_data['CentralAir']

data['PavedDrive'].dtypes
data['CentralAir'].dtypes

# %%
#Before going any further, there are a couple of 
#null values in the data that we need to clean up:
data[data.isnull().any(axis=1)]
data.head() 

# %%
data.shape

#%%
#Selecting feature based on correlation
#Generating the correlation matrix
corr = data.corr()
sns.heatmap(corr)


# %%
#Selected feature: YearBuilt
#Assuming to null hypothesis is "The YearBuilt do not have any effect on # the SalePrice".

sale_price = data['SalePrice']

def decimal_str(x: float, decimals: int = 50) -> str:
    return format(x, f".{decimals}f").lstrip().rstrip('0')

def interpret(alpha, p_val):
    print(f"Probability results occurred by chance: {decimal_str(p_val, 30)}.\nIs our p-value less than the alpha? {'Yes. We reject the null hypothesis!' if p_val < alpha else 'No. Our null hypothesis is correct.'}")
    
alpha = 0.05

expected_mean_table = data.pivot_table(
    index = 'YearBuilt',
    values = 'SalePrice',
    aggfunc = 'sum'
)

year_built_mean = data.groupby('YearBuilt')['SalePrice'].mean()

expected_mean_table.reset_index(0) 
                  
expected_mean = float(expected_mean_table.mean())
                   
p_val = ttest_1samp(
    sale_price,
    expected_mean
)[1]
          
p_val      
          
interpret(alpha, p_val)

#Probability results occurred by chance: 0..
#Is our p-value less than the alpha? 
# Yes. We reject the null hypothesis!


# %%
year_built_mean = data.groupby('YearBuilt')['SalePrice'].mean()
year_built_mean

# %%
year_built_mean.iplot(kind = 'line')

# %%
year_built_mean.iplot(kind = 'hist')

# %%
#Showing the LotArea in the purchased houses are most common in the highest 10 sales:

top_10 = data.sort_values('SalePrice', ascending = False).reset_index().loc[:10]
lot_area = top_10.groupby(['LotArea']).mean().reset_index()
chart = lot_area[['LotArea', 'SalePrice']]

plt.barh(chart['LotArea'], chart['SalePrice'], color = 'green')

# %%
#Showing if is there a significant difference between PavedDrive and CentralAir:
#(Converted data from categorical to numerical above)

paved_drive = data['PavedDrive']
central_air = data['CentralAir']

p_val = ttest_rel(paved_drive, central_air)[1]

print('p_val: ', p_val)

# %%
#p_val is smoller than 0.05: There is no significant difference between those columns.
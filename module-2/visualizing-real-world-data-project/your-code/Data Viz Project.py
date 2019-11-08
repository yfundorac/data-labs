# %%
'''
Trending YouTube Video Statistics - US Videos
https://www.kaggle.com/datasnaek/youtube-new/data
'''
# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import chart_studio.plotly as py
import cufflinks as cf
from ipywidgets import interact
warnings.filterwarnings('ignore')


# %%
data = pd.read_csv('USvideos.csv')

# %%
data.head(5)

# %%
data.describe()

# %%
data.dtypes

# %%
## 10 Top Trending Channels (# of views of videos)

# %%
top_ten = data.groupby('channel_title')['views'].sum().nlargest(10).reset_index()
#top_ten
top_ten.sort_values(by = "views", ascending = True).plot.barh()
#top_ten.sort_values(by = "views", ascending = True).iplot( kind = 'bar')


# %%
## Correlation between views and likes

data.plot(x = 'views', y = 'likes', kind = 'scatter')

# %%
## Summary statistics of views

data.boxplot(column='views')

# %%
by_category = data.groupby('category_id')['dislikes'].sum()
by_category.plot(kind = 'hist')

# %%

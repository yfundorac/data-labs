'''
Trending YouTube Video Statistics - US Videos
https://www.kaggle.com/datasnaek/youtube-new/data
'''

import streamlit as st
import altair as alt
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff


st.title("Data Visualization Project")
st.write("Trending YouTube Video Statistics - US Videos")
st.write("Dataframe:")

data = pd.read_csv('USvideos.csv')

st.write(data[:1000])

st.write("10 Top Trending Channels (# of views of videos)")

top_ten = data.groupby('channel_title')['views'].sum().nlargest(10).reset_index()
st.bar_chart(top_ten)


st.write("Correlation between views and likes")
c = alt.Chart(data[:1000]).mark_circle().encode(x='views', y='likes', size='channel_title', color='channel_title')
st.write(c)

st.write("Summary statistics of views")
views = data[:1000].groupby('views').sum().reset_index()
# data[:1000].boxplot(column='views')
# tips = px.data.tips()
# fig = px.box(tips, y="total_bill")
# fig.show()  
st.line_chart(views)



st.write("Distribution of dislikes by categories  -- Histogram")
by_category = data.groupby('category_id')['dislikes'].sum().reset_index()
st.bar_chart(by_category)


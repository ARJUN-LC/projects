import numpy as np
import pandas as pd
movie=pd.read_csv("movies.dat",delimiter='::')
# print(movie.head())
movie.columns=['id','title','genre']
# print(movie.head())
ratings=pd.read_csv("ratings.dat",delimiter="::")

ratings.columns=['user','id','rating','timestamp']
# print(ratings.head())
data=pd.merge(movie,ratings,on=['id','id'])
# print(data.head())
# ratings=data["rating"].value_counts()
# numbers=ratings.index
# quantity=ratings.values
# import plotly.express as px
# fig = px.pie(data,values=quantity,names=numbers)
# fig.show()
data2=data.query('rating==10')
print(data2['title'].value_counts().head(10))
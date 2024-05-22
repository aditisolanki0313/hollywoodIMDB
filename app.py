import streamlit as st
import pickle
import pandas as pd
import os
file_path = os.path.join('C:\\Users\\aditi\\Downloads\\DA,DS\\movie\\server', 'mo.pkl')
file_path2 = os.path.join('C:\\Users\\aditi\\Downloads\\DA,DS\\movie\\server', 'similarity.pkl')



def recommend(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:6]

    recommended = []  
   
    for i in movie_list:
        recommended.append(movie.iloc[i[0]].title)
    return recommended


movie_dict = pickle.load(open(file_path, 'rb'))
movie = pd.DataFrame(movie_dict)
similarity = pickle.load(open(file_path2, 'rb'))
# movie_dict = pickle.load(open('mo.pkl', 'rb')) 

st.title('Movie Recommendation')
options = st.selectbox(
    "What are your favorite movie",
    movie['title'].values) 


if st.button("Recommend"):
    fav = recommend(options)
    for i in fav:
        st.write(i) 


     



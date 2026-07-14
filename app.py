import streamlit as st
import pickle
import joblib
import nltk
import sklearn
import pandas as pd

st.title("Movie Recommender System!")

with open('movies.pkl', 'rb') as m:
    movies=pickle.load(m)

similarities=joblib.load('similarities.joblib')

def recommend(name_movie):

    movie_index=int(movies[movies['title']==name_movie].index[0])

    recommendations=similarities[movie_index]

    movie_list=sorted(enumerate(recommendations), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

movies_names=movies['title'].values

name_movie=st.selectbox("Enter the Movie name", movies_names)

if st.button("Recommend"):
    recommended_movies=recommend(name_movie)
    st.write("Recommended movies are.")
    for movie in recommended_movies:
        st.write(movie)

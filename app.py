import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=26f79ea3c78de8808738bda241044608&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommdation(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distance = similarity[movie_index]
    #     print(distance)
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    L = []
    recommended_movie_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        L.append(movies.iloc[i[0]].title)
    return L , recommended_movie_posters

st.title("Movie Recommendation System")

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# print(movies)

option = st.selectbox("how would you like to contact?",movies['title'].values)
if st.button("Recommendation"):
    name,poster=recommdation(option)
    col1, col2, col3, col4 ,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])


import streamlit as st
import pickle as pk
import requests

dataset = pk.load(open("dataset.pkl","rb"))
recommender = pk.load(open("similarity_recommender.pkl","rb"))

# import zipfile

# def unzip_file(zip_file_path, extract_to_path):
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to_path)

# # Example usage:
# zip_file_path = 'similarity_recommender.zip'
# extract_to_path = ''

# recommender = unzip_file(zip_file_path, extract_to_path)




def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a716cbb7c501852c46cc1fccaf0784fe")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = dataset[dataset["title"] == movie].index[0]
    distances = recommender[movie_index]
    recommend_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
    movies_list = []
    movies_posters = []

    for i in recommend_movies:
        movies_id = dataset.iloc[i[0]][0]
        movies_list.append(dataset.iloc[i[0]][1])
        # fetch posters from api
        movies_posters.append(fetch_poster(movies_id))
    return movies_list,movies_posters
    




# title
st.title("Movies Recommendation System")
# about app
st.write("You can select 1 movie name at a time. After selecting movie, click on 'Recommend Button'. And then, this app will suggest you 6 movies that are related to your selected movie in term of Hero, Director, overview, tags or content.")
# select-box
movie_name = st.selectbox("Select Movie Name:", dataset["title"].unique())
# 

if st.button("Recommend"):
    name,poster = recommend(movie_name)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{1}. "+name[0])
        st.image(poster[0])
    with col2:
        st.write(f"{2}. "+name[1])
        st.image(poster[1])
    

    col3, col4 = st.columns(2)
    with col3:
        st.write(f"{3}. "+name[2])
        st.image(poster[2])
    with col4:
        st.write(f"{4}. "+name[3])
        st.image(poster[3])

    col5, col6 = st.columns(2)
    with col5:
        st.write(f"{5}. "+name[4])
        st.image(poster[4])
    with col6:
        st.write(f"{6}. "+name[5])
        st.image(poster[5])
    

# About Developer
st.header("About the Developer")
st.write("This app is developed by Abdullah_Khan_Kakar. You can contact me at abdullahkhan4465917@gmail.com")

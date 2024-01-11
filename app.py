import streamlit as st 
import pandas as pd 
import numpy as np
import pickle
import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide"
)

popular_books_df = pd.read_pickle('popular_books_df.pkl')
book_df = pd.read_pickle('book_df.pkl')
similarity_matrix = pd.read_pickle('similarity_matrix.pkl')
sparse_matrix = pd.read_pickle('sparse_matrix.pkl')

def Recommend_Book(Book_Name):
  sparse_matrix_temp = sparse_matrix
  similarity_matrix_temp = similarity_matrix
  book_df_temp = book_df

  Book_Index = np.where(sparse_matrix_temp.index == Book_Name)[0][0]

  similar_books = sorted(list(enumerate(similarity_matrix_temp[Book_Index])), key = lambda x: x[1], reverse=True)[1:11]

  similar_books_detail = []
  for i in similar_books:
    individual_book_details = []
    individual_book_details.append(sparse_matrix_temp.index[i[0]])
    individual_book_details.append(book_df_temp[book_df_temp["Book-Title"] == sparse_matrix_temp.index[i[0]]].drop_duplicates('Book-Title')['Book-Author'].iloc[0])
    individual_book_details.append(book_df_temp[book_df_temp["Book-Title"] == sparse_matrix_temp.index[i[0]]].drop_duplicates('Book-Title')['Image-URL-M'].iloc[0])
    similar_books_detail.append(individual_book_details)

  return similar_books_detail

with st.container(border=True):
    st.title("IntellectuaRead: A Sophisticated Literary Recommendation System")
    st.write("  ")

tab1, tab2 = st.tabs(["Home", "Recommend"])

with tab1:
    st.subheader("Top-20 Popular Books: ")
    st.write(" ")
    a = 0

    
    with st.container(border=True):
        col1 = st.columns(5)
        for i in range(5):
            col1[i].image(popular_books_df["Image-URL-M"].iloc[a])
            col1[i].write(popular_books_df["Book-Title"].iloc[a])
            col1[i].markdown(f'Author : {popular_books_df["Book-Author"].iloc[a]}', unsafe_allow_html=True)
            col1[i].markdown(f'Votes: {popular_books_df["rating_count_per_book"].iloc[a]}')
            col1[i].markdown(f'Ratings: {popular_books_df["mean_rating_per_book"].iloc[a]}')
            a = a+1

        col1 = st.columns(5)
        for i in range(5):
            col1[i].image(popular_books_df["Image-URL-M"].iloc[a])
            col1[i].write(popular_books_df["Book-Title"].iloc[a])
            col1[i].markdown(f'Author : {popular_books_df["Book-Author"].iloc[a]}', unsafe_allow_html=True)
            col1[i].markdown(f'Votes: {popular_books_df["rating_count_per_book"].iloc[a]}')
            col1[i].markdown(f'Ratings: {popular_books_df["mean_rating_per_book"].iloc[a]}')
            a = a+1
    
        col1 = st.columns(5)
        for i in range(5):
            col1[i].image(popular_books_df["Image-URL-M"].iloc[a])
            col1[i].write(popular_books_df["Book-Title"].iloc[a])
            col1[i].markdown(f'Author : {popular_books_df["Book-Author"].iloc[a]}', unsafe_allow_html=True)
            col1[i].markdown(f'Votes: {popular_books_df["rating_count_per_book"].iloc[a]}')
            col1[i].markdown(f'Ratings: {popular_books_df["mean_rating_per_book"].iloc[a]}')
            a = a+1
    
        col1 = st.columns(5)
        for i in range(5):
            col1[i].image(popular_books_df["Image-URL-M"].iloc[a])
            col1[i].write(popular_books_df["Book-Title"].iloc[a])
            col1[i].markdown(f'Author : {popular_books_df["Book-Author"].iloc[a]}', unsafe_allow_html=True)
            col1[i].markdown(f'Votes: {popular_books_df["rating_count_per_book"].iloc[a]}')
            col1[i].markdown(f'Ratings: {popular_books_df["mean_rating_per_book"].iloc[a]}')
            a = a+1

with tab2:
    with st.container(border=True):

        st.markdown("<p style='font-size: 24px;'><b>Fuel your book appetite</b>: Tell us your taste, and we'll fill your reading plate.</p>", 
                    unsafe_allow_html=True)
        selected_book_for_recommendation = st.selectbox(" ", options= list(sparse_matrix.index), index=None, placeholder="Select a book from the list below")


    if selected_book_for_recommendation is not None:

        with st.container(border=True):
            st.subheader("The book you have chosen: ")
            st.image(book_df[book_df["Book-Title"] == selected_book_for_recommendation].drop_duplicates('Book-Title')['Image-URL-M'].iloc[0])
            st.write(selected_book_for_recommendation)
            st.write(book_df[book_df["Book-Title"] == selected_book_for_recommendation].drop_duplicates('Book-Title')['Book-Author'].iloc[0])
            
        recommended_books = Recommend_Book(selected_book_for_recommendation)
        with st.container(border=True):
            st.subheader("Beyond the Appetizer:")

            rec_col = st.columns(5, gap = 'small')
            for i in range(5):
                rec_col[i].image(recommended_books[i][2])
                rec_col[i].write(recommended_books[i][0])
                rec_col[i].write(recommended_books[i][1])
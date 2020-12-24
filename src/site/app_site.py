import requests
import streamlit as st

BASE = "http://127.0.0.1:5000/"


def get_review_sentiment(movie_review):
    st.write('The Entered movie review is ', movie_review)
    with st.spinner('The model is calculating the sentiment'):
        response = requests.put(BASE + 'Review', {movie_review})
    st.text("The sentiment of the review is:")
    if response[0] == 'good':
        st.success(f'{response[0]} with a confidence of{response[1]}')
    else:
        st.error(f'{response[0]} with a confidence of{response[1]}')


def start_site():
    st.title('Movie Reviews Sentiment App')
    movie_review = st.text_area('Enter your movie review here please')
    if st.button("Get Review Sentiment"):
        if not movie_review:
            st.warning('Please input a review.')
            st.stop()
        get_review_sentiment(movie_review)


if __name__ == '__main__':
    start_site()

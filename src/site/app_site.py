import requests
import streamlit as st

BASE = "http://127.0.0.1:5000/"


def get_review_sentiment(movie_review):
    with st.spinner('The model is calculating the sentiment'):
        response = requests.put(BASE + 'Review', {"review": movie_review}).json()
    st.text("The sentiment of the review is:")
    if response['sentiment'] == 'good':
        st.success(f'{response["sentiment"]} with a confidence of {response["confidence"]}')
    else:
        st.error(f'{response["sentiment"]} with a confidence of {response["confidence"]}')


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

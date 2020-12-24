import pytest

from algorithm.data_loader import load_movie_review_data
from algorithm.sentiment_model import SentimentModel


@pytest.fixture()
def test_model():
    return SentimentModel()


@pytest.fixture()
def input_movie_data():
    data = load_movie_review_data(r'C:\School\workspace\SentimentProject\Data')
    return data

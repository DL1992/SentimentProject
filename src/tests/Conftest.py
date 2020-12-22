import pytest

from algorithm.data_loader import load_movie_review_data


@pytest.fixture
def input_value():
    return 39


@pytest.fixture()
def input_movie_data():
    return load_movie_review_data(r'C:\School\workspace\SentimentProject\Data')

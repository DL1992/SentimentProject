# from sklearn.model_selection import train_test_split
import os
# from src.algorithm.data_loader import load_movie_review_data
from algorithm.sentiment_model import SentimentModel


def test_load_movie_review_data(input_movie_data):
    # data = load_movie_review_data(r'C:\School\workspace\SentimentProject\Data')
    assert len(input_movie_data) == 2000


def test_save_model_creates_file():
    model = SentimentModel()
    model.save_model('test_model.joblib')
    assert os.path.isfile(r'test_model.joblib') == True

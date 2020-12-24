import os
import pytest


def test_load_movie_review_data(input_movie_data):
    assert len(input_movie_data.data) == 2000


def test_save_model_creates_file(test_model):
    test_model.save_model('test_model.joblib')
    assert os.path.isfile(r'test_model.joblib')


@pytest.mark.parametrize("test_input_review,expected_sentiment",
                         [(["This is the worst movie i saw, simple bad movie"], 0),
                          (["this is one of the best movies i saw. simple a good movie "], 1)])
def test_sentiment_model_predict(test_model, test_input_review, expected_sentiment):
    test_model.load_model(r'C:\School\workspace\SentimentProject\src\algorithm\my_model')
    assert test_model.predict(test_input_review)[0] == expected_sentiment


@pytest.mark.parametrize("test_input_review,expected_sentiment",
                         [(["This is the worst movie i saw, simple bad movie"], 'bad'),
                          (["this is one of the best movies i saw. simple a good movie "], 'good')])
def test_sentiment_model_predict_sentiment(test_model, test_input_review, expected_sentiment):
    test_model.load_model(r'C:\School\workspace\SentimentProject\src\algorithm\my_model')
    prediction = test_model.predict_sentiment(test_input_review)
    assert prediction['sentiment'] == expected_sentiment
    assert prediction['confidence'] >= 0.5

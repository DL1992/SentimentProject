from algorithm.data_loader import load_movie_review_data


def test_load_movie_review_data():
    data = load_movie_review_data(r'C:\School\workspace\SentimentProject\Data')
    assert len(data.data) == 2000

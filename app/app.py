from flask import Flask, request
from flask_restx import Api, Resource, reqparse

from algorithm.sentiment_model import SentimentModel

app = Flask(__name__)
api = Api(app)

model = SentimentModel()
model.load_model(r'algorithm/my_model.joblib')

reviews_put_args = reqparse.RequestParser()
reviews_put_args.add_argument('review', type=str, help='review must be string')


@api.route('/Review')
class MovieReview(Resource):
    def get(self):
        return {'hello': 'world'}

    def put(self):
        args = reviews_put_args.parse_args()
        review = [args['review']]
        result = model.predict_proba(review)
        return {"good": result[0][0], 'bad': result[0][1]}


if __name__ == '__main__':
    app.run(debug=True)

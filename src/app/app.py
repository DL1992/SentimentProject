from flask import Flask
from flask_restx import Api, Resource, reqparse
from ..algorithm.sentiment_model import SentimentModel

app = Flask(__name__)
api = Api(app)

reviews_put_args = reqparse.RequestParser()

model = SentimentModel()
model.load_model(r'C:\School\workspace\SentimentProject\src\algorithm\my_model')

reviews_put_args.add_argument('review', required=True, type=str, help='review must be string: {error_msg}')


@api.errorhandler(Exception)
def handle_root_exception(error):
    return {'message': f'{error}'}, 400


@api.route('/Review')
class MovieReview(Resource):
    def get(self):
        return {'hello': 'world'}

    @api.expect(reviews_put_args)
    def put(self):
        args = reviews_put_args.parse_args()
        review = [args['review']]
        result = model.predict_proba(review)
        return {"good": result[0][0], 'bad': result[0][1]}


if __name__ == '__main__':
    app.run(debug=True)


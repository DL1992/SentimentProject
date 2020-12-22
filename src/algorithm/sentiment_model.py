from sklearn import metrics
from joblib import dump, load
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from src.algorithm.data_loader import load_movie_review_data
from sklearn.model_selection import GridSearchCV, train_test_split


def print_classification_report(pred_y, test_y, target_names):
    print(metrics.classification_report(test_y, pred_y,
                                        target_names=target_names))
    cm = metrics.confusion_matrix(test_y, pred_y)
    print(cm)


class SentimentModel:

    def __init__(self):
        self.tf_idf_vec = TfidfVectorizer(min_df=3, max_df=0.95)
        self.clf = RandomForestClassifier()
        self.clf_pipeline = Pipeline([('tfidf', self.tf_idf_vec),
                                      ('clf', self.clf)])

    def fit(self, train_x, train_y):
        self.clf_pipeline.fit(train_x, train_y)

    def fit_grid_search(self, train_x, train_y, params):
        self.clf_pipeline = GridSearchCV(self.clf_pipeline, params, n_jobs=-1)
        self.clf_pipeline.fit(train_x, train_y)

    def predict(self, x_test):
        predictions = self.clf_pipeline.predict(x_test)
        return predictions

    def predict_proba(self, x_test):
        predictions_proba = self.clf_pipeline.predict_proba(x_test)
        return predictions_proba

    def save_model(self, file_path):
        dump(self.clf_pipeline, file_path)

    def load_model(self, file_path):
        self.clf_pipeline = load(file_path)


if __name__ == '__main__':
    data = load_movie_review_data(r'C:\School\workspace\SentimentProject\Data')
    docs_train, docs_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=None)

    model = SentimentModel()
    #
    # parameters = {
    #     'tfidf__ngram_range': [(1, 1), (1, 2)],
    # }
    #
    # model.fit_grid_search(docs_train, y_train, parameters)
    #
    # n_candidates = len(model.clf_pipeline.cv_results_['params'])
    # for i in range(n_candidates):
    #     print(
    #         f'{i}, params - {model.clf_pipeline.cv_results_["params"][i]}; '
    #         f'mean-{model.clf_pipeline.cv_results_["mean_test_score"][i]}, '
    #         f'std-{model.clf_pipeline.cv_results_["std_test_score"][i]}')
    #
    # y_predicted = model.predict(docs_test)
    # print_classification_report(y_predicted, y_test, data.target_names)
    # model.save_model('my_model')

    # print(model.predict_proba(['this is very bad. worst ever']))

import csv
import json

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Movie(Resource):
    def __init__(self, movieid_c, title_c, genres_c):
        self._movieid_c = movieid_c
        self._title_c = title_c
        self._genres_c = genres_c

        @property
        def movieid_c(self) -> str:
            return self._movieid_c

        @property
        def title_c(self) -> str:
            return self._title_c

        @property
        def genres_c(self) -> str:
            return self._genres_c

    # def __str__(self):
    def get(self, movieid_c, title_c, genres_c):
        # return json.dumps(dict(self), ensure_ascii=False)
        return json.dumps({'movieid': movieid_c, 'title': title_c,
                           'genres': genres_c})


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


movies_list = []

with open('source_files/movies.csv', newline='') as movies_csv:
    # movies_str = movies_csv.read()
    reader = csv.reader(movies_csv)
    next(reader, None)
    for movieId, title, genres in reader:
        print(movieId, title, genres)
        # movies_list.append(Movie(movieId, title, genres))
        Movie(movieId, title, genres)

api.add_resource(Movie, '/movies')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

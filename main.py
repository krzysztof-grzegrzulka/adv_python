import csv
import json

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Movie(Resource):
    def __init__(self, movieId_c, title_c, genres_c):
        self._movieId_c = movieId_c
        self._title_c = title_c
        self._genres_c = genres_c

        @property
        def movieId_c(self) -> str:
            return self._movieId_c

        @property
        def title_c(self) -> str:
            return self._title_c

        @property
        def genres_c(self) -> str:
            return self._genres_c

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)


movies_list = []

with open('source_files/movies.csv', newline='') as movies_csv:
    # movies_str = movies_csv.read()
    reader = csv.reader(movies_csv)
    next(reader, None)
    for movieId, title, genres in reader:
        movies_list.append(Movie(movieId, title, genres))

api.add_resource(Movie, '/movies')

# def iter_func(string=movies_str):
#     return iter(string.splitlines())


# movies_str = movies_str.iter_func(movies_str)
# for line in enumerate(movies_str):
#     print(line)

if __name__ == '__main__':
    app.run(debug=True)

import csv
import json

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Movie(Resource):
    def __init__(self, movieId, title, genres):
        self._movieId = movieId
        self._title = title
        self._genres = genres

        @property
        def movieId(self) -> str:
            return self._movieId

        @property
        def title(self) -> str:
            return self._title

        @property
        def genres(self) -> str:
            return self._genres

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)


movies_list = []

with open('source_files/movies.csv', newline='') as movies_csv:
    # movies_str = movies_csv.read()
    reader = csv.reader(movies_csv)
    next(reader, None)
    for movieId, title, genres in reader:
        movies_list.append(Movie(movieId, title, genres))

print(movies_list)

api.add_resource(Movie, '/movies')

# def iter_func(string=movies_str):
#     return iter(string.splitlines())


# movies_str = movies_str.iter_func(movies_str)
# for line in enumerate(movies_str):
#     print(line)

if __name__ == '__main__':
    app.run(debug=True)

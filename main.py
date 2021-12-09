import csv

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Movie(Resource):
    def __init__(self, id, title, genres):
        self._id = id
        self._title = title
        self._genres = genres

        @property
        def id(self) -> str:
            return self._id

        @property
        def title(self) -> str:
            return self._title

        @property
        def genres(self) -> str:
            return self._genres


movies_list = []

with open('source_files/movies.csv', newline='') as movies_csv:
    # movies_str = movies_csv.read()
    reader = csv.reader(movies_csv)
    next(reader, None)
    for id, title, genres in reader:
        id = str(id)
        title = str(title)
        genres = str(genres)
        movies_list.append(Movie(id, title, genres))

print(movies_list)


# def iter_func(string=movies_str):
#     return iter(string.splitlines())


# movies_str = movies_str.iter_func(movies_str)
# for line in enumerate(movies_str):
#     print(line)

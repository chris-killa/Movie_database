from movie_app import MovieApp
from storage_csv import StorageCsv


def main():
    """initialize the storage and start the programm"""
    storage = StorageCsv('data/movies.csv')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()

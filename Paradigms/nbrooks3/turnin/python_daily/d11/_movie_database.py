class _movie_database:

    def __init__(self):
	self.movies = []

    def load_movies(self, movie_file):
	for line in open(movie_file, 'r'):
	    parts = line.split("::")
	    self.movies.append(parts[1])

    def print_sorted_movies(self):
	for result in sorted(self.movies):
	    print result

if __name__ == "__main__":
       mdb = _movie_database()

       #### MOVIES ########
       mdb.load_movies('ml-1m/movies.dat')
       mdb.print_sorted_movies()


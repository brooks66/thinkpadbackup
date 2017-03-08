class _movie_database:

    def __init__(self):
	self.movies_titles = {} #uses movie ID as the key
	self.movies_genres = {} #uses movie ID as the key
	self.users_gender = {} #uses user ID as the key
	self.users_age = {} #uses user ID as the key
	self.users_occupation = {} #uses user ID as the key
	self.users_zipcode = {} #uses user ID as the key
	self.ratings = {} #uses movie ID as the key

    def load_movies(self, movie_file):
	# If movies were already loaded, clear records
	if self.movies_titles:
	    self.movies_titles.clear()
	if self.movies_genres:
	    self.movies_genres.clear()

	# If/once records are clear, populate records
	for line in open(movie_file, 'r'):
	    parts = line.split("::")
	    self.movies_titles[int(parts[0])] = parts[1]
	    self.movies_genres[int(parts[0])] = parts[2].rstrip()

    def print_sorted_movies(self):
	for key, value in sorted(self.movies_titles.iteritems()):
	    print key, value

    def print_movie(self, mid):
	print self.movies_titles[int(mid)]

    def get_movie(self, mid):
	if int(mid) in self.movies_titles:
	    return list([self.movies_titles[int(mid)], self.movies_genres[int(mid)]])
	else:
	    return None

    def get_movies(self):
	movieIDlist = []
	for key in sorted(self.movies_titles.iteritems()):
	    movieIDlist.append(int(key))
	return movieIDlist

    def set_movie(self, mid, titleandgenre):
        self.movies_titles[int(mid)]=titleandgenre[0]
        self.movies_genres[int(mid)]=titleandgenre[1]

    def delete_movie(self, mid):
	if int(mid) in self.movies_titles:
	    del self.movies_titles[int(mid)]
	    del self.movies_genres[int(mid)]

    def load_users(self, users_file):
	# If users were already loaded, clear records
	if self.users_gender:
	    self.users_gender.clear()
	if self.users_age:
	    self.users_age.clear()
	if self.users_occupation:
	    self.users_occupation.clear()
	if self.users_zipcode:
	    self.users_zipcode.clear()

	# If/once records are clear, populate records
	for line in open(users_file, 'r'):
	    parts = line.split("::")
	    self.users_gender[int(parts[0])] = parts[1]
	    self.users_age[int(parts[0])] = parts[2]
	    self.users_occupation[int(parts[0])] = parts[3]
	    self.users_zipcode[int(parts[0])] = parts[4].rstrip()

    def get_user(self, uid):
	if int(uid) in self.users_gender:
	    return list([self.users_gender[int(uid)], int(self.users_age[int(uid)]), int(self.users_occupation[int(uid)]), self.users_zipcode[int(uid)]])
	else:
	    return None

    def get_users(self):
	userIDlist = []
	for key in sorted(self.users_gender.iteritems()):
	    userIDlist.append(int(key))
	return userIDlist

    def set_user(self, uid, userstuff):
	self.users_gender[int(uid)]=userstuff[0]
	self.users_age[int(uid)]=int(userstuff[1])
	self.users_occupation[int(uid)]=int(userstuff[2])
	self.users_zipcode[int(uid)]=userstuff[3]

    def delete_user(self, uid):
	if int(uid) in self.users_gender:
	    del self.users_gender[int(uid)]
	    del self.users_age[int(uid)]
	    del self.users_occupation[int(uid)]
	    del self.users_zipcode[int(uid)]

    def load_ratings(self, ratings_file):
	# If ratings were already loaded, clear records
	if self.ratings:
	    self.ratings.clear()

	# If/once records are clear, populate records
	for line in open(ratings_file, 'r'):
	    parts = line.split("::")
	    try:
		self.ratings[int(parts[1])][int(parts[0])] = int(parts[2])
	    except KeyError:
	        self.ratings[int(parts[1])] = {int(parts[0]) : int(parts[2])}

    def get_rating(self, mid):
	sum = float(0)
	count = float(0)
	average = float(0)
	if mid in self.ratings:
	    for key, value in self.ratings[mid].iteritems():
		count += float(1)
		sum += value
	    average = float(sum)/float(count)
	    return float(average)
	else:
	    return float(0)

    def get_highest_rated_movie(self):
	maximum = float(0)
	thisdict = {}
	if len(self.ratings) != 0:
	    for key,value in self.ratings.iteritems():
		thisdict[key] = self.get_rating(int(key))
	    for key, value in thisdict.iteritems():
		if value > maximum:
		    maxmid = key
		    maximum = value
	    return maxmid
	else:
	    return None

    def set_user_movie_rating(self, uid, mid, rating):
	if int(mid) in self.ratings:
	    self.ratings[int(mid)][int(uid)] = int(rating)
	else:
	    self.ratings[int(mid)] = {int(uid) : int(rating)}

    def get_user_movie_rating(self, uid, mid):
	if int(mid) in self.ratings:
	    if int(uid) in self.ratings[int(mid)]:
		return self.ratings[int(mid)][int(uid)]

    def delete_all_ratings(self):
	if self.ratings:
	    self.ratings.clear()

if __name__ == "__main__":
       mdb = _movie_database()

       #### MOVIES ########
       mdb.load_movies('ml-1m/movies.dat')
       mdb.load_ratings('ml-1m/ratings.dat')
       mdb.load_users('ml-1m/users.dat')
#       rating = mdb.get_rating(3952)
 #      print "3952 = " + str(rating)
  #     rating = mdb.get_rating(787)
   #    print "787 = " + str(rating)
#mdb.get_highest_rated_movie()

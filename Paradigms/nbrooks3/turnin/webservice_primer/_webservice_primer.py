# Name: Nikolas Dean Brooks
# Date: 3/3/2017

import requests
import json

class _webservice_primer:
	def __init__(self):
		self.SITE_URL = 'http://ash.campus.nd.edu:40001'
		self.MOVIES_URL = self.SITE_URL + '/movies/'
		self.RESET_URL = self.SITE_URL + '/reset/'

	def get_movie(self, movie_id): # Gets a dictionary containing the information for a given movie_id
		r = requests.get(self.MOVIES_URL + str(movie_id))
		resp = json.loads(r.content.decode('utf-8'))
		return resp

	def set_movie_title(self, movie_id, title): # sets the title of given movie_id to a given title
		q = requests.get(self.MOVIES_URL + str(movie_id))
		q = json.loads(q.content.decode('utf-8'))
		q['title'] = title
		q = json.dumps(q)
		r = requests.put(self.MOVIES_URL + str(movie_id), q)

	def delete_movie(self, movie_id): # deletes a movie from the web service
		r = requests.delete(self.MOVIES_URL + str(movie_id))

	def reset_movie(self, movie_id): # Resets a given movie_id to the default information
		blah = {}
		blah = json.dumps(blah)
		r = requests.put(self.RESET_URL + str(movie_id), blah)

if __name__ == "__main__":
	MID = 13 # YOUR ASSIGNED MOVIE ID
	ws = _webservice_primer()

#	movie = ws.get_movie(13)
#	print (movie.headers)
#	if movie['result'] == 'success':
#		print ("Title:\t%s" % movie['title'])
#	else:
#		print ("Error:\t%s" % movie['message'])

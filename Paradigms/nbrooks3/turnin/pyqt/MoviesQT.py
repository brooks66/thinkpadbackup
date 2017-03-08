# Nikolas Dean Brooks
# 3/6/17
# Note: I have a bit of a bug where switching users makes one extra
# empty window. Program resumes normal execution fine once it's closed
# out, though. Thanks!

import os
import sys
import requests
import json
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MoviesQT(QMainWindow):
		def __init__(self):
				super(MoviesQT, self).__init__()
				self.SITE_URL = 'http://ash.campus.nd.edu:40001'
				self.USERS_URL = self.SITE_URL + '/users/'
				self.RECOMMENDATIONS_URL = self.SITE_URL + '/recommendations/'
				self.central = MoviesCentral(parent=self)
				self.setCentralWidget(self.central)
				self.setWindowTitle("Movie Recommender")

				# Make file menu, exit option
				self.filemenu = self.menuBar().addMenu("File")
				fileExitAction = QAction("Exit", self)
				self.filemenu.addAction(fileExitAction)

				# Make user menu, "View Profile" and "Set User" options
				self.filemenu = self.menuBar().addMenu("User")
				fileViewProfileAction = QAction("View Profile", self)
				self.filemenu.addAction(fileViewProfileAction)
				fileSetUserAction = QAction("Set User", self)
				self.filemenu.addAction(fileSetUserAction)

				self.connect(fileExitAction, SIGNAL("triggered()"), self.exit_program)
				self.connect(fileViewProfileAction, SIGNAL("triggered()"), self.VPDialog)
				self.connect(fileSetUserAction, SIGNAL("triggered()"), self.SUDialog)

		def VPDialog(self):
			ViewProfileDialog2 = ViewProfileDialog(self.central.uid)
			ViewProfileDialog2.exec_()

		def SUDialog(self):
			SetUserDialog2 = SetUserDialog(self.central.uid)
			SetUserDialog2.exec_()
			value = SetUserDialog2.temp
			self.central.uid = value
			self.central.update()

		def exit_program(self):
			app.quit()

		def upfunction(self):
			q = requests.get(self.RECOMMENDATIONS_URL + str(self.central.uid))
			q = json.loads(q.content.decode('utf-8'))
			q['rating'] = 5.0
			q = json.dumps(q)
			r = requests.put(self.RECOMMENDATIONS_URL + str(self.central.uid), q)
			self.central.update()

		def downfunction(self):
			q = requests.get(self.RECOMMENDATIONS_URL + str(self.central.uid))
			q = json.loads(q.content.decode('utf-8'))
			q['rating'] = 1.0
			q = json.dumps(q)
			r = requests.put(self.RECOMMENDATIONS_URL + str(self.central.uid), q)
			self.central.update()

class MoviesCentral(QWidget):
		def __init__(self, parent=None):
				super(MoviesCentral, self).__init__(parent)
				self.SITE_URL = 'http://ash.campus.nd.edu:40001'
				self.uid = 5 # Just chose this one for now
				self.MOVIES_URL = self.SITE_URL + '/movies/'
				self.RESET_URL = self.SITE_URL + '/reset/'
				self.RECOMMENDATIONS_URL = self.SITE_URL + '/recommendations/'
				self.RATINGS_URL = self.SITE_URL + '/ratings/'

				# Init buttons
				self.upbutton = QPushButton("UP")
				self.downbutton = QPushButton("DOWN")

				self.doallthethings()

				self.connect(self.upbutton, SIGNAL("clicked()"), parent.upfunction)
				self.connect(self.downbutton, SIGNAL("clicked()"), parent.downfunction)

		def update(self):
				movie_id = self.get_recommendations()
				info = self.get_movie(movie_id)
				rating = self.get_rating(movie_id)
				path = "/home/scratch/paradigms/data/images/" + info['img']

				self.movietitle.setText(info['title'])
				pixmap = QPixmap(path)
				self.label.setPixmap(pixmap)
				self.genres.setText(info['genres'])
				self.movierating.setText(str(round(rating, 3)))

		def doallthethings(self):
				movie_id = self.get_recommendations()
				info = self.get_movie(movie_id)
				rating = self.get_rating(movie_id)
				path = "/home/scratch/paradigms/data/images/" + info['img']

				# Set up vertical layout
				self.movietitle = QLabel(info['title'])
				self.label = QLabel()
				pixmap = QPixmap(path)
				self.label.setPixmap(pixmap)
				self.genres = QLabel(info['genres'])
				self.movierating = QLabel(str(round(rating, 3)))

				self.movietitle.setAlignment(Qt.AlignCenter)
				self.label.setAlignment(Qt.AlignCenter)
				self.genres.setAlignment(Qt.AlignCenter)
				self.movierating.setAlignment(Qt.AlignCenter)

				layout = QHBoxLayout()
				layoutv = QVBoxLayout()

				layoutv.addWidget(self.movietitle)
				layoutv.addWidget(self.label)
				layoutv.addWidget(self.genres)
				layoutv.addWidget(self.movierating)
				layout.addWidget(self.upbutton)
				layout.addLayout(layoutv)
				layout.addWidget(self.downbutton)

				self.setLayout(layout)

		def get_movie(self, movie_id):
				self.MOVIES_URL = self.SITE_URL + '/movies/'
				r = requests.get(self.MOVIES_URL + str(movie_id))
				resp = json.loads(r.content.decode())
				return resp # would print /agy8DheVu5zpQFbXfAdvYivF2FU.jpg

		def get_recommendations(self):
				r = requests.get(self.RECOMMENDATIONS_URL + str(self.uid))
				resp = json.loads(r.content.decode())
				mid = resp['movie_id'] # mid is now the ID of the recommended movie
				return mid

		def get_rating(self,movie_id):
				r = requests.get(self.RATINGS_URL + str(movie_id))
				resp = json.loads(r.content.decode())
				rating = resp['rating'] # mid is now the ID of the recommended movie
				return rating

class ViewProfileDialog(QDialog):
		def __init__(self, uid):
				super(ViewProfileDialog, self).__init__()
				self.SITE_URL = 'http://ash.campus.nd.edu:40001'
				self.USERS_URL = self.SITE_URL + '/users/'
				self.uid = uid
				self.initUI()

		def initUI(self):
				self.setWindowTitle("View Profile")
				info = self.get_profile()

				self.Profile = QLabel("Profile ")
				self.gender = QLabel("Gender: " + info['gender'])
				self.zipcode = QLabel("Zipcode: " + info['zipcode'])
				self.age = QLabel("Age: " + str(info['age']))

				self.gender.setAlignment(Qt.AlignCenter)
				self.zipcode.setAlignment(Qt.AlignCenter)
				self.age.setAlignment(Qt.AlignCenter)

				layoutv = QVBoxLayout()

				layoutv.addWidget(self.Profile)
				layoutv.addWidget(self.gender)
				layoutv.addWidget(self.zipcode)
				layoutv.addWidget(self.age)

				self.setLayout(layoutv)

		def get_profile(self):
				r = requests.get(self.USERS_URL + str(self.uid))
				resp = json.loads(r.content.decode())
				return resp

class SetUserDialog(QDialog):
		def __init__(self, uid):
				super(SetUserDialog, self).__init__()
				self.SITE_URL = 'http://ash.campus.nd.edu:40001'
				self.USERS_URL = self.SITE_URL + '/users/'
				self.uid = uid
				self.temp = 0
				self.initUI()

		def initUI(self):
				self.showDialog()
				self.show()

		def showDialog(self):
				text, ok = QInputDialog.getText(self, 'Set User', 'User ID:')
				if ok:
					self.temp = int(text)
				else:
					return None

app = QApplication(sys.argv)
form = MoviesQT()
form.show()
app.exec_()

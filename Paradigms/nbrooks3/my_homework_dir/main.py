# main.py
# This file is similar to the one we did in class. Brooks
# isn't working actively in this file. To see that, look
# at brooksmain.py
import cherrypy
import json

class MyController(object):
	def __init__(self):
		self.myd = dict()

	def GET(self):
		my_dictionary = { 'result' : 'success' }
#		key = str(key)
#		try:
#			value = self.myd[key]
#			my_dictionary['key'] = key
#			my_dictionary['value'] = value
#		except KeyError as ex:
#			my_dictionary['result'] = 'error'
#			my_dictionary['message'] = 'key not found'
		return json.dumps(my_dictionary)

def start_service():

	myController = MyController()

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	dispatcher.connect('randomname', '/duck/', controller = myController, action = 'GET', conditions = dict(method=['GET']))

#	dispatcher.connect('dict_get',
#		'/dictionary/:key', #When this resource is being asked for...
#		controller = myController, # Use an object of this class
#		action = 'GET', #Using this function
#		conditions=dict(method=['GET']) #Something, Something
#	)

	conf = { 'global' : {
			'server.socket_host' : 'ash.campus.nd.edu',
			'server.socket_port' : 40013,
				},
		'/' : {'request.dispatch' : dispatcher}
				 }
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()

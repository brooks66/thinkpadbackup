# brooksmain.py
# This file contains brooks's current work on
# the cherrypy_primer.

import cherrypy
import json
import requests

class MyController(object):
	def __init__(self):
		self.my_dictionary = dict()

	def GET(self, key):
		my_dictionary = { 'result' : 'success' }
		key = str(key)
		try:
			value = self.my_dictionary[key]
			my_dictionary['key'] = key
			my_dictionary['value'] = value
		except KeyError as ex:
			my_dictionary['result'] = 'error'
			my_dictionary['message'] = 'key not found'
		return json.dumps(my_dictionary)

	def PUT(self, key):
		key = str(key)
		my_dictionary = { 'result' : 'success' }
		try:
			q = json.loads(str(cherrypy.request.body.read(), 'utf-8'))
#			print ("Q VALUE = " + q['value'])
			my_dictionary['key'] = str(q['value'])
			my_dictionary['result'] = 'success'
		except KeyError as ex:
			my_dictionary['result'] = 'error'
			my_dictionary['message'] = 'key not found'
		return json.dumps(my_dictionary)

	def DELETE(self, key):
		key = str(key)
		my_dictionary = { 'result' : 'success'}
		self.my_dictionary.pop(key, None)
		return json.dumps(my_dictionary)

	def GETNOKEY(self):
		pass

	def POSTNOKEY(self):
		pass

	def DELETENOKEY(self):
		pass



def start_service():

	myController = MyController()

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	dispatcher.connect('dict_get', '/dictionary/:key', controller = myController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('dict_put', '/dictionary/:key', controller = myController, action = 'PUT', conditions=dict(method=['PUT']))
#	dispatcher.connect('dict_delete', '/dictionary/:key', controller = myController, action = 'DELETE', conditions=dict(method=['DELETE']))
#	dispatcher.connect('dict_getnokey', '/dictionary/', controller = myController, action = 'GETNOKEY', conditions=dict(method=['GET']))
#	dispatcher.connect('dict_postnokey', '/dictionary/', controller = myController, action = 'POSTNOKEY', conditions=dict(method=['POST']))
#	dispatcher.connect('dict_deletenokey', '/dictionary/', controller = myController, action = 'DELETENOKEY', conditions=dict(method=['DELETE']))

	conf = { 'global' : {
		'server.socket_host' : 'localhost',
		'server.socket_port' : 40013,
		},
		'/' : {'request.dispatch' : dispatcher}
	 }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()


import urllib2
import logging
import traceback

import webapp2


urls = [
		'https://jenkins-mirogula.rhcloud.com', 
		'https://nexus-mirogula.rhcloud.com'
	]


class Pinger(webapp2.RequestHandler):

	def get(self):
		for url in urls:
			try :
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				content = response.read()
				headers = ''.join(response.info().headers)
				logging.info('\n===URL===\n'+url
					+'\n===HEADERS===\n'+headers
					+'===CONTENT===\n'+content)
			except:
				logging.error('\n===URL===\n'+url
					+'\n===EXCEPTION===\n'+traceback.format_exc())



application = webapp2.WSGIApplication(
	[
		('/ping', Pinger)
	], 
	debug=True)




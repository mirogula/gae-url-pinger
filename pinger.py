import urllib2
import logging
import traceback

import webapp2


urls = ['http://google.com', 'http://www.voidspace.org.uk']


class Pinger(webapp2.RequestHandler):

	def get(self):
		for url in urls:
			try :
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				the_page = response.read()
				logging.info('url: '+url+'\ncontent:\n'+the_page);
			except:
				logging.error('url: '+url+'\nexception:\n'+traceback.format_exc())



application = webapp2.WSGIApplication(
	[
		(r'/', Pinger)
	], 
	debug=True)




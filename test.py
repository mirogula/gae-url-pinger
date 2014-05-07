import urllib2
import logging
import traceback

urls = [
		'http://google.com', 
		'http://www.voidspace.org.uk'
	]


logging.basicConfig(level=logging.DEBUG)

for url in urls:
	try :
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		the_page = response.read()
		headers = ''.join(response.info().headers)
		logging.info('\n===URL===\n'+url
			+'\n===HEADERS===\n'+headers
			+'===CONTENT===\n'+the_page)
	except:
		logging.error('url: '+url+'\nexception:\n'+traceback.format_exc())


def application(env, start_response):
	start_response('200 OK',  [('Contest-Type', 'text/html')] )
	return [b'uWSGI is Good!']   #python3
	#return ['uWSGI is Good!']   #python2


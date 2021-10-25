"My simple WSGI app/"

import datetime
import json


def app(environ, start_response):
    "Returns JSON wih current time"

    url = 'http://{}:{}{}'.format(
        environ['SERVER_NAME'],
        environ['SERVER_PORT'],
        environ['PATH_INFO'],
    )
    if environ['QUERY_STRING']:
        url += '?' + environ['QUERY_STRING']
    data = {
        'time': str(datetime.datetime.now()),
        'url': url,
    }
    data = json.dumps(data).encode('utf-8')
    start_response('200 OK', [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(data)))
    ])
    return [data]

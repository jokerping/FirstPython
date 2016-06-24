
'WSGIdameo'

from wsgiref.simple_server import make_server

def application(eiviron,start_response):
    start_response('200 ok',[('Content-Type', 'text/html')])
    return [b'<h1>du chun hui da sha bi</h1>']

httpd=make_server('127.0.0.1',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
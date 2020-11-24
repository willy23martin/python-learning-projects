"""
Python WSGI:
- Interface that process all the request and
  response of a simple web server coded using Python.
- Requirements: Python v2
"""

"""
:param - environ: HTTP request information
:param - start_response: function that process the response to be returned.
"""
def web_application(environ, start_response):
    response = '<h1> Python simple native web application </h1>'

    # Contains the HTTP Response Code and the Headers.
    start_response(
        '200 OK',
        [
            ('Content Type', 'text/html; charset=utf-8')
        ]
    )
    return response

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    python_native_web_server = make_server('localhost', 9093, web_application)
    python_native_web_server.serve_forever()
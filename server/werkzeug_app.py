#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application  # The method tells the script to run any code inside of the fucntion in the browser a specified location we specify our development server.
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    # (Method) Runs  a server for a one-page application without complications
    run_simple(
        hostname='localhost',        
        port=5555,                       
        application=application
    )
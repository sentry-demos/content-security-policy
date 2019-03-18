#!/usr/bin/env python
import SimpleHTTPServer

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Security-Policy", # use Content-Security-Policy-Report only for reporting without enforcing
                         "default-src *; "
                         "script-src 'self' 'unsafe-eval' 'unsafe-inline' cdn.example.com cdnc.ravenjs.com example.com; "
                         "style-src 'self' 'unsafe-inline' cdn.example.com; "
                         "img-src * data:; "
                         "report-uri https://sentry.io/api/288413/csp-report/?sentry_key=8fe74c6f5ea546ac9fc4ca1527c08bde")

if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)

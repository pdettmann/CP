import os
import threading
from src.utils.util import run_profiler, send_data
from http.server import BaseHTTPRequestHandler, HTTPServer

test_api_key = 'api-key'

test_case = '''test
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 test_case.py:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''

class MockServerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

class TestClass:
    def test_profiler(self):
        entry_file_path = os.getcwd() + '/tests/test_case.py'
        assert run_profiler(entry_file_path) == test_case

    def test_send_data(self):
        os.environ["TEST"] = "true"
        webServer = HTTPServer(("localhost", 8080), MockServerHandler)
        threading.Thread(target=webServer.serve_forever).start()
        assert send_data(test_case, test_api_key) == 'data sent successfully'
        webServer.shutdown()

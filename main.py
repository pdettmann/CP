import http.client
import json
import os

ENV = os.environ

#entry_file = ENV["MAIN"]
entry_file = './test.py'

os.popen('python3 -m cProfile {} > profile_data'.format(entry_file))

lines = []
with open('./profile_data', encoding='utf8') as f:
    lines = f.readlines()

matches = [match for match in lines if "function calls in" in match]
words = matches[0].split()
functionCalls = words[0]
totalTime = words[4]

# Post profiler data to API
apiUrl = '5q2hk4toq1.execute-api.us-west-2.amazonaws.com'
#apiKey = ENV["API_KEY"]
apiKey =  'xxe03w4sb8hp3w1n5qjer'

connection = http.client.HTTPSConnection(apiUrl)

headers = {'Content-type': 'application/json', 'Authorization': apiKey}

body = {'functionCalls': functionCalls, 'totalTime': totalTime}
json_body = json.dumps(body)

connection.request('POST', '/prod/SaveBenchmarkData', json_body, headers)

response = connection.getresponse()
decoded_response = response.read().decode()

if response.status != 200:
    print('something went wrong')
    print(decoded_response)
print('data sent successfully')

import http.client
import json
import os

ENV = os.environ

entry_file = "/github/workspace/" + ENV["INPUT_ENTRY_FILE"]

os.popen('python3 -m cProfile {} > profile_data'.format(entry_file))

lines = []
with open('action/profile_data', encoding='utf8') as f:
    all = f.read()

print(all)

with open('./profile_data', encoding='utf8') as f:
    lines = f.readlines()

matches = [match for match in lines if "function calls in" in match]
words = matches[0].split()
function_calls = words[0]
total_time = words[4]

# Post profiler data to API
api_url = '5q2hk4toq1.execute-api.us-west-2.amazonaws.com'
api_key = ENV.get('INPUT_API_KEY')

if api_key != None:
    connection = http.client.HTTPSConnection(api_url)

    headers = {'Content-type': 'application/json', 'Authorization': api_key}

    body = {'functionCalls': function_calls, 'totalTime': total_time}
    json_body = json.dumps(body)

    connection.request('POST', '/prod/SaveBenchmarkData', json_body, headers)

    response = connection.getresponse()
    decoded_response = response.read().decode()

    if response.status != 200:
        print('something went wrong')
        print(decoded_response)
    else:
        print('data sent successfully')

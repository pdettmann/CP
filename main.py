import http.client
import json
import os
import subprocess

ENV = os.environ

entry_file = ENV.get("INPUT_ENTRY_FILE")
if entry_file == None:
    print("missing entry file")
    raise SystemExit

entry_file_path = "/github/workspace/" + entry_file

profile_cmd = subprocess.Popen(['python3', '-m', 'cProfile', entry_file_path], stdout=subprocess.PIPE)
profile_data = profile_cmd.communicate()
profile_cmd.wait()
profile_data = profile_data[0].decode('utf-8')
lines = profile_data.split('\n')

print(profile_data)

matches = [match for match in lines if "function calls in" in match]
words = matches[0].split()
function_calls = words[0]
total_time = words[4]

# Post profiler data to API
api_url = '5q2hk4toq1.execute-api.us-west-2.amazonaws.com'
api_key = ENV.get('INPUT_API_KEY')

if api_key == None:
    print("No api key so data was not sent")
    raise SystemExit
else:
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

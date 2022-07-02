#!/usr/bin/env python3

import os
import http.client
import json
import subprocess

def run_profiler(entry_file_path):
    if entry_file_path == None:
        print("missing entry file path")
        raise SystemExit

    profile_cmd = subprocess.Popen(['python3', '-m', 'cProfile', entry_file_path], stdout=subprocess.PIPE)
    profile_data = profile_cmd.communicate()
    profile_cmd.wait()
    profile_data = profile_data[0].decode('utf-8')

    print(profile_data)
    return profile_data

def send_data(profile_data, api_key):
    lines = profile_data.split('\n')
    matches = [match for match in lines if "function calls in" in match]
    words = matches[0].split()
    function_calls = words[0]
    total_time = words[4]

    # Post profiler data to API
    if api_key == None:
        print("No api key so data was not sent")
        raise SystemExit
    else:
        is_test = os.environ.get("TEST") == "true"
        if is_test:
            connection = http.client.HTTPConnection("localhost", 8080)
        else:
            connection = http.client.HTTPSConnection("api.ammonite-profiler.xyz")

        headers = {'Content-type': 'application/json', 'Authorization': api_key}

        body = {'functionCalls': function_calls, 'totalTime': total_time}
        json_body = json.dumps(body)

        connection.request('POST', '/SaveBenchmarkData', json_body, headers)

        response = connection.getresponse()
        decoded_response = response.read().decode()

        if response.status != 200:
            print('something went wrong')
            print(decoded_response)
        else:
            print('data sent successfully')
            return 'data sent successfully'

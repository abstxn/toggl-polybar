import requests
import json
import time
from dotenv import dotenv_values
from base64 import b64encode
from os import path

def prettify_duration(seconds) -> str:
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return '{:02.0f}h {:02.0f}m'.format(hours, minutes)
    # return '{:02.0f}h {:02.0f}m {:02.0f}s'.format(hours, minutes, seconds)

def get_api_token(env_path) -> str:
    token_str = dotenv_values(env_path)['API_TOKEN']
    return b64encode((token_str + ':api_token').encode('utf-8')).decode('ascii')

script_dir = path.dirname(path.abspath(__file__))

API_TOKEN = get_api_token(script_dir + '/api_token.env')
current_entry_url = 'https://api.track.toggl.com/api/v9/me/time_entries/current'
headers = {'content-type': 'application/json', 'Authorization' : 'Basic %s' %  API_TOKEN}

data = requests.get(current_entry_url, headers=headers).json()

if data == None:
    print("No running project.")
else:
    entry_description = data['description']
    entry_duration = prettify_duration(time.time() + data['duration'])
    print(f'{entry_description}: {entry_duration}')
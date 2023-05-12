from dotenv import dotenv_values

API_TOKEN = dotenv_values('api_token.env')['API_TOKEN']
if API_TOKEN == None:
    print('No API token loaded. Exiting...')
    exit(1)


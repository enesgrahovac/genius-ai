"""
The purpose of this file is to test
out how to query data from the Genius
API.

The inspiration for this code is from
this online tutorial/blog: 
https://bigishdata.com/2016/09/27/getting-song-lyrics-from-geniuss-api-scraping/
"""

import requests
from CLIENT_TOKEN import ACCESS_TOKEN

#TOKEN below should be the string that the API docs tells you
#Clearly I'm not giving mine out here on the internet. That'd be dumb
base_url = "http://api.genius.com"
#Key line below here when, this is how to authorize your request when
#using the API
headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
search_url = base_url + "/search"
song_title = "In the Midst of It All"
params = {'q': song_title}
response = requests.get(search_url, params=params, headers=headers)
response_data = response.json()
print(response_data.json)
print(response.text)
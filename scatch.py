import requests
from bs4 import BeautifulSoup

youtube_url = 'https://youtube.com/feed/trending'

response = requests.get(youtube_url)

print('Status Code', response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title.text)

# Find all the video divs
video_divs = doc.find_all('div', class_='style-scope ytd-video-renderer')
print(video_divs)
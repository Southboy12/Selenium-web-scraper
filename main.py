from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

youtube_url = 'https://youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  video_div_tag = 'ytd-video-renderer'
  driver.get(youtube_url)
  videos = driver.find_elements(By.TAG_NAME, video_div_tag)
  return videos

def parse_video(video):
  title_tag =  video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')
  
  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text
  
  description = video.find_element(By.ID, 'description-text').text

  return {
  'title': title,
  'url': url,
  'thumnail_url': thumbnail_url,
  'channel': channel_name,
  'decription': description
  }

  
if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()
  
  print('Fetching trending videos')
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')

print('Parsing the first video')
# title, url, thumbnail_url, channel, views, uploaded, description
video = videos[0]



print('Title:', title)
print('URL:', url)
print('Thumbnail URL:', thumbnail_url)
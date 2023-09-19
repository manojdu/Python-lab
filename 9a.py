#Write a python program to download the all XKCD comics
import requests
import os

base_url = 'https://xkcd.com'
save_directory = 'xkcd_comics'

if not os.path.exists(save_directory):
  os.makedirs(save_directory)

comic_number = 1

for i in range(10):
  comic_url = f'{base_url}/{comic_number}/info.0.json'
  response = requests.get(comic_url)

  if response.status_code == 200:
    comic_data = response.json()
    image_url = comic_data['img']

    response = requests.get(image_url)
    image_path = os.path.join(save_directory,f'xkcd_{comic_number}.png')

    with open(image_path,"wb") as image_file:
      image_file.write(response.content)

    print(f'Downloaded comic #{comic_number}')
    comic_number += 1
  else:
    break

    print("10 XKCD comics downloaded successfully")
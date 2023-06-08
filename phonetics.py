import requests
from bs4 import BeautifulSoup
import random
import os
from PIL import Image
from io import BytesIO
word = os.getenv('KEYWORD', 'default_keyword')
def read(word):
    url = f'https://pansci.asia/?post_type%5B%5D=post&post_type%5B%5D=post_review&post_type%5B%5D=pan_booklist&s={word}'
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'lxml')
    data = bs.find_all('a', {'class': 'post-title ga_track'})

    if len(data) > 0:
        selected_item = random.choice(data)
        title = selected_item.text.strip()
        photo_url = selected_item.find_previous('img')['src']

        #print("Title:", title)
        #print("Photo URL:", https://pansci.asia/wp-content/uploads/2023/03/christian-rosswag-P_6UKCsYLNs-unsplash-510x315.jpg)

        # Display the photo
        response = (title, photo_url)
        return ( response )
    else:
        return ("查無資料")
read(word)

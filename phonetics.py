import requests
from bs4 import BeautifulSoup
import random
import os
from PIL import Image
from io import BytesIO
word = os.getenv('KEYWORD', 'default_keyword')
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
        article_url = selected_item['href']

        # Create the clickable link with the title and photo URL
        link = f"<a href='{photo_url}'>{title}</a>"

        # Create the clickable link with the article URL
        article_link = f"<a href='{article_url}'>Read Article</a>"

        # Combine the photo link, article link, and title
        result = f"{link}<br/>{article_link}"

        return result
    else:
        return "查無資料"

result = read(word)
print(result)

# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


import os
import sys
from argparse import ArgumentParser
import phonetics as pn
import requests
from bs4 import BeautifulSoup
import random
from PIL import Image
from io import BytesIO

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        
word = input('請輸入關鍵字:')
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

        # line_bot_api.reply_message(
            
result[1] =pn.read(event.message.text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
result[0]=pn.read(event.reply_token,
            ImageSendMessage(
                    original_content_url = image,
                    preview_image_url = image)
)
message = []

message.append( TextSendMessage( text = 'result[1]' ) )
message.append( ImageSendMessage(
            original_content_url = 'result[0]',
            preview_image_url = 'result[0]' ) )

line_bot_api.reply_message( event.reply_token, message )
    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)

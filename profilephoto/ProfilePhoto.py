import json
import os
import re

from telegram import Bot
from telethon import TelegramClient
from config import *


class ProfilePhoto():
    session_name = 'default_session_name'
   
    def __init__(self, photo_dir='user_photos') -> None:
        self.client = TelegramClient(self.session_name, API_ID, API_HASH).start(bot_token=BOT_TOKEN)
        self.photo_dir = photo_dir 
        self.bot = Bot(token=BOT_TOKEN)
        
        
    def update_photo_file(self, user_id:int) -> bool:
        try:
            photo = self.bot.get_user_profile_photos(user_id).photos
        except:
            return False
        if photo:
            photo = photo[0][1]
        else:
            return False
        self._download_photo(photo, path=f'{self.photo_dir}/{user_id}.png')
        self._update_data_file(user_id, photo.file_id)
        return True
    
    def _download_photo(self, photo_obj, path):
        photo_obj.get_file().download(custom_path=path)
       
        
    def _update_data_file(self, user_id:int, photo_id:str) -> None:  
        data = self._get_photos_data()
        with open(f'{self.photo_dir}/data.json', 'w+') as f:
            data[f'{user_id}'] = photo_id
            json.dump(dict(data), f)
            
            
    def _get_photos_data(self) -> dict[str:str]:
        with open(f'{self.photo_dir}/data.json', 'r') as f:
            if os.stat(f'{self.photo_dir}/data.json').st_size == 0:
                data = {}
            else:
                data = json.load(f)
        return data
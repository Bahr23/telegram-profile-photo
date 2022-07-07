import telethon

from .ProfilePhoto import ProfilePhoto
from config import *


class ProfilePhotoUpdater(ProfilePhoto):
    session_name = 'photo_updater'      
       
       
    def start(self): 
        self.sync_photos()
        self.client.add_event_handler(self._check_update)
        self.client.run_until_disconnected()
    
    
    async def _check_update(self, update):
        if isinstance(update, telethon.tl.types.UpdateUserPhoto):
            print(update)
            self.update_photo_file(update.user_id)
            
            
    def sync_photos(self):
        data = self._get_photos_data()
        
        if data:
            for user_id in data.keys():
                photo = self.bot.get_user_profile_photos(int(user_id)).photos
                if photo:
                    photo = photo[0][1]
                    if photo.file_id != data[user_id]:
                        self.update_photo_file(int(user_id))
                else:
                    photo = None

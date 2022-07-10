import os.path

from .ProfilePhoto import ProfilePhoto
from config import *


class ProfilePhotoGetter(ProfilePhoto):
    session_name = 'photo_getter'
      

    def get(self, user_id:int) -> str:
        data = self._get_photos_data()
        result = True
        if str(user_id) in data.keys():
            if not self._check_is_file_exist(data[str(user_id)]):
                result = self.update_photo_file(user_id)
        else:
            result = self.update_photo_file(user_id)
        data = self._get_photos_data()    
        if result:
            return f'{self.photo_dir}/{data[str(user_id)]}.png'
        else:
            return None
    
    def _check_is_file_exist(self, file_id:str) -> bool:
        return os.path.isfile(f'{self.photo_dir}/{file_id}.png')
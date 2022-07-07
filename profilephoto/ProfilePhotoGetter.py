import os.path

from .ProfilePhoto import ProfilePhoto
from config import *


class ProfilePhotoGetter(ProfilePhoto):
    session_name = 'photo_getter'
      

    def get(self, user_id:int) -> str:
        if not self._check_is_file_exist(user_id):
            if self.update_photo_file(user_id):
                return f'{self.photo_dir}/{user_id}.png'
            else:
                return None
        return f'{self.photo_dir}/{user_id}.png'
    
    def _check_is_file_exist(self, user_id:int) -> bool:
        return os.path.isfile(f'{self.photo_dir}/{user_id}.png')
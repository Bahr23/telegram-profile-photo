from threading import Thread

from app import app
from config import *
from profilephoto import *


def main():  
    app_thread = Thread(target=app.run)
    app_thread.start()

    profile_photo_updater = ProfilePhotoUpdater()
    profile_photo_updater.start()


if __name__ == '__main__':
    main()
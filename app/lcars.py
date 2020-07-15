from screens.main import ScreenMain
from screens.authorize import ScreenAuthorize
from screens.screensaver import ScreenSaver
from ui.ui import UserInterface

import config

if __name__ == "__main__":

    if config.PIN == '':
        UserInterface.Authorised = True
    
    firstScreen = ScreenMain()
    authorizeScreen = ScreenAuthorize()
    screenSaver = ScreenSaver()
    
    audio_params=(22050, -8, 1, 1024)
    
    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
                       config.SOUND, audio_params, authorizeScreen, screenSaver)

    while (True):
        ui.tick()


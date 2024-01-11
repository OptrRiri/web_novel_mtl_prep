import os
from pathlib import Path

firefox_binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

firefox_marionette_cmdStr = r"firefox.exe -marionette -start-debugger-server 2828"

firefox_profile_pathStr = r"C:\Users\ASUS\AppData\Roaming\Mozilla\Firefox\Profiles\0d2xdi3k.for-selenium"

pathfinder_geckodriver_pathStr = r"C:\Users\ASUS\pythonData\pathfinder\geckodriver.exe"
broke_pathfinder_geckodriver_pathStr = r"C:\Users\ASUS\pythonData\geckodriver.exe"
local_absolute_geckodriver_pathStr = r"C:\Users\ASUS\notesData\jpLearning\novel-translation\dev\link_to_excel\drivers\geckodriver.exe"
FOLDER_OF_THIS_FILE = Path(
    os.path.dirname(
        p=os.path.realpath(
            path=__file__
        )
    )
)
local_relative_geckodriver_pathStr = FOLDER_OF_THIS_FILE.parent / Path("drivers") / Path("geckodriver.exe")
geckopath = pathfinder_geckodriver_pathStr

service_args = [
    '--marionette-port',  
    "2828", 
    '--connect-existing'
]

gtl_link = r"https://translate.google.com/?sl=ja&tl=en&op=translate"
interval_wait_for_complete_tl = 5
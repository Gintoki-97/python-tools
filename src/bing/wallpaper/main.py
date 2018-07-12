import os
import json
import requests
import win32api
import win32con
import win32gui

# @Modifiable
# The URL is the local storage folder of the wallpapers that downloaded from Bing
_WALLPAPER_ROOT = "D:/Resource/OS/Picture/Wallpaper/"

# @NonModifiable
# The URLs are related to the wallpaper source path, needn't modified
_BING = "https://cn.bing.com"
_BING_WALLPAPER = _BING + "/HPImageArchive.aspx?format=js&idx=0&n=1&nc=0&pid=hp&video=1"


# Get the index of wallpaper in local storage folder, each wallpaper need to rename by the increment index
def get_wallpaper_index():
    max_index = 1
    images = os.listdir(_WALLPAPER_ROOT)

    for image in images:
        curr_index = int(image.split(".")[0])
        if curr_index > max_index:
            max_index = curr_index

    max_index = max_index + 1

    return max_index


# Get the JSON data according to the wallpaper source path
def get_wallpaper_json():
    # Send HTTP Request
    resp = requests.get(_BING_WALLPAPER)

    # Handler the response
    if resp.status_code == 200:
        return json.loads(resp.text)


# Get the image file from the image URL in JSON data
def get_wallpaper(wallpaper_json):
    wallpaper_url = _BING + wallpaper_json['images'][0]['url']
    resp = requests.get(wallpaper_url)

    return resp.content


# Set the wallpaper for OS
def set_wallpaper(image_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1+2)


# Create new wallpaper file
target_file = _WALLPAPER_ROOT + str(get_wallpaper_index()) + ".jpg"
target_file_handler = open(target_file, "wb")

# Write the web image to file
wallpaper = get_wallpaper_json()
target_file_handler.write(get_wallpaper(wallpaper))
target_file_handler.close()

# Set wallpaper
set_wallpaper(target_file)
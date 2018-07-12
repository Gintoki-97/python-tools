## 1. Description

#####  A very easy script about Python

> This script can be used to automatically download Bing daily wallpaper, store it to local directory and set it to desktop wallpaper.

## 2. Develop Environment

- OS : Windows 64 bit
- Python : 3.6.0
- IDE : PyCharm Community 2018.1

> The Linux system also could run this program, because of the cross platform of Python 

## 3. How To Run

> I will only describe how to run on windows, because if you use the Linux system, running the program should have no difficulty for you.

1. Install the Python3.6 environment for your windows system.
2. Modified the local storage folder of the wallpapers for your own system, and modify the path of the .py file in run.cmd (line:6).
3. Configuring the "task scheduler" in "computer management", create a new task to run the cmd file.

##### About run.cmd
- ##### The path of cmd file is %python-tools%/src/bing/wallpaper/run.cmd. It could run the main.py automatic
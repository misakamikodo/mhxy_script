import os

import psutil
import pytesseract
from PIL import Image
import datetime as dt
import pyperclip

from game_process import GameProcess
from mhxy import *
import playsound as pl
#导入线程模块
import threading


if __name__ == '__main__':
    gam = GameProcess()
    gam.closeMoniqi()

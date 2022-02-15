from os import listdir, mkdir
from pyrogram import Client
from CilikMusic import config
from CilikMusic.MusicUtilities.tgcallsrun.queues import (clear, get, is_empty, put, task_done)
from CilikMusic.MusicUtilities.tgcallsrun.downloader import download
from CilikMusic.MusicUtilities.tgcallsrun.convert import convert
from CilikMusic.MusicUtilities.tgcallsrun.music import run
from CilikMusic.MusicUtilities.tgcallsrun.music import smexy as ASS_ACC
smexy = 1

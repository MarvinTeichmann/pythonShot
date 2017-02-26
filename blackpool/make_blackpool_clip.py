#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys
import logging

import moviepy.editor as mpy

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)

basedir = '/home/marvin/Videos/Blackpool'

fotos = ['IMG_0850.JPG', 'IMG_0852.JPG', 'IMG_0851.JPG']

clip_list = {
    'walz_emp': 'IMG_0855.MOV',
    'quick_emp': 'IMG_0856.MOV',
    'walz_span': 'IMG_0858.MOV',
    'quick_span': 'IMG_0859.MOV'
}

import ipdb
ipdb.set_trace()


exit(0)


def main():
    movielist = config()
    generate_movies(movielist)
    return


def config():

    start_clip = {"name": "0005_united.mp4", "seq": (9, 25.5)}
    seg1 = {"name": "0001_segmentation.mp4", "seq": (0, 12)}
    seg2 = {"name": "0019_segmentation.mp4", "seq": (7.8, 20.6)}
    det1 = {"name": "0018_detection.mp4", "seq": (2, 20)}
    det2 = {"name": "0010_united.mp4", "seq": (4, None)}
    united = {"name": "0003_united.mp4", "seq": (2, 12)}

    movielist = [start_clip, seg1, seg2, det1, det2, united]

    return movielist


def generate_clip(movie):
    clip = mpy.VideoFileClip(movie['name'])
    if "seq" in movie:
        clip = clip.subclip(*movie['seq'])
    return clip


def generate_movies(movielist):

    cliplist = [generate_clip(movie) for movie in movielist]

    final_clip = mpy.concatenate_videoclips(cliplist)

    final_clip.write_videofile("MultiNet.mp4")

if __name__ == "__main__":
    main()

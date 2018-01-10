# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import os

def mkdir(path):
    # delete head space and tail \
    path = path.strip().rstrip('\\')
    if os.path.exists(path):
        return False
    else:
        os.makedirs(path)
        return True

def get_music_ids_and_singer_name_by_singer_id(singer_id):
    """
    :param singer_id: integer of a singer's id
    :return: list of music ids
            string of singer name
    """

    url = 'http://music.163.com/artist?id='+str(singer_id)
    r = requests.get(url).text
    # print(r)
    bs_obj = BeautifulSoup(r, features='lxml')
    # singer_name = bs_obj.select("#artist-name")[0].get('title')
    # print(singer_name)
    t = bs_obj.find('textarea')
    musics = json.loads(t.text.replace('(','[').replace(')',']').replace('\'','"'))
    music_ids = {}
    for music in musics:
        music_ids[music['name']] = music['id']
    print(music_ids)


def get_lyric_by_music_id(music_id):
    """
    :param music_id: integer of a music's id
    :return: string of a song's lyrics
    """
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
    json_obj = requests.get(lrc_url).text
    # print(json_obj)
    j_dict = json.loads(json_obj)
    # print(j_dict)

    # get lrc
    try:
        lrc = j_dict['lrc']['lyric']
        pattern = re.compile(r'\[.*\]')
        lrc = re.sub(pattern,'',lrc)
        lrc = lrc.strip()
        print(lrc)
    except KeyError:
        pass







if __name__ == '__main__':
    ## 1197115 : PG one
    # get_music_ids_and_singer_name_by_singer_id(5781)
    ## 512376362 : 中二病 Remix
    # get_lyric_by_music_id(512376362)
    pass
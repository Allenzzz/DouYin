from douyin.config import hot_music_url
from douyin.structures import HotMusic
from douyin.utils import fetch
from douyin.utils.common import parse_datetime
from douyin.utils.tranform import data_to_music


def music(search_key):
    """
    get hot music result
    :return: HotMusic object
    """
    result = fetch(hot_music_url.format(search_key))
    # process json data
    datetime = parse_datetime(result.get('active_time'))
    # video_list = result.get('music_list', [])
    musics = []
    music_list = result.get('data').get('music')
    for item in music_list:
        music = data_to_music(item)
        # music.hot_count = item.get('hot_value')
        musics.append(music)
        # construct HotMusic object and return
    return HotMusic(datetime=datetime, data=musics)

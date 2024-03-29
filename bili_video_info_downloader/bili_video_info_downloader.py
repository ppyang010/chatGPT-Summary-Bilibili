import requests
from bili_video_info_downloader.section_info import section_dict


class VideoInfoDownloader:
    def __init__(self, bv_id: str) -> None:
        self.bv_id = bv_id
        self.info_api = "https://api.bilibili.com/x/web-interface/view"
        self.tags_api = "https://api.bilibili.com/x/web-interface/view/detail/tag"


    def _get_info(self):
        custom_headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36'
        }
        params = (
            ('bvid', self.bv_id),
        )
        response = requests.get(self.info_api, params=params,headers=custom_headers)
        return response.json()['data']


    def _get_tags(self):

        custom_headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36'
        }
        params = (
            ('bvid', self.bv_id),
        )

        response = requests.get(self.tags_api, params=params,headers=custom_headers)
        data = response.json()['data']
        if data:
            tags = [x['tag_name'] for x in data]
            if len(tags) > 5:
                tags = tags[:5]
        else:
            tags = []
        return tags


    def download_video_info(self):
        info = self._get_info()
        tags = self._get_tags()
        section = section_dict[info['tid']]
        return {
            "info": info,
            "tags": tags,
            "section": section,
            "bvid": self.bv_id
        }

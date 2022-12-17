from src.data_fetch.api_manager import ApiManager


class AdsManager(ApiManager):
    def __init__(self, username, password, **kwargs):
        super().__init__(**kwargs)
        self.get_tokens(username, password)

    def add_ad(self, params):
        self.refresh()
        url = "/ads/add"
        return self.send_post(url, params)

    def get_ad(self, params):
        self.refresh()
        url = "/ads/get"
        return self.send_get(url, params)

    def list_ads(self, params):
        self.refresh()
        url = "/ads/list"
        return self.send_get(url, params)

    def update_ad(self, params):
        self.refresh()
        url = "/ads/update"
        return self.send_post(url, params)

    def delete_ad(self, params):
        self.refresh()
        url = "/ads/delete"
        return self.send_post(url, params)

    def undelete_ad(self, params):
        self.refresh()
        url = "/ads/undelete"
        return self.send_post(url, params)

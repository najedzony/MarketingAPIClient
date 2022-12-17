from src.data_fetch.api_manager import ApiManager


class CampaignsManager(ApiManager):
    def __init__(self, username, password, **kwargs):
        super().__init__(**kwargs)
        self.get_tokens(username, password)

    def add_campaign(self, params):
        self.refresh()
        url = "/campaign/add"
        return self.send_post(url, params)

    def list_campaigns(self, params):
        self.refresh()
        url = "/campaign/list"
        return self.send_get(url, params)

    def update_campaign(self, params):
        self.refresh()
        url = "/campaign/update"
        return self.send_post(url, params)

    def delete_campaign(self, params):
        self.refresh()
        url = "/campaign/delete"
        return self.send_post(url, params)

    def undelete_campaign(self, params):
        self.refresh()
        url = "/campaign/undelete"
        return self.send_post(url, params)

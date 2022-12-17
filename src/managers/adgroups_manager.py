from src.data_fetch.api_manager import ApiManager


class AdgroupsManager(ApiManager):
    def __init__(self, username, password, **kwargs):
        super().__init__(**kwargs)
        self.get_tokens(username, password)

    def add_adgroup(self, params):
        self.refresh()
        url = "/adgroups/add"
        return self.send_post(url, params)

    def get_adgroup(self, params):
        self.refresh()
        url = "/adgroups/get"
        return self.send_get(url, params)

    def list_adgroups(self, params):
        self.refresh()
        url = "/adgroups/list"
        return self.send_get(url, params)

    def update_adgroup(self, params):
        self.refresh()
        url = "/adgroups/update"
        return self.send_post(url, params)

    def delete_adgroup(self, params):
        self.refresh()
        url = "/adgroups/delete"
        return self.send_post(url, params)

    def undelete_adgroup(self, params):
        self.refresh()
        url = "/adgroups/undelete"
        return self.send_post(url, params)

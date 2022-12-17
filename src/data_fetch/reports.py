from src.data_fetch.api_manager import ApiManager


class ReportsFetcher(ApiManager):
    def __init__(self, username, password, **kwargs):
        super().__init__(**kwargs)
        self.get_tokens(username, password)

    def get_advertiser_reports(self, date_from, date_to):
        self.refresh()
        url_suffix = "/reports/advertiser"
        params = {
            "date_from": date_from,
            "date_to": date_to,
        }
        return self.send_get(url_suffix, params)

    def get_campaigns_reports(self, date_from, date_to, group_by):
        self.refresh()
        url_suffix = "/reports/campaigns"
        params = {
            "date_from": date_from,
            "date_to": date_to,
            "group_by": list(group_by),
        }
        return self.send_get(url_suffix, params)

    def get_adgroups_reports(self, date_from, date_to, group_by):
        self.refresh()
        url_suffix = "/reports/adgroups"
        params = {
            "date_from": date_from,
            "date_to": date_to,
            "group_by": list(group_by),
        }
        return self.send_get(url_suffix, params)

    def get_ads_reports(self, date_from, date_to, group_by):
        self.refresh()
        url_suffix = "/reports/ads"
        params = {
            "date_from": date_from,
            "date_to": date_to,
            "group_by": list(group_by),
        }
        return self.send_get(url_suffix, params)


# username = "username6"
# password = "password12345"
# base_url = "http://127.0.0.1:5000/api/v1"
# fetcher = ReportsFetcher(base_url=base_url, username=username, password=password)
#
# print(fetcher.get_advertiser_reports("2022-01-01", "2022-12-12"))

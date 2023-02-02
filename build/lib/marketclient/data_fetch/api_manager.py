import requests


class ApiManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.access_token = None
        self.refresh_token = None

    def get_tokens(self, username, password):
        params = {
            "username": username,
            "password": password,
        }
        url = f"{self.base_url}/auth/authenticate"
        response = requests.post(url, json=params)
        response_json = self.get_response_json(response)
        self.access_token, self.refresh_token = (
            response_json["user"]["access_token"],
            response_json["user"]["refresh_token"],
        )

    def refresh(self):
        url = f"{self.base_url}/auth/refresh"
        headers = {"Authorization": f"Bearer {self.refresh_token}"}
        response = requests.post(url, headers=headers)
        response_json = self.get_response_json(response)
        self.access_token = response_json["access_token"]

    def send_get(self, url_suffix, params):
        url = f"{self.base_url}{url_suffix}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers, json=params)
        return self.get_response_json(response)

    def send_post(self, url_suffix, params):
        url = f"{self.base_url}{url_suffix}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.post(url, headers=headers, json=params)
        return self.get_response_json(response)

    def get_response_json(self, response):
        accept_codes = [200, 201, 202, 204]
        if response.status_code not in accept_codes:
            raise Exception(
                f"Request failed with status {response.status_code} and message {response.text}"
            )
        try:
            return response.json()
        except Exception:
            raise


# apimanager = ApiManager(base_url="http://127.0.0.1:5000/api/v1")
# username = "username6"
# password = "password12345"
# apimanager.get_tokens(username, password)
# print(apimanager.access_token)
# apimanager.refresh()
# print(apimanager.access_token)

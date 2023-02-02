from cached_property import cached_property
from google.oauth2 import service_account
from google.cloud import storage


class GoogleCloudStorageClient:
    def __init__(self, credentials_key_path, project):
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_key_path,
            scopes=[
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/devstorage.full_control",
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/devstorage.read_write",
            ],
        )
        self.project = project

    @cached_property
    def _client(self):
        return storage.Client(
            credentials=self.credentials, project=self.project
        )

    def create_bucket(self, bucket_name):
        self._client.create_bucket(bucket_name)

    def list_buckets(self):
        return [bucket.name for bucket in self._client.list_buckets()]

    def download_file(self, bucket_name, path):
        bucket = self._client.get_bucket(bucket_name)
        blob = bucket.blob(path)
        return blob.download_as_string()

    def list_files(self, bucket_name):
        return [blob.name for blob in self._client.list_blobs(bucket_name)]

    def upload_file(self, bucket_name, path, data):
        bucket = self._client.get_bucket(bucket_name)
        blob = bucket.blob(path)
        blob.upload_from_string(data)

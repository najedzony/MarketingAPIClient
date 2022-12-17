import pandas_gbq
from cached_property import cached_property
from google.cloud import bigquery
from google.oauth2 import service_account


class BigqueryClient:
    def __init__(self, credentials_key_path):
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_key_path,
            scopes=[
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/bigquery",
            ],
        )

    @cached_property
    def _client(self):
        return bigquery.Client(
            credentials=self.credentials, project=self.credentials.project
        )

    def create_table(self, table_id, schema):
        bq_schema = [
            bigquery.SchemaField(name, type, mode="NULLABLE") for name, type in schema
        ]
        table = bigquery.Table(table_id, schema=bq_schema)
        self._client.create_table(table)

    def upload_dataframe(self, table_id, df):
        pandas_gbq.to_gbq(
            df,
            table_id,
            project_id=self.credentials.project,
            credentials=self.credentials,
            if_exists="append",
        )

    def read_dataframe(self, query):
        pandas_gbq.read_gbq(
            query, project_id=self.credentials.project, credentials=self.credentials
        )

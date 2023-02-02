import pandas_gbq
from cached_property import cached_property
from google.cloud import bigquery
from google.oauth2 import service_account

from marketclient.transforming.base_transformer import TYPE_CONVERSION


class BigqueryClient:
    def __init__(self, credentials_key_path, project):
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_key_path,
            scopes=[
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/bigquery",
            ],
        )
        self.project = project

    @cached_property
    def _client(self):
        return bigquery.Client(
            credentials=self.credentials, project=self.project
        )

    def _build_bq_fields(self, schema):
        return [bigquery.SchemaField(name, type, mode="NULLABLE") for name, type in schema]

    def transform_fields_types(self, df, schema):
        for name, type in schema:
            df[name] = df[name].apply(lambda x: TYPE_CONVERSION[type](x))
        return df

    def create_table(self, table_id, schema):
        bq_schema = self._build_bq_fields(schema)
        table = bigquery.Table(table_id, schema=bq_schema)
        self._client.create_table(table)

    def upload_dataframe(self, table_id, df, schema):
        if schema:
            df = self.transform_fields_types(df, schema)
            job_config = bigquery.LoadJobConfig(
                schema=self._build_bq_fields(schema),
                write_disposition="WRITE_APPEND",
            )
        else:
            job_config = bigquery.LoadJobConfig(
                autodetect=True,
                write_disposition="WRITE_APPEND",
            )
        job = self._client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )
        job.result()

    def read_dataframe(self, query):
        return pandas_gbq.read_gbq(
            query, project_id=self.project, credentials=self.credentials
        )

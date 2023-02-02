import json

import pandas as pd

from marketclient.data_fetch.api_manager import ApiManager
from marketclient.data_fetch.reports import ReportsFetcher
from marketclient.gcptools.bigquery import BigqueryClient
from marketclient.gcptools.gcs import GoogleCloudStorageClient
from marketclient.managers.adgroups_manager import AdgroupsManager
from marketclient.managers.ads_manager import AdsManager
from marketclient.managers.campaigns_manager import CampaignsManager

"""
admin, admin_password
"""

USERNAME = "username10"
PASSWORD = "password"

campaign_manager = CampaignsManager(base_url="http://127.0.0.1:5000/api/v1", username=USERNAME, password=PASSWORD)
# adgroups_manager = AdgroupsManager(base_url="http://127.0.0.1:5000/api/v1", username=USERNAME, password=PASSWORD)
# ads_manager = AdsManager(base_url="http://127.0.0.1:5000/api/v1", username=USERNAME, password=PASSWORD)

# reports_manager = ReportsFetcher(base_url="http://127.0.0.1:5000/api/v1", username=USERNAME, password=PASSWORD)
# print(reports_manager.get_advertiser_reports(date_from="2022-12-01", date_to="2022-12-05"))
# print(reports_manager.get_ads_reports(date_from="2022-12-01", date_to="2022-12-05", group_by="REPORT_DATE"))

# campaign_manager.delete_campaign(
#     {
#         "campaign_id": 7
#     }
# )

PROJECT = "bachelorsthesis-372012"

bq_client = BigqueryClient(credentials_key_path="./secrets/sa.json", project=PROJECT)

# bq_client.create_table(
#     schema=(
#         ("campaign_id", "INTEGER"),
#         ("campaign_name", "STRING"),
#         ("creation_date", "TIMESTAMP"),
#         ("daily_budget", "FLOAT"),
#         ("deletion_date", "TIMESTAMP"),
#         ("last_update_date", "TIMESTAMP"),
#         ("status", "STRING"),
#     ),
#     table_id=f"{PROJECT}.marketing_api_data.campaigns"
# )

data = campaign_manager.list_campaigns({})
df = pd.DataFrame(data)
print(df.to_string())

schema = (
    ("campaign_id", "INTEGER"),
    ("campaign_name", "STRING"),
    ("creation_date", "STRING"),
    ("daily_budget", "FLOAT"),
    ("deletion_date", "STRING"),
    ("last_update_date", "STRING"),
    ("status", "STRING"),
)

# bq_client.upload_dataframe(table_id=f"{PROJECT}.marketing_api_data.campaigns", df=df, schema=schema)
query = "SELECT * FROM `bachelorsthesis-372012.marketing_api_data.campaigns`"
# df = bq_client.read_dataframe(query)
# print(df.to_string())

gcs_client = GoogleCloudStorageClient(credentials_key_path="./secrets/sa.json", project=PROJECT)
# gcs_client.create_bucket("dupa-test-bucket")
# gcs_client.upload_file("dupa-test-bucket", "dupa-test-bucket/nowy_plik.json", json.dumps(data))
print(gcs_client.list_files("dupa-test-bucket"))
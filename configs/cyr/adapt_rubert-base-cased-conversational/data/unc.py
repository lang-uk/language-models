from language_model.data.load import YSDataDownloadTask
from language_model.data.processing import LightweightMention

task = YSDataDownloadTask(
    credentials_path="configs/credentials",
    topic_id=252714,
    query={
        "from": "2018-01-01",
        "to": "2021-03-01",
        "sanitize": False,
        "dedup": False,
        "respectAnalyticalWindow": False,
        "samplingRate": 0.25,
    },
    sandbox_folder_path="data",
    mention_processor=LightweightMention(),
)
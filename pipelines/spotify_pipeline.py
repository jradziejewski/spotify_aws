from utils.constants import OUTPUT_PATH
from etls.spotify_etl import extract_data, transform_data, load_data


def spotify_pipeline(file_name: str, time_filter="day", limit=None):
    # extract data
    data = extract_data(time_filter, limit)

    # transform data
    transformed_data = transform_data(data)

    # load data to csv
    path = f"{OUTPUT_PATH}/{file_name}.csv"
    load_data(transformed_data, path)

    return path

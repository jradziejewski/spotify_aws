import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), "../config/config.conf"))

SECRET = parser.get("api_keys", "spotify_secret_key")
CLIENT_ID = parser.get("api_keys", "spotify_client_id")

DATABASE_HOST = parser.get("database", "database_host")
DATABASE_NAME = parser.get("database", "database_name")
DATABASE_PORT = parser.get("database", "database_port")
DATABASE_USER = parser.get("database", "database_username")
DATABASE_PASSWORD = parser.get("database", "database_password")

AWS_ACCESS_KEY_ID = parser.get("aws", "aws_access_key_id")
AWS_SECRET_ACCESS_KEY = parser.get("aws", "aws_secret_access_key")
AWS_REGION = parser.get("aws", "aws_region")
AWS_BUCKET_NAME = parser.get("aws", "aws_bucket_name")

INPUT_PATH = parser.get("file_paths", "input_path")
OUTPUT_PATH = parser.get("file_paths", "output_path")

PLAYLIST_ID = "37i9dQZEVXbMDoHDwVN2tF"

TRACK_FIELDS = [
    "available_markets",
    "disc_number",
    "duration_ms",
    "explicit",
    "href",
    "id",
    "name",
    "popularity",
    "preview_url",
    "track_number",
    "type",
    "uri",
    "is_local",
]

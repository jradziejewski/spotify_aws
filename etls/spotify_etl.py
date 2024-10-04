import requests
import sys
import pandas as pd
from utils.constants import CLIENT_ID, SECRET, TRACK_FIELDS, PLAYLIST_ID


def get_access_token():
    """
    Get the access token for the Spotify API.
    """
    try:
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": SECRET,
        }
        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print("Failed to obtain access token:", response.json())
            sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)


def extract_data(time_filter, limit):
    """
    Extract data from the Spotify API.
    """
    access_token = get_access_token()

    playlist_id = PLAYLIST_ID
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        print("Token expired, getting new token")
        access_token = get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to extract data:", response.json())
        sys.exit(1)


def transform_data(data):
    """
    Transform the data extracted from Spotify API into a DataFrame.
    """
    track_list = []
    for track in data["tracks"]["items"]:
        track_dict = {}

        # Get artist names
        track_dict["artists"] = [artist["name"] for artist in track["track"]["artists"]]
        # Get album name
        track_dict["album"] = track["track"]["album"]["name"]

        # Get required fields
        for field in TRACK_FIELDS:
            # Check if the field exists in the track
            if field in track["track"]:
                track_dict[field] = track["track"][field]
            else:
                track_dict[field] = None  # Assign None if field does not exist

        track_list.append(track_dict)

    # Create a DataFrame from the list of tracks
    data_df = pd.DataFrame(track_list)
    return data_df


def load_data(data_df, path):
    """
    Load the transformed data to a CSV file.
    """
    data_df.to_csv(path, index=False)

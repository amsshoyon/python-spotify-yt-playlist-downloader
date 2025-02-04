import os
import re


class SpotifyPlaylistDownloader:
    def __init__(self, base_download_path, playlist_url, playlist_name):
        self.base_folder = os.path.join(base_download_path, "spotify")
        self.playlist_url = playlist_url
        self.playlist_name = playlist_name

    def get_playlist_name(self):
        return self.playlist_name or re.search(r"(?<=playlist/)([A-Za-z0-9_-]+)", self.playlist_url).group(0)

    def get_download_path(self):
        playlist_name = self.get_playlist_name()
        download_folder = os.path.join(self.base_folder, playlist_name)
        os.makedirs(download_folder, exist_ok=True)
        return download_folder

    def download_playlist(self):
        download_path = self.get_download_path()
        print(f"Downloading playlist to: {download_path}")
        spotdl_command = f'spotdl {self.playlist_url} --output "{download_path}"'
        os.system(spotdl_command)
        print(f"Task Completed.")

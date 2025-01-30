import os
import spotdl
import re
import subprocess

def download_playlist(playlist_url):
    deault_playlist_name = playlist_name or re.search(r"(?<=playlist/)([A-Za-z0-9_-]+)", playlist_url).group(0)
    
    download_folder = f"downloads/{playlist_name}"

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    print(f"Downloading playlist from: {playlist_url}")
    
    spotdl_command = f"spotdl {playlist_url} --output \"{download_folder}/%(title)s.%(ext)s\""
    os.system(spotdl_command)

playlist_url = input("Enter the Spotify playlist URL: ")
playlist_name = input("Enter the desired name for playlist: ")
download_playlist(playlist_url)

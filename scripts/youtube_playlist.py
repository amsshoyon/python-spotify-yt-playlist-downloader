import os
import subprocess

from dotenv import load_dotenv

load_dotenv()

ffmpeg_path = os.getenv("FFMPEG_PATH")


class YouTubePlaylistDownloader:
    def __init__(self, base_download_path, playlist_url, playlist_name):
        self.base_download_path = os.path.join(base_download_path, "youtube")
        self.playlist_url = playlist_url
        self.playlist_name = playlist_name or self.get_playlist_name()
        self.audio_download_path = None
        self.video_download_path = None

    def create_download_path(self, choice):
        self.audio_download_path = os.path.join(self.base_download_path, "audio", self.playlist_name)
        self.video_download_path = os.path.join(self.base_download_path, "video", self.playlist_name)

        if choice in [1, 3]:
            os.makedirs(self.audio_download_path, exist_ok=True)
        if choice in [2, 3]:
            os.makedirs(self.video_download_path, exist_ok=True)

    def get_playlist_name(self):
        command = ["yt-dlp", "--flat-playlist", "--print", "%(playlist_title)s", self.playlist_url]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip() or "Unknown_Playlist"

    def download_audio(self):
        print(f"\n🎵 Downloading audio from: {self.playlist_url}")

        command = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--ffmpeg-location", ffmpeg_path,
            "--output", f"{self.audio_download_path}/%(title)s.%(ext)s",
            self.playlist_url
        ]

        subprocess.run(command)
        print(f"✅ Audio downloaded successfully! Saved in: {self.audio_download_path}\n")

    def download_video(self):
        print(f"\n🎥 Downloading videos from: {self.playlist_url}")

        command = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",
            "--merge-output-format", "mp4",
            "--ffmpeg-location", ffmpeg_path,
            "--output", f"{self.video_download_path}/%(title)s.%(ext)s",
            self.playlist_url
        ]

        subprocess.run(command)
        print(f"✅ Video downloaded successfully! Saved in: {self.video_download_path}\n")

    def get_download_choice(self):
        print("\n📌 What do you want to download?")
        print("1️⃣ Audio only (MP3), 2️⃣ Video only (MP4), 3️⃣ Both Audio & Video")
        return input("\nEnter your choice (1/2/3): ").strip()

    def download(self):
        choice = self.get_download_choice()
        self.create_download_path(choice)

        if choice == "1":
            self.download_audio()
        elif choice == "2":
            self.download_video()
        elif choice == "3":
            self.download_audio()
            self.download_video()
        else:
            print("\n❌ Invalid choice! Please enter 1, 2, or 3.")
